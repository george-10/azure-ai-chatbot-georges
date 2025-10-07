from datetime import datetime

def chat_to_dict(chat) -> dict:
    return {
        "id": chat.id,
        "message_count": len(chat.messages),
    }

def message_to_dict(msg) -> dict:
    ts = msg.timestamp.isoformat() if isinstance(msg.timestamp, datetime) else str(msg.timestamp)
    return {
        "id": msg.id,
        "role": msg.role,
        "content": msg.content,
        "timestamp": ts,
        "chat_id": msg.chat_id,
    }
