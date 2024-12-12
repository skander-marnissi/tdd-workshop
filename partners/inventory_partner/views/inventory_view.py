from uuid import uuid4
from flask import request, jsonify, Blueprint

inventory_bp = Blueprint("inventory", __name__)

@inventory_bp.route("/products/<product_id:string>/<quantity:integer>", methods=["GET"])
def get_user_detail(product_id,quantity):
    is_available = bool(product_id) and bool(quantity)
    return jsonify({'product_id':product_id, 'quantity':quantity, 'is_availabe':is_available}), 200
