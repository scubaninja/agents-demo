import unittest
import json
from typing import Dict, List, Any
from flask import Flask, Response
from models import db, Category, init_db
from routes.categories import categories_bp

class TestCategoriesRoutes(unittest.TestCase):
    # Test data
    TEST_DATA: Dict[str, List[Dict[str, str]]] = {
        "categories": [
            {"name": "Strategy", "description": "Strategy games"},
            {"name": "Card Game", "description": "Card-based games"}
        ]
    }
    
    # API paths
    CATEGORIES_API_PATH: str = '/api/categories'

    def setUp(self) -> None:
        """Set up test database and seed data"""
        # Create a fresh Flask app for testing
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        
        # Register the categories blueprint
        self.app.register_blueprint(categories_bp)
        
        # Initialize the test client
        self.client = self.app.test_client()
        
        # Initialize in-memory database for testing
        init_db(self.app, testing=True)
        
        # Create tables and seed data
        with self.app.app_context():
            db.create_all()
            self._seed_test_data()

    def tearDown(self) -> None:
        """Clean up test database"""
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
            db.engine.dispose()

    def _seed_test_data(self) -> None:
        """Helper method to seed test data"""
        categories = [
            Category(**category_data) for category_data in self.TEST_DATA["categories"]
        ]
        db.session.add_all(categories)
        db.session.commit()

    def _get_response_data(self, response: Response) -> Any:
        """Helper method to parse response data"""
        return json.loads(response.data)

    def test_get_categories_success(self) -> None:
        """Test successful retrieval of categories"""
        # Act
        response = self.client.get(self.CATEGORIES_API_PATH)
        data = self._get_response_data(response)
        
        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), len(self.TEST_DATA["categories"]))
        for i, category_data in enumerate(data):
            test_category = self.TEST_DATA["categories"][i]
            self.assertEqual(category_data['name'], test_category["name"])
            self.assertEqual(category_data['description'], test_category["description"])

if __name__ == '__main__':
    unittest.main()
