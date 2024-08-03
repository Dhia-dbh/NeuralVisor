import unittest
from unittest.mock import MagicMock
from pymongo import errors
from CRUD_OP.teacher_db import add_teacher, update_teacher, delete_teacher, get_all_teachers

class TestTeacherDB(unittest.TestCase):
    def setUp(self):
        self.mock_collection = MagicMock()

    def test_add_teacher_success(self):
        data = {
            'FirstName': 'Jane',
            'LastName': 'Smith',
            'Email': 'jane.smith@example.com',
            'Password': 'securepassword'
        }
        self.mock_collection.insert_one = MagicMock()
        response = add_teacher(self.mock_collection, data)
        self.assertEqual(response[0], {"message": "Teacher Added"})
        self.assertEqual(response[1], 200)

    def test_add_teacher_duplicate(self):
        data = {
            'FirstName': 'Jane',
            'LastName': 'Smith',
            'Email': 'jane.smith@example.com',
            'Password': 'securepassword'
        }
        self.mock_collection.insert_one = MagicMock(side_effect=errors.DuplicateKeyError("Duplicate key error"))
        response = add_teacher(self.mock_collection, data)
        self.assertEqual(response[0], {"message": "A Teacher with this email already exists."})
        self.assertEqual(response[1], 400)

    def test_update_teacher_success(self):
        data = {
            'FirstName': 'Jane',
            'LastName': 'Smith',
            'Email': 'jane.smith@example.com',
            'Password': 'newpassword'
        }
        self.mock_collection.update_one = MagicMock(return_value=MagicMock(matched_count=1))
        response = update_teacher(self.mock_collection, data)
        self.assertEqual(response[0], {"message": "Teacher Updated"})
        self.assertEqual(response[1], 200)

    def test_update_teacher_not_found(self):
        data = {
            'FirstName': 'Jane',
            'LastName': 'Smith',
            'Email': 'jane.smith@example.com',
            'Password': 'newpassword'
        }
        self.mock_collection.update_one = MagicMock(return_value=MagicMock(matched_count=0))
        response = update_teacher(self.mock_collection, data)
        self.assertEqual(response[0], {"message": "No teacher found with the given email"})
        self.assertEqual(response[1], 404)

    def test_delete_teacher_success(self):
        self.mock_collection.delete_one = MagicMock(return_value=MagicMock(deleted_count=1))
        response = delete_teacher(self.mock_collection, 'jane.smith@example.com')
        self.assertEqual(response[0], {"message": "Teacher deleted"})
        self.assertEqual(response[1], 200)

    def test_delete_teacher_not_found(self):
        self.mock_collection.delete_one = MagicMock(return_value=MagicMock(deleted_count=0))
        response = delete_teacher(self.mock_collection, 'jane.smith@example.com')
        self.assertEqual(response[0], {"message": "Teacher not found"})
        self.assertEqual(response[1], 404)

    def test_get_all_teachers(self):
        documents = [
            {'_id': 'jane.smith@example.com', 'FirstName': 'Jane', 'LastName': 'Smith', 'Email': 'jane.smith@example.com', 'Password': 'securepassword'}
        ]
        cursor = MagicMock()
        cursor.__iter__.return_value = iter(documents)
        self.mock_collection.find = MagicMock(return_value=cursor)
        response = get_all_teachers(self.mock_collection)
        self.assertEqual(response[0], {"message": [{'FirstName': 'Jane', 'LastName': 'Smith', 'Email': 'jane.smith@example.com', 'Password': 'securepassword'}]})
        self.assertEqual(response[1], 200)

if __name__ == '__main__':
    unittest.main()
