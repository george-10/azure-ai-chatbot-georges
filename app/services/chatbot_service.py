
try:
    from app.chatbot import get_completion_from_messages 
except Exception: 
    get_completion_from_messages = None

def complete(messages_payload: list[dict]) -> str:
    if get_completion_from_messages is None:
        raise RuntimeError("Chatbot backend is not configured.")

    model_resp = get_completion_from_messages(messages_payload)
    if isinstance(model_resp, dict):
        return model_resp.get("content") or model_resp.get("text") or str(model_resp)
    return str(model_resp)
