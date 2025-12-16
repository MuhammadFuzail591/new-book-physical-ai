import uuid
import time
import logging
from typing import List, Tuple, Optional
from ..models.models import Query, Response as ResponseModel, Context, Source, Message
from ..services.qdrant_service import qdrant_service
from ..services.cohere_service import cohere_service
from ..services.query_validation_service import query_validation_service
from ..config.settings import get_settings

# Initialize logging
logger = logging.getLogger(__name__)

class ChatService:
    """
    Main service for handling chat queries and responses
    """

    def __init__(self):
        self.settings = get_settings()

    def process_query(self, query: Query, conversation_history: Optional[List[Message]] = None) -> ResponseModel:
        """
        Process a user query and return a response

        Args:
            query: The user query object
            conversation_history: Optional conversation history for context

        Returns:
            ResponseModel with the answer and metadata
        """
        start_time = time.time()

        # Validate the query
        is_valid, error_msg = query_validation_service.validate_query_object(query)
        if not is_valid:
            raise ValueError(error_msg)

        logger.info(f"Processing query: {query.query_text[:100]}...")

        try:
            # Create embedding for the query
            query_embedding = cohere_service.embed_text(query.query_text, input_type="search_query")

            # Search for similar content in Qdrant
            contexts = qdrant_service.search_similar(
                query_vector=query_embedding,
                limit=self.settings.max_contexts_per_query
            )

            # Check if we found relevant contexts
            if not contexts or all(ctx.score < self.settings.context_similarity_threshold for ctx in contexts):
                # If no relevant contexts found, return "I don't know" response
                response = ResponseModel(
                    response_text="I don't know. The textbook does not contain information about this topic.",
                    sources=[],
                    confidence=0.0,
                    query_id=str(uuid.uuid4())
                )
            else:
                # Filter contexts based on similarity threshold
                relevant_contexts = [ctx for ctx in contexts if ctx.score >= self.settings.context_similarity_threshold]

                # Prepare the query with conversation context if available
                if conversation_history:
                    # Format conversation history for context
                    history_context = self._format_conversation_history(conversation_history)
                    full_query = f"{history_context}\n\nCurrent question: {query.query_text}"
                else:
                    full_query = query.query_text

                # Generate response using Cohere with the retrieved contexts
                response_text, sources = cohere_service.generate_response_with_sources(
                    query=full_query,
                    contexts=relevant_contexts,
                    max_tokens=self.settings.max_response_tokens,
                    temperature=self.settings.default_temperature
                )

                # Calculate confidence based on the highest similarity score
                confidence = max(ctx.score for ctx in relevant_contexts) if relevant_contexts else 0.0

                response = ResponseModel(
                    response_text=response_text,
                    sources=sources,
                    confidence=confidence,
                    query_id=str(uuid.uuid4())
                )

            processing_time = time.time() - start_time
            logger.info(f"Query processed in {processing_time:.2f}s")

            return response

        except Exception as e:
            logger.error(f"Error processing query: {str(e)}", exc_info=True)
            raise

    def _format_conversation_history(self, history: List[Message]) -> str:
        """
        Format conversation history for inclusion in the query context

        Args:
            history: List of messages in the conversation

        Returns:
            Formatted string of conversation history
        """
        if not history:
            return ""

        formatted_history = ["Previous conversation:"]
        for msg in history:
            role_prefix = "User:" if msg.role == "user" else "Assistant:"
            formatted_history.append(f"{role_prefix} {msg.content}")

        return "\n".join(formatted_history)

    def get_contexts_for_query(self, query_text: str) -> List[Context]:
        """
        Get relevant contexts for a query without generating a response

        Args:
            query_text: The query text

        Returns:
            List of Context objects
        """
        # Create embedding for the query
        query_embedding = cohere_service.embed_text(query_text, input_type="search_query")

        # Search for similar content in Qdrant
        contexts = qdrant_service.search_similar(
            query_vector=query_embedding,
            limit=self.settings.max_contexts_per_query
        )

        # Filter contexts based on similarity threshold
        relevant_contexts = [ctx for ctx in contexts if ctx.score >= self.settings.context_similarity_threshold]

        return relevant_contexts

    def generate_response_only(self, query_text: str, contexts: List[Context], conversation_history: Optional[List[Message]] = None) -> Tuple[str, List[Source]]:
        """
        Generate a response based on provided contexts without searching

        Args:
            query_text: The query text
            contexts: List of relevant contexts
            conversation_history: Optional conversation history for context

        Returns:
            Tuple of (response_text, sources)
        """
        # Prepare the query with conversation context if available
        if conversation_history:
            history_context = self._format_conversation_history(conversation_history)
            full_query = f"{history_context}\n\nCurrent question: {query_text}"
        else:
            full_query = query_text

        return cohere_service.generate_response_with_sources(
            query=full_query,
            contexts=contexts,
            max_tokens=self.settings.max_response_tokens,
            temperature=self.settings.default_temperature
        )


# Global instance
chat_service = ChatService()