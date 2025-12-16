import pytest
from datetime import datetime, timedelta
from unittest.mock import patch
from ...src.services.session_service import SessionService
from ...src.models.models import Message


def test_create_session():
    """Test creating a new session"""
    service = SessionService()

    session = service.create_session()

    assert session.session_id is not None
    assert session.created_at <= datetime.utcnow()
    assert session.last_activity <= datetime.utcnow()
    assert session.conversation_history == []


def test_create_session_with_id():
    """Test creating a session with a specific ID"""
    service = SessionService()
    custom_id = "custom-session-id"

    session = service.create_session(custom_id)

    assert session.session_id == custom_id


def test_get_existing_session():
    """Test getting an existing session"""
    service = SessionService()
    session = service.create_session()

    retrieved_session = service.get_session(session.session_id)

    assert retrieved_session is not None
    assert retrieved_session.session_id == session.session_id


def test_get_nonexistent_session():
    """Test getting a non-existent session"""
    service = SessionService()

    retrieved_session = service.get_session("nonexistent-id")

    assert retrieved_session is None


def test_session_timeout():
    """Test that sessions expire after timeout period"""
    # Create service with 1-minute timeout
    service = SessionService(session_timeout_minutes=1)

    # Create a session
    session = service.create_session()

    # Mock the time to be in the past (beyond timeout)
    past_time = datetime.utcnow() - timedelta(minutes=2)

    # Update session's last activity to the past
    session.last_activity = past_time
    service.sessions[session.session_id] = session

    # Try to get the session (should be expired and deleted)
    retrieved_session = service.get_session(session.session_id)

    assert retrieved_session is None


def test_add_message_to_session():
    """Test adding a message to a session"""
    service = SessionService()
    session = service.create_session()

    message = Message(role="user", content="Hello, world!")
    result = service.add_message_to_session(session.session_id, message)

    assert result is True

    updated_session = service.get_session(session.session_id)
    assert len(updated_session.conversation_history) == 1
    assert updated_session.conversation_history[0].role == "user"
    assert updated_session.conversation_history[0].content == "Hello, world!"


def test_add_message_to_nonexistent_session():
    """Test adding a message to a non-existent session"""
    service = SessionService()
    message = Message(role="user", content="Hello, world!")

    result = service.add_message_to_session("nonexistent-id", message)

    assert result is False


def test_get_conversation_history():
    """Test getting conversation history from a session"""
    service = SessionService()
    session = service.create_session()

    # Add some messages
    message1 = Message(role="user", content="First message")
    message2 = Message(role="assistant", content="Second message")

    service.add_message_to_session(session.session_id, message1)
    service.add_message_to_session(session.session_id, message2)

    history = service.get_conversation_history(session.session_id)

    assert len(history) == 2
    assert history[0].content == "First message"
    assert history[1].content == "Second message"


def test_get_conversation_history_with_limit():
    """Test getting limited conversation history"""
    service = SessionService()
    session = service.create_session()

    # Add several messages
    for i in range(5):
        message = Message(role="user", content=f"Message {i}")
        service.add_message_to_session(session.session_id, message)

    # Get only last 2 messages
    history = service.get_conversation_history(session.session_id, limit=2)

    assert len(history) == 2
    assert history[0].content == "Message 3"  # Third to last
    assert history[1].content == "Message 4"  # Last message


def test_validate_session():
    """Test session validation"""
    service = SessionService()
    session = service.create_session()

    is_valid = service.validate_session(session.session_id)

    assert is_valid is True


def test_validate_nonexistent_session():
    """Test validation of non-existent session"""
    service = SessionService()

    is_valid = service.validate_session("nonexistent-id")

    assert is_valid is False


def test_delete_session():
    """Test deleting a session"""
    service = SessionService()
    session = service.create_session()

    # Verify session exists
    assert service.get_session(session.session_id) is not None

    # Delete session
    result = service.delete_session(session.session_id)

    assert result is True
    assert service.get_session(session.session_id) is None


def test_cleanup_expired_sessions():
    """Test cleaning up expired sessions"""
    service = SessionService(session_timeout_minutes=1)

    # Create a session
    session = service.create_session()

    # Manually set last activity to be in the past (beyond timeout)
    past_time = datetime.utcnow() - timedelta(minutes=2)
    session.last_activity = past_time
    service.sessions[session.session_id] = session

    # Clean up expired sessions
    service.cleanup_expired_sessions()

    # Session should be gone
    assert service.get_session(session.session_id) is None


def test_update_session_activity():
    """Test updating session activity time"""
    service = SessionService()
    session = service.create_session()

    # Store original last activity time
    original_time = session.last_activity

    # Wait a moment and update activity
    import time
    time.sleep(0.01)  # Sleep briefly to ensure time difference

    result = service.update_session_activity(session.session_id)

    assert result is True

    updated_session = service.get_session(session.session_id)
    assert updated_session.last_activity > original_time