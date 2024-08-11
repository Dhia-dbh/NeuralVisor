from pymongo import MongoClient, errors
from pymongo.server_api import ServerApi
import os

def get_database():
    URI = os.getenv('URI')
    
    try:
        # Attempt to create a client and connect to the database
        client = MongoClient(URI, server_api=ServerApi('1'))
        db = client.cluster0
        student_collection = db.Student
        teacher_collection = db.Teacher
        Files_collection = db.Files
        
        # Return the collections if connection is successful
        return student_collection, teacher_collection ,Files_collection

    except errors.ConnectionError as e:
        # Handle connection-related errors
        print(f"ConnectionError: {str(e)}")
        return None, None

    except errors.ConfigurationError as e:
        # Handle configuration-related errors (e.g., invalid URI)
        print(f"ConfigurationError: {str(e)}")
        return None, None

    except Exception as e:
        # Handle any other exceptions
        print(f"An error occurred: {str(e)}")
        return None, None