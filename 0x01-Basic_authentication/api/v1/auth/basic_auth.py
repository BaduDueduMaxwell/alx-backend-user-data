#!/usr/bin/env python3
"""
Route module for the API
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Basic Auth class that inherits from Auth.
    For now, this class is empty, but will be implemented later.
    """
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """Returns the Base64 part of the
        Authorization header for Basic Auth.
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split(" ", 1)[1]
