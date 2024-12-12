from flask import Flask
from app.views.user_view import user_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(user_bp, url_prefix="/users")
    return app