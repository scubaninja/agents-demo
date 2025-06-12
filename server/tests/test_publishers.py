import unittest
import json
from typing import Dict, List, Any
from flask import Flask, Response
from models import db, Publisher, Category, init_db
from routes.publishers import publishers_bp

class TestPublishersRoutes(unittest.TestCase):
    # Test data
    TEST_DATA: Dict[str, List[Dict[str, str]]] = {
        "publishers": [
            {"name": "DevGames Inc", "description": "A test publisher"},
            {"name": "Scrum Masters", "description": "Another test publisher"}
        ]
    }
    
    # API paths
    PUBLISHERS_API_PATH: str = '/api/publishers'

    def setUp(self) -> None:
        """Set up test database and seed data"""
        # Create a fresh Flask app for testing
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        
        # Register the publishers blueprint
        self.app.register_blueprint(publishers_bp)
        
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
        publishers = [
            Publisher(**publisher_data) for publisher_data in self.TEST_DATA["publishers"]
        ]
        db.session.add_all(publishers)
        db.session.commit()

    def _get_response_data(self, response: Response) -> Any:
        """Helper method to parse response data"""
        return json.loads(response.data)

    def test_get_publishers_success(self) -> None:
        """Test successful retrieval of publishers"""
        # Act
        response = self.client.get(self.PUBLISHERS_API_PATH)
        data = self._get_response_data(response)
        
        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), len(self.TEST_DATA["publishers"]))
        for i, publisher_data in enumerate(data):
            test_publisher = self.TEST_DATA["publishers"][i]
            self.assertEqual(publisher_data['name'], test_publisher["name"])
            self.assertEqual(publisher_data['description'], test_publisher["description"])

if __name__ == '__main__':
    unittest.main()
