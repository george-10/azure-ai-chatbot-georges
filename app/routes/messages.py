from flask import Blueprint, jsonify, request
from flasgger.utils import swag_from
from ..extensions import db
from ..models import Chat, ChatMessage
from ..serializers import message_to_dict
from ..services.chatbot_service import complete

bp = Blueprint("messages", __name__)

@bp.route("/chats/<int:chat_id>/messages", methods=["GET"])
@swag_from({
    "tags": ["Messages"],
    "parameters": [
        {"name": "chat_id", "in": "path", "type": "integer", "required": True, "description": "The ID of the chat"},
    ],
    "responses": {
        200: {
            "description": "A list of messages for the chat",
            "schema": {"type": "array", "items": {"$ref": "#/definitions/ChatMessage"}},
        },
        404: {"description": "Chat not found"},
    },
})
def get_chat_messages(chat_id):
    chat = Chat.query.get(chat_id)
    if chat is None:
        return jsonify(error="Not Found", message="Chat not found"), 404

    messages = (
        ChatMessage.query
        .filter_by(chat_id=chat.id)
        .order_by(ChatMessage.id.asc())
        .offset(1)                       
        .all()
    )

    return jsonify([message_to_dict(m) for m in messages]), 200


@bp.route("/chats/<int:chat_id>/messages", methods=["POST"])
@swag_from({
    "tags": ["Messages"],
    "parameters": [
        {"name": "chat_id", "in": "path", "type": "integer", "required": True, "description": "The ID of the chat"},
        {
            "in": "body",
            "name": "body",
            "required": True,
            "schema": {"$ref": "#/definitions/CreateMessagePayload"},
            "description": "Message payload",
        },
    ],
    "responses": {
        201: {"description": "Message created", "schema": {"$ref": "#/definitions/ChatMessage"}},
        400: {"description": "Invalid payload"},
        404: {"description": "Chat not found"},
    },
})
def create_message(chat_id):
    chat = Chat.query.get(chat_id)
    if chat is None:
        return jsonify(error="Not Found", message="Chat not found"), 404

    data = request.get_json(silent=True) or {}
    role = (data.get("role") or "").strip()
    content = (data.get("content") or "").strip()
    if not role or not content:
        return jsonify(error="Bad Request", message="Both 'role' and 'content' are required"), 400

    msg = ChatMessage(role=role, content=content, chat_id=chat.id)
    db.session.add(msg)
    db.session.commit()

    convo = (
        ChatMessage.query
        .filter_by(chat_id=chat.id)
        .order_by(ChatMessage.id.asc())
        .all()
    )
    messages_payload = [{"role": m.role, "content": m.content} for m in convo]

    try:
        response_text = complete(messages_payload)
    except Exception as e:
        return jsonify(error="ModelError", message=str(e)), 500

    resp_msg = ChatMessage(role="assistant", content=response_text, chat_id=chat.id)
    db.session.add(resp_msg)
    db.session.commit()

    return jsonify(message_to_dict(resp_msg)), 201


@bp.route("/chats/<int:chat_id>", methods=["DELETE"])
@swag_from({
    "tags": ["Chats"],
    "parameters": [
        {"name": "chat_id", "in": "path", "type": "integer", "required": True, "description": "The ID of the chat"},
    ],
    "responses": {
        204: {"description": "Chat deleted"},
        404: {"description": "Chat not found"},
    },
})
def delete_chat(chat_id):
    chat = Chat.query.get(chat_id)
    if chat is None:
        return jsonify(error="Not Found", message="Chat not found"), 404

    db.session.delete(chat)
    db.session.commit()
    return ("", 204)
