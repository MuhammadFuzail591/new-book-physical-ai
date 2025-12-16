from fastapi import APIRouter, HTTPException, Depends, status
from typing import Optional
import logging
import time
from ..models.models import Query, Response as ResponseModel, Error
from ..services.chat_service import chat_service
from ..config.settings import get_settings

# Initialize router
router = APIRouter(prefix="/chat", tags=["chat"])

# Initialize logging
logger = logging.getLogger(__name__)

@router.post(
    "/",
    response_model=ResponseModel,
    responses={
        200: {"description": "Successful response with answer to the query"},
        400: {"description": "Invalid query format", "model": Error},
        500: {"description": "Internal server error", "model": Error}
    }
)
async def chat_endpoint(query: Query):
    """
    Submit a query about the textbook content and get a response based on embedded knowledge
    """
    try:
        # Process the query using the chat service (without conversation history for basic chat)
        response = chat_service.process_query(query, conversation_history=None)
        return response

    except ValueError as e:
        # Handle validation errors
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        logger.error(f"Error processing chat query: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error occurred while processing the query"
        )


from ..services.session_service import session_service
from ..models.models import Message


@router.post(
    "/conversation",
    response_model=ResponseModel,
    responses={
        200: {"description": "Successful response with answer to the query"},
        400: {"description": "Invalid query format", "model": Error},
        500: {"description": "Internal server error", "model": Error}
    }
)
async def chat_conversation_endpoint(query: Query):
    """
    Submit a query with conversation context for multi-turn conversations
    """
    try:
        # Validate that session_id is provided
        if not query.session_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="session_id is required for conversation endpoint"
            )

        # Validate session exists
        if not session_service.validate_session(query.session_id):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Session {query.session_id} does not exist or has expired"
            )

        # Add user message to session history
        user_message = Message(role="user", content=query.query_text)
        session_service.add_message_to_session(query.session_id, user_message)

        # Get conversation history for context
        conversation_history = session_service.get_conversation_history(query.session_id, limit=5)  # Get last 5 messages

        # Process the query using the chat service with conversation history
        response = chat_service.process_query(query, conversation_history=conversation_history)

        # Add assistant response to session history
        assistant_message = Message(role="assistant", content=response.response_text)
        session_service.add_message_to_session(query.session_id, assistant_message)

        return response

    except HTTPException:
        # Re-raise HTTP exceptions as they are
        raise
    except Exception as e:
        logger.error(f"Error processing conversation query: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error occurred while processing the conversation query"
        )