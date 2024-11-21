# User Authentication Service

## Project Overview

This project is designed to walk you through the process of creating a user authentication system from scratch using Flask and SQLAlchemy, to understand the inner workings of authentication systems in web development. While it’s generally recommended to use a pre-built authentication system like Flask-User in production, this project focuses on learning and understanding the process through implementation.

## Learning Objectives

By the end of this project, you will be able to:

- Declare API routes in a Flask app.
- Get and set cookies in Flask.
- Retrieve request form data from the user.
- Return various HTTP status codes based on different situations.

## Technologies

- **Flask**: A web framework for Python used to create the backend of the application.
- **SQLAlchemy**: A Python ORM used to interact with the database.
- **bcrypt**: A password hashing library used to securely hash passwords.

## Requirements

- **Allowed Editors:** vi, vim, emacs
- **Environment:** Ubuntu 18.04 LTS, Python 3.7
- **Files Should End With a New Line**
- **First Line of Each File Should Be:** `#!/usr/bin/env python3`
- **Pycodestyle:** Your code should adhere to PEP 8 style using pycodestyle version 2.5.
- **SQLAlchemy version:** 1.3.x
- **All files must be executable.**
- **All classes, functions, and modules must be properly documented.**

## Setup Instructions

To set up the project, you will need to install the necessary dependencies.

1. **Install bcrypt**:
   ```
   pip3 install bcrypt
   ```

2. **Clone the GitHub repository** for the project:
   ```
   git clone https://github.com/your-repository/alx-backend-user-data.git
   ```

3. **Navigate to the project directory**:
   ```
   cd alx-backend-user-data/0x03-user_authentication_service
   ```

## Project Tasks

### 0. User Model

In this task, you will create a `User` model using SQLAlchemy for a table named `users` with the following fields:
- `id`: Integer primary key.
- `email`: A non-nullable string.
- `hashed_password`: A non-nullable string.
- `session_id`: A nullable string.
- `reset_token`: A nullable string.

The model will be defined in the `user.py` file.

Example usage:
```python
from user import User
print(User.__tablename__)
for column in User.__table__.columns:
    print("{}: {}".format(column, column.type))
```

### 1. Create User

You will implement the `add_user` method in the `DB` class to create a new user and save it to the database.

### 2. Find User

Implement the `find_user_by` method in the `DB` class, which allows you to search for a user by arbitrary keyword arguments.

### 3. Update User

You will implement the `update_user` method that allows you to update user attributes using keyword arguments. If invalid attributes are passed, raise a `ValueError`.

### 4. Hash Password

Define the `_hash_password` method to hash the password using bcrypt and return the hashed password as bytes.

### 5. Register User

You will implement the `register_user` method in the `Auth` class. This method should handle user registration, hash the password, and store the user in the database. It will raise a `ValueError` if a user with the provided email already exists.

### 6. Basic Flask App

Set up a basic Flask app with a single route (`/`) that returns a JSON payload `{"message": "Bienvenue"}`.

Example:
```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify({"message": "Bienvenue"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
```

### 7. Register User API Endpoint

Create a Flask API endpoint at `/users` that accepts POST requests for user registration. The endpoint should accept form data for `email` and `password`. If the user already exists, return a 400 status with a message indicating the email is already registered.

Example:
```bash
curl -XPOST localhost:5000/users -d 'email=bob@me.com' -d 'password=mySuperPwd' -v
```

## Code Structure

- **user.py**: Contains the SQLAlchemy `User` model.
- **db.py**: Contains the `DB` class with methods to interact with the database.
- **auth.py**: Contains the `Auth` class that handles user authentication.
- **app.py**: Flask app that sets up the basic routes and user registration endpoint.

## Testing the Application

1. **Running the Flask App**:
   ```
   python3 app.py
   ```

2. **Using curl to test the POST /users endpoint**:
   ```
   curl -XPOST localhost:5000/users -d 'email=bob@me.com' -d 'password=mySuperPwd' -v
   ```

3. **Testing registration with an existing user**:
   ```
   curl -XPOST localhost:5000/users -d 'email=bob@me.com' -d 'password=mySuperPwd' -v
   ```
