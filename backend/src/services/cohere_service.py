import os
import logging
from typing import List, Optional
from cohere import Client
from dotenv import load_dotenv
from ..models.models import Context, Source

# Load environment variables
load_dotenv()

# Initialize logging
logger = logging.getLogger(__name__)

class CohereService:
    """
    Service for interacting with Cohere API for response generation
    """

    def __init__(self):
        # Get API key from environment
        self.api_key = os.getenv("COHERE_API_KEY")
        if not self.api_key:
            raise ValueError("COHERE_API_KEY environment variable is required")

        # Initialize Cohere client
        self.client = Client(api_key=self.api_key)

        # Default model for generation
        self.generation_model = os.getenv("COHERE_GENERATION_MODEL", "command-r-plus")

        # Default model for embeddings (from existing embeddings)
        self.embedding_model = os.getenv("COHERE_EMBEDDING_MODEL", "embed-english-v3.0")

        logger.info("Cohere client initialized")

    def generate_response(
        self,
        query: str,
        contexts: List[Context],
        max_tokens: Optional[int] = 500,
        temperature: Optional[float] = 0.7
    ) -> str:
        """
        Generate a response based on the query and retrieved contexts

        Args:
            query: The user's query
            contexts: List of relevant contexts retrieved from Qdrant
            max_tokens: Maximum number of tokens in the response
            temperature: Controls randomness in generation (0.0-1.0)

        Returns:
            Generated response text
        """
        try:
            # Format the contexts for the prompt
            context_texts = []
            for ctx in contexts:
                context_texts.append(f"Source: {ctx.section_title or 'Unknown'}\nContent: {ctx.content}")

            # Combine contexts into a single string
            combined_context = "\n\n".join(context_texts)

            # Create the prompt for Cohere
            prompt = f"""
            You are an AI assistant that helps students understand the Physical AI & Humanoid Robotics textbook.
            Answer the user's question based only on the provided textbook content.
            If the information is not available in the provided context, respond with "I don't know" or "The textbook does not contain information about this topic."

            Context from textbook:
            {combined_context}

            User's question: {query}

            Assistant's answer:
            """

            # Generate the response using Cohere
            response = self.client.generate(
                model=self.generation_model,
                prompt=prompt,
                max_tokens=max_tokens,
                temperature=temperature,
                stop_sequences=["User:", "Assistant:"]
            )

            # Extract the generated text
            generated_text = response.generations[0].text.strip()

            logger.info(f"Generated response for query: {query[:50]}...")
            return generated_text

        except Exception as e:
            logger.error(f"Error generating response with Cohere: {str(e)}")
            raise

    def generate_response_with_sources(
        self,
        query: str,
        contexts: List[Context],
        max_tokens: Optional[int] = 500,
        temperature: Optional[float] = 0.7
    ) -> tuple[str, List[Source]]:
        """
        Generate a response with source attribution

        Args:
            query: The user's query
            contexts: List of relevant contexts retrieved from Qdrant
            max_tokens: Maximum number of tokens in the response
            temperature: Controls randomness in generation (0.0-1.0)

        Returns:
            Tuple of (generated response text, list of sources used)
        """
        try:
            # Generate the response
            response_text = self.generate_response(query, contexts, max_tokens, temperature)

            # Convert contexts to sources
            sources = [
                Source(
                    content=ctx.content,
                    score=ctx.score,
                    page_number=ctx.page_number,
                    section_title=ctx.section_title,
                    metadata=ctx.metadata
                )
                for ctx in contexts
            ]

            return response_text, sources

        except Exception as e:
            logger.error(f"Error generating response with sources: {str(e)}")
            raise

    def check_connection(self) -> bool:
        """
        Check if the Cohere connection is working by making a simple request

        Returns:
            True if connection is successful, False otherwise
        """
        try:
            # Make a simple request to test the connection
            response = self.client.generate(
                model=self.generation_model,
                prompt="Hello, how are you?",
                max_tokens=10,
                temperature=0.7
            )
            return True
        except Exception as e:
            logger.error(f"Cohere connection check failed: {str(e)}")
            return False

    def embed_text(self, text: str, input_type: str = "search_query") -> List[float]:
        """
        Create an embedding for the given text using Cohere

        Args:
            text: Text to embed
            input_type: Type of input (search_query, search_document, classification, etc.)

        Returns:
            List of floats representing the embedding
        """
        try:
            response = self.client.embed(
                model=self.embedding_model,
                input_type=input_type,
                texts=[text],
            )
            return response.embeddings[0]  # Return the first embedding

        except Exception as e:
            logger.error(f"Error creating embedding with Cohere: {str(e)}")
            raise

# Global instance for use in other services
cohere_service = CohereService()