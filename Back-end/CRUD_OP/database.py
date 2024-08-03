from pymongo import MongoClient
from pymongo.server_api import ServerApi
import os

def get_database():
    URI = os.getenv('URI')
    client = MongoClient(URI, server_api=ServerApi('1'))
    db = client.cluster0
    student_collection = db.Student
    teacher_collection = db.Teacher
    return student_collection, teacher_collection