from .extensions import db

class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    messages = db.relationship("ChatMessage", backref="chat", lazy=True, cascade="all, delete-orphan")

class ChatMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())
    chat_id = db.Column(db.Integer, db.ForeignKey("chat.id"), nullable=False)

    def __repr__(self):
        preview = (self.content or "")[:20]
        return f"<ChatMessage {self.role}: {preview}>"
