import unittest
from unittest.mock import patch, MagicMock
from CRUD_OP.database import get_database

class TestDatabase(unittest.TestCase):
    @patch('CRUD_OP.database.MongoClient')
    @patch('CRUD_OP.database.ServerApi')
    def test_get_database(self, mock_server_api, mock_mongo_client):
        # Setup mocks
        mock_server_api.return_value = MagicMock()
        mock_client_instance = MagicMock()
        mock_mongo_client.return_value = mock_client_instance
        
        student_collection = MagicMock()
        teacher_collection = MagicMock()
        mock_client_instance.cluster0.Student = student_collection
        mock_client_instance.cluster0.Teacher = teacher_collection
        
        # Test get_database function
        result = get_database()
        
        # Check collections are as expected
        self.assertEqual(result[0], student_collection)
        self.assertEqual(result[1], teacher_collection)
        
        # Check collections are not None
        self.assertIsNotNone(result[0], "Student collection is None")
        self.assertIsNotNone(result[1], "Teacher collection is None")

if __name__ == '__main__':
    unittest.main()
