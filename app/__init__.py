from flask import Flask, jsonify
from .config import Config
from .extensions import db, migrate, cors, swagger, build_swagger_template
from .routes import register_blueprints
from .errors import register_error_handlers
from flasgger import Swagger
def create_app(config_object: type[Config] = Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_object)

    cors.init_app(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)
    db.init_app(app)
    migrate.init_app(app, db)

    Swagger(app, template=build_swagger_template())

    register_blueprints(app)


    register_error_handlers(app)


    return app
