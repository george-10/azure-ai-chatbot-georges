from flask import jsonify

def register_error_handlers(app):
    @app.errorhandler(400)
    def bad_request(e):
        return jsonify(error="Bad Request", message=getattr(e, "description", str(e))), 400

    @app.errorhandler(404)
    def not_found(e):
        return jsonify(error="Not Found", message=getattr(e, "description", str(e))), 404
