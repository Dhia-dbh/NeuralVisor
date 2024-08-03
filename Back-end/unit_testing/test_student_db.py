import unittest
from unittest.mock import MagicMock
from pymongo import errors
from CRUD_OP.student_db import add_student, update_student, delete_student, get_all_students

class TestStudentDB(unittest.TestCase):
    def setUp(self):
        self.mock_collection = MagicMock()

    def test_add_student_success(self):
        data = {
            'FirstName': 'John',
            'LastName': 'Doe',
            'Email': 'john.doe@example.com',
            'Password': 'securepassword'
        }
        self.mock_collection.insert_one = MagicMock()
        response = add_student(self.mock_collection, data)
        self.assertEqual(response[0], {"message": "Student Added"})
        self.assertEqual(response[1], 200)

    def test_add_student_duplicate(self):
        data = {
            'FirstName': 'John',
            'LastName': 'Doe',
            'Email': 'john.doe@example.com',
            'Password': 'securepassword'
        }
        self.mock_collection.insert_one = MagicMock(side_effect=errors.DuplicateKeyError("Duplicate key error"))
        response = add_student(self.mock_collection, data)
        self.assertEqual(response[0], {"message": "A Student with this email already exists."})
        self.assertEqual(response[1], 400)

    def test_update_student_success(self):
        data = {
            'FirstName': 'John',
            'LastName': 'Doe',
            'Email': 'john.doe@example.com',
            'Password': 'newpassword'
        }
        self.mock_collection.update_one = MagicMock(return_value=MagicMock(matched_count=1))
        response = update_student(self.mock_collection, data)
        self.assertEqual(response[0], {"message": "Student Updated"})
        self.assertEqual(response[1], 200)

    def test_update_student_not_found(self):
        data = {
            'FirstName': 'John',
            'LastName': 'Doe',
            'Email': 'john.doe@example.com',
            'Password': 'newpassword'
        }
        self.mock_collection.update_one = MagicMock(return_value=MagicMock(matched_count=0))
        response = update_student(self.mock_collection, data)
        self.assertEqual(response[0], {"message": "No student found with the given email"})
        self.assertEqual(response[1], 404)

    def test_delete_student_success(self):
        self.mock_collection.delete_one = MagicMock(return_value=MagicMock(deleted_count=1))
        response = delete_student(self.mock_collection, 'john.doe@example.com')
        self.assertEqual(response[0], {"message": "Student deleted"})
        self.assertEqual(response[1], 200)

    def test_delete_student_not_found(self):
        self.mock_collection.delete_one = MagicMock(return_value=MagicMock(deleted_count=0))
        response = delete_student(self.mock_collection, 'john.doe@example.com')
        self.assertEqual(response[0], {"message": "Student not found"})
        self.assertEqual(response[1], 404)

    def test_get_all_students(self):
        documents = [
            {'_id': 'john.doe@example.com', 'FirstName': 'John', 'LastName': 'Doe', 'Email': 'john.doe@example.com', 'Password': 'securepassword'}
        ]
        cursor = MagicMock()
        cursor.__iter__.return_value = iter(documents)
        self.mock_collection.find = MagicMock(return_value=cursor)
        response = get_all_students(self.mock_collection)
        self.assertEqual(response[0], {"message": [{'FirstName': 'John', 'LastName': 'Doe', 'Email': 'john.doe@example.com', 'Password': 'securepassword'}]})
        self.assertEqual(response[1], 200)

if __name__ == '__main__':
    unittest.main()
