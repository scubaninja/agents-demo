from flask import jsonify, Response, Blueprint
from models import db, Category
from sqlalchemy.orm import Query

# Create a Blueprint for categories routes
categories_bp = Blueprint('categories', __name__)

def get_categories_base_query() -> Query:
    """Get base query for categories with proper joins"""
    return db.session.query(Category).order_by(Category.name)

@categories_bp.route('/api/categories', methods=['GET'])
def get_categories() -> Response:
    """Get all categories"""
    categories_query = get_categories_base_query().all()
    categories_list = [category.to_dict() for category in categories_query]
    return jsonify(categories_list)
