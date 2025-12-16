import uuid
import time
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import logging
from threading import Lock

from ..models.models import Session, Message, Query, Context

# Initialize logging
logger = logging.getLogger(__name__)

class SessionService:
    """
    Service for managing conversation sessions and history
    """

    def __init__(self, session_timeout_minutes: int = 30):
        self.sessions: Dict[str, Session] = {}
        self.session_timeout = timedelta(minutes=session_timeout_minutes)
        self.lock = Lock()  # Thread-safe access to sessions
        logger.info(f"Session service initialized with {session_timeout_minutes}-minute timeout")

    def create_session(self, session_id: Optional[str] = None) -> Session:
        """
        Create a new conversation session

        Args:
            session_id: Optional session ID (if not provided, one will be generated)

        Returns:
            Session object
        """
        if session_id is None:
            session_id = str(uuid.uuid4())

        current_time = datetime.utcnow()
        session = Session(
            session_id=session_id,
            created_at=current_time,
            last_activity=current_time,
            conversation_history=[]
        )

        with self.lock:
            self.sessions[session_id] = session

        logger.info(f"Created new session: {session_id}")
        return session

    def get_session(self, session_id: str) -> Optional[Session]:
        """
        Get a session by ID

        Args:
            session_id: The session ID

        Returns:
            Session object or None if not found
        """
        with self.lock:
            session = self.sessions.get(session_id)

        if session:
            # Check if session has expired
            if datetime.utcnow() - session.last_activity > self.session_timeout:
                self.delete_session(session_id)
                logger.info(f"Session {session_id} expired and deleted")
                return None

        return session

    def update_session_activity(self, session_id: str) -> bool:
        """
        Update the last activity time for a session

        Args:
            session_id: The session ID

        Returns:
            True if session exists and was updated, False otherwise
        """
        with self.lock:
            session = self.sessions.get(session_id)
            if session:
                session.last_activity = datetime.utcnow()
                return True
        return False

    def add_message_to_session(self, session_id: str, message: Message) -> bool:
        """
        Add a message to a session's conversation history

        Args:
            session_id: The session ID
            message: The message to add

        Returns:
            True if message was added, False if session doesn't exist
        """
        session = self.get_session(session_id)
        if not session:
            return False

        if session.conversation_history is None:
            session.conversation_history = []

        session.conversation_history.append(message)
        session.last_activity = datetime.utcnow()

        with self.lock:
            self.sessions[session_id] = session

        logger.debug(f"Added message to session {session_id}")
        return True

    def get_conversation_history(self, session_id: str, limit: Optional[int] = None) -> Optional[List[Message]]:
        """
        Get conversation history for a session

        Args:
            session_id: The session ID
            limit: Optional limit on number of messages to return

        Returns:
            List of messages or None if session doesn't exist
        """
        session = self.get_session(session_id)
        if not session:
            return None

        history = session.conversation_history or []
        if limit:
            history = history[-limit:]  # Get last N messages

        return history

    def delete_session(self, session_id: str) -> bool:
        """
        Delete a session

        Args:
            session_id: The session ID to delete

        Returns:
            True if session was deleted, False if it didn't exist
        """
        with self.lock:
            if session_id in self.sessions:
                del self.sessions[session_id]
                logger.info(f"Deleted session: {session_id}")
                return True
        return False

    def cleanup_expired_sessions(self):
        """
        Remove all expired sessions
        """
        current_time = datetime.utcnow()
        expired_sessions = []

        with self.lock:
            for session_id, session in self.sessions.items():
                if current_time - session.last_activity > self.session_timeout:
                    expired_sessions.append(session_id)

        for session_id in expired_sessions:
            self.delete_session(session_id)

    def validate_session(self, session_id: str) -> bool:
        """
        Validate that a session exists and is active

        Args:
            session_id: The session ID to validate

        Returns:
            True if session is valid, False otherwise
        """
        return self.get_session(session_id) is not None


# Global instance
session_service = SessionService()