#!/usr/bin/env python3
"""
Route module for the API
"""
from typing import List, TypeVar
from flask import request


class Auth:
    """
    Manage API authentication methods
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Determines if authentication is required"""
        if path is None or not excluded_paths:
            return True

        normalized_path = path.rstrip('/')

        for excluded_path in excluded_paths:
            # Remove the trailing slash and check for wildcard (*) at the end
            normalized_excluded_path = excluded_path.rstrip('/')
            
            # If excluded_path ends with '*', match the prefix
            if normalized_excluded_path.endswith('*'):
                if normalized_path.startswith(normalized_excluded_path[:-1]):
                    return False
            elif normalized_path == normalized_excluded_path:
                return False

        return True


    def authorization_header(self, request=None) -> str:
        """Returns the authorization header from the request"""
        if request is None:
            return None
        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns the current user based on the request"""
        return None  # Placeholder for now
