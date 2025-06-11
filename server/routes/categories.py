from flask import jsonify, Response, Blueprint
from models import db, Category
from sqlalchemy.orm import Query

# Create a Blueprint for category routes
categories_bp = Blueprint('categories', __name__)

def get_categories_base_query() -> Query:
    """
    Create and return a base query for categories
    
    Returns:
        Query: SQLAlchemy query object for categories
    """
    return db.session.query(Category).order_by(Category.name)

@categories_bp.route('/api/categories', methods=['GET'])
def get_categories() -> Response:
    """
    Get all categories
    Returns:
        Response: JSON response with list of categories
    """
    categories_query = get_categories_base_query().all()
    categories_list = [category.to_dict() for category in categories_query]
    return jsonify(categories_list)
