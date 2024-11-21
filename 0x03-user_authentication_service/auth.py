#!/usr/bin/env python3
""" Hash password
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Hash a password using bcrypt and return the salted hash as bytes."""
    # Generate a salt
    salt = bcrypt.gensalt()

    # Hash the password with the salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password
