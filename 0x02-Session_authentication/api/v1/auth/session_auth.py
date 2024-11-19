#!/usr/bin/env python3
"""
SessionAuth module for handling session-based authentication.
"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """ SessionAuth class for session-based authentication
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Creates a Session ID for a user_id
        """
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        # Generate a new session ID using uuid4
        session_id = str(uuid.uuid4())

        # Store the session ID and user_id in the dictionay
        self.user_id_by_session_id[session_id] = user_id

        return session_id
