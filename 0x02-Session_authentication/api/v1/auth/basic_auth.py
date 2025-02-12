#!/usr/bin/env python3
"""
Route module for the API
"""
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User


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

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """ Returns the user instance based on his email and password"""
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        # Look for the user in the databse by email
        users = User.search({"email": user_email})
        if not users:
            return None
        user = users[0]
        if not user.is_valid_password(user_pwd):
            return None
        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the user instance based on the Authorization header.
        """
        # Get the authorization header
        authorization_header = self.authorization_header(request)

        if not authorization_header:
            return None

        # Extract Base64 encoded credentials
        base64_authorization_header = self.extract_base64_authorization_header(
            authorization_header)

        if not base64_authorization_header:
            return None

        # Decode the Base64 authorization header
        decoded_authorization_header = self.decode_base64_authorization_header(
            base64_authorization_header)

        if not decoded_authorization_header:
            return None

        # Extract the user credentials (email and password)
        user_email, user_pwd = self.extract_user_credentials(
            decoded_authorization_header)

        if not user_email or not user_pwd:
            return None

        # Get the User instance based on the credentials
        return self.user_object_from_credentials(user_email, user_pwd)
