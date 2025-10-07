# app/api/chats.py
from flask import Blueprint, jsonify, abort
from flasgger.utils import swag_from
from sqlalchemy.exc import SQLAlchemyError

from ..extensions import db
from ..models import Chat, ChatMessage
from ..serializers import chat_to_dict
from ..prompts import get_initial_system_prompt

bp = Blueprint("chats", __name__)

@bp.route("/chats", methods=["GET"])
@swag_from({
    "tags": ["Chats"],
    "responses": {
        200: {
            "description": "A list of chats",
            "schema": {"type": "array", "items": {"$ref": "#/definitions/Chat"}},
            "examples": {"application/json": [{"id": 1, "message_count": 3}, {"id": 2, "message_count": 0}]},
        },
        400: {"description": "Bad Request"},
        404: {"description": "Not Found"},
    },
})
def get_chats():
    try:
        chats = Chat.query.all()
        return jsonify([chat_to_dict(c) for c in chats]), 200
    except SQLAlchemyError as e:
        abort(400, description="Failed to fetch chats")

@bp.route("/chats", methods=["POST"])
@swag_from({
    "tags": ["Chats"],
    "responses": {
        201: {
            "description": "Chat created",
            "schema": {"$ref": "#/definitions/Chat"},
            "examples": {"application/json": {"id": 3, "message_count": 0}},
        },
        400: {"description": "Bad Request"},
        404: {"description": "Not Found"},
    },
})
def create_chat():
    try:
        chat = Chat()
        db.session.add(chat)
        db.session.flush()  

        sys_msg = ChatMessage(
            role="system",
            content=get_initial_system_prompt(),
            chat_id=chat.id,
        )
        db.session.add(sys_msg)
        db.session.commit()

        return jsonify(chat_to_dict(chat)), 201

    except SQLAlchemyError as e:
        db.session.rollback()
        abort(400, description="Failed to create chat")
