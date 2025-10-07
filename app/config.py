import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "postgresql://myuser:mypassword@localhost/postgres"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SWAGGER = {
        "title": "Chat API",
        "uiversion": 3,  
    }
