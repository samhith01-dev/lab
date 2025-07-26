from flask import Blueprint, request, jsonify
from services.user_service import create_user, get_users

user_bp = Blueprint('user_bp', __name__, url_prefix='/users')

@user_bp.route('/', methods=['GET'])
def list_users():
    return jsonify(get_users())

@user_bp.route('/', methods=['POST'])
def add_user():
    data = request.get_json()
    return jsonify(create_user(data)), 201