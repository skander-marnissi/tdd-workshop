from flask import Flask

from partners.inventory_partner.views.inventory_view import inventory_bp


def create_app():
    app = Flask(__name__)
    # Register Blueprints
    app.register_blueprint(inventory_bp, url_prefix="/inventory")

    return app