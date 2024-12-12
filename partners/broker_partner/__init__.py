from flask import Flask
from partners.broker_partner.views.order_view import order_bp

def create_app():
    app = Flask(__name__)
    # Register Blueprints
    app.register_blueprint(order_bp, url_prefix="/orders")

    return app