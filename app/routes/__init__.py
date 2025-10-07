from flask import Flask
from .chats import bp as chats_bp
from .messages import bp as messages_bp

def register_blueprints(app: Flask):
    app.register_blueprint(chats_bp)
    app.register_blueprint(messages_bp)
