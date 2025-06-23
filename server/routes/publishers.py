from flask import Blueprint, jsonify
from ..models.publisher import Publisher
from ..database import db

publishers_bp = Blueprint('publishers', __name__)

@publishers_bp.route('', methods=['GET'])
def get_publishers():
    """Get all publishers"""
    publishers = Publisher.query.all()
    return jsonify([publisher.to_dict() for publisher in publishers])
