from flask import Blueprint, request, jsonify
from app.services.user_service import UserService

user_bp = Blueprint('users', __name__)


@user_bp.route('/', methods=['POST'])
def create_user():
    payload = request.get_json()
    user_service = UserService()

    required_fields = ['firstname', 'lastname', 'email', 'age', 'phone']
    if not all(field in payload for field in required_fields):
        return jsonify({"error": "Missing fields"}), 400

    user = user_service.create_user(
        firstname=payload.get('firstname'),
        lastname=payload.get('lastname'),
        email=payload.get('email'),
        age=payload.get('age'),
        phone=payload.get('phone')
    )
    return jsonify(user.__dict__), 201

@user_bp.route('/', methods=['GET'])
def get_users():
    user_service = UserService()
    users = user_service.get_users()
    return jsonify([user.__dict__ for user in users]), 200