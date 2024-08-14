from flask import Blueprint, request, jsonify
from backend.services.blockchain_service import create_wallet, get_balance

wallet_bp = Blueprint('wallet', __name__)

@wallet_bp.route('/create', methods=['POST'])
def create():
    data = request.get_json()
    wallet = create_wallet(data['user_id'])
    return jsonify(wallet)

@wallet_bp.route('/balance/<wallet_id>', methods=['GET'])
def balance(wallet_id):
    balance = get_balance(wallet_id)
    return jsonify(balance)
