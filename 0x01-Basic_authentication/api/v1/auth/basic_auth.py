#!/usr/bin/env python3
"""
Route module for the API
"""
from api.v1.auth.auth import Auth
import base64


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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ Returns the decoded value of a Base64 string
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded = base64.b64decode(
                base64_authorization_header, validate=True)
            return decoded.decode('utf-8')
        except (base64.binascii.Error, ValueError):
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """ Returns the user email and password from Base64 decoded value
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        email, password = decoded_base64_authorization_header.split(":", 1)
        return email, password
