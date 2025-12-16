import re
from typing import Optional
from ..models.models import Query
from ..config.settings import get_settings

class QueryValidationService:
    """
    Service for validating user queries before processing
    """

    @staticmethod
    def validate_query_text(query_text: str) -> tuple[bool, Optional[str]]:
        """
        Validate the query text based on length and content requirements

        Args:
            query_text: The query text to validate

        Returns:
            Tuple of (is_valid, error_message)
        """
        settings = get_settings()

        # Check if query is empty or contains only whitespace
        if not query_text or not query_text.strip():
            return False, "Query cannot be empty or contain only whitespace"

        # Check query length
        if len(query_text) > settings.max_query_length:
            return False, f"Query exceeds maximum length of {settings.max_query_length} characters"

        if len(query_text.strip()) < settings.min_query_length:
            return False, f"Query must be at least {settings.min_query_length} characters long"

        # Check for potentially malicious content (basic validation)
        # This could be expanded based on specific requirements
        if QueryValidationService._contains_malicious_content(query_text):
            return False, "Query contains potentially malicious content"

        return True, None

    @staticmethod
    def _contains_malicious_content(query_text: str) -> bool:
        """
        Check if the query contains potentially malicious content
        This is a basic implementation - expand based on security requirements

        Args:
            query_text: The query text to check

        Returns:
            True if malicious content is detected, False otherwise
        """
        # Convert to lowercase for case-insensitive matching
        text_lower = query_text.lower()

        # Check for SQL injection patterns
        sql_patterns = [
            r"drop\s+\w+", r"delete\s+from", r"insert\s+into", r"update\s+\w+\s+set",
            r"exec\s*\(", r"execute\s*\(", r"sp_", r"xp_"
        ]

        for pattern in sql_patterns:
            if re.search(pattern, text_lower):
                return True

        # Check for script tags (XSS prevention)
        if "<script" in text_lower or "javascript:" in text_lower:
            return True

        # Check for system command patterns
        command_patterns = [r"\|\|", r"&&", r";", r"`", r"\$"]
        for pattern in command_patterns:
            if re.search(pattern, query_text):
                # Additional check to see if it's part of a legitimate query
                # For now, we'll be permissive but this can be made more strict
                pass

        return False

    @staticmethod
    def validate_query_object(query: Query) -> tuple[bool, Optional[str]]:
        """
        Validate a Query object

        Args:
            query: The Query object to validate

        Returns:
            Tuple of (is_valid, error_message)
        """
        # Validate the query text
        is_valid, error_msg = QueryValidationService.validate_query_text(query.query_text)
        if not is_valid:
            return False, error_msg

        # Validate session_id if provided
        if query.session_id:
            # Basic pattern validation for session_id
            if not re.match(r"^[a-zA-Z0-9_-]+$", query.session_id):
                return False, "Invalid session_id format"

        # Validate user_id if provided
        if query.user_id:
            # Basic pattern validation for user_id
            if not re.match(r"^[a-zA-Z0-9_-]+$", query.user_id):
                return False, "Invalid user_id format"

        return True, None


# Global instance
query_validation_service = QueryValidationService()