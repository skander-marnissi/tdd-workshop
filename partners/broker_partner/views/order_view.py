from uuid import uuid4
from flask import request, jsonify, Blueprint

order_bp = Blueprint("order", __name__)

@order_bp.route("/", methods=["POST"])
def create_order():
    product_id = request.args.get("product_id")
    nb_of_unit =  request.args.get("nb_of_unit")
    generated_order_id = str(uuid4())

    return jsonify({'order_id':generated_order_id, 'product_id':product_id, 'nb_of_unit':nb_of_unit}), 200
