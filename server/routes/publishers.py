from flask import jsonify, Response, Blueprint
from models import db, Publisher
from sqlalchemy.orm import Query

# Create a Blueprint for publishers routes
publishers_bp = Blueprint('publishers', __name__)

def get_publishers_base_query() -> Query:
    """Get base query for publishers with proper joins"""
    return db.session.query(Publisher).order_by(Publisher.name)

@publishers_bp.route('/api/publishers', methods=['GET'])
def get_publishers() -> Response:
    """Get all publishers"""
    publishers_query = get_publishers_base_query().all()
    publishers_list = [publisher.to_dict() for publisher in publishers_query]
    return jsonify(publishers_list)