from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flasgger import Swagger
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
swagger = Swagger()
cors = CORS()

def build_swagger_template():
    return {
        "swagger": "2.0",
        "info": {
            "title": "Chat API",
            "version": "1.0.0",
            "description": "Simple Chat API with Flask, SQLAlchemy, and Swagger (Flasgger).",
        },
        "basePath": "/",
        "schemes": ["http"],
        "consumes": ["application/json"],
        "produces": ["application/json"],
        "definitions": {
            "Chat": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "message_count": {"type": "integer"},
                },
            },
            "ChatMessage": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "role": {"type": "string"},
                    "content": {"type": "string"},
                    "timestamp": {"type": "string", "format": "date-time"},
                    "chat_id": {"type": "integer"},
                },
                "required": ["role", "content", "chat_id"],
            },
            "CreateMessagePayload": {
                "type": "object",
                "required": ["role", "content"],
                "properties": {
                    "role": {"type": "string", "example": "user"},
                    "content": {"type": "string", "example": "Hello there!"},
                },
            },
        },
    }
