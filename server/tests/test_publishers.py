import unittest
import json
from server.app import app
from server.database import db
from server.models.publisher import Publisher

class TestPublishersRoute(unittest.TestCase):
    def setUp(self):
        """Set up test environment"""
        self.app = app.test_client()
        self.app.testing = True
        
        # Create an application context
        with app.app_context():
            # Create the database and tables
            db.create_all()
            
            # Add test data
            test_publisher1 = Publisher(name="Test Publisher 1", website="https://testpublisher1.com")
            test_publisher2 = Publisher(name="Test Publisher 2", website="https://testpublisher2.com")
            db.session.add(test_publisher1)
            db.session.add(test_publisher2)
            db.session.commit()
    
    def tearDown(self):
        """Clean up after tests"""
        with app.app_context():
            db.session.remove()
            db.drop_all()
    
    def test_get_publishers(self):
        """Test getting all publishers"""
        response = self.app.get('/api/publishers')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['name'], 'Test Publisher 1')
        self.assertEqual(data[1]['name'], 'Test Publisher 2')

if __name__ == '__main__':
    unittest.main()
