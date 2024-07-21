"""
This module provides a Flask application with routes for student and teacher management,
authentication, and real-time communication using Socket.IO.
"""

import os
import base64
from flask import Flask, jsonify, request, render_template
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_socketio import SocketIO, emit
from pymongo import MongoClient, errors
from pymongo.server_api import ServerApi
from track import track_focus_screenshot

app = Flask(__name__)
socketio = SocketIO(app)

app.config['JWT_SECRET_KEY'] = "a3f5e3a4d2f4b5c3e5f2a4b3c5e2f3a4d2b5c3e5a4f3b2c5e3a4d2f4b5c3e5f2"
jwt = JWTManager(app)

def handle_download(data):
    """Handle the downloading of base64-encoded images."""
    img_data = base64.b64decode(data.split(',')[1])
    filename = 'screenshot.png'
    filepath = os.path.join(filename)

    with open(filepath, 'wb') as file:
        file.write(img_data)

    print(f"Saved file: {filepath}")  # Debugging information

@app.route("/")
def home():
    """Home route."""
    return "Welcome to the back-end"

@app.route("/addStudent")
def add_student():
    """Add a new student."""
    try:
        data = request.args
        first_name = data.get('FirstName')
        last_name = data.get('LastName')
        email = data.get('Email')
        password = data.get('Password')
        document = {
            "_id": email, "FirstName": first_name, "LastName": last_name,
            "Email": email, "password": password
        }
        student_collection.insert_one(document)
        return jsonify({"message": "Student Added"}), 200
    except errors.DuplicateKeyError:
        return jsonify({"message": "A Student with this email already exists."}), 400
    except errors.PyMongoError as e:
        print(e)
        return jsonify({"message": str(e)}), 500

@app.route("/addTeacher")
def add_teacher():
    """Add a new teacher."""
    try:
        data = request.args
        first_name = data.get('FirstName')
        last_name = data.get('LastName')
        email = data.get('Email')
        password = data.get('Password')
        document = {
            "_id": email, "FirstName": first_name, "LastName": last_name,
            "Email": email, "password": password
        }
        teacher_collection.insert_one(document)
        return jsonify({"message": "Teacher Added"}), 200
    except errors.DuplicateKeyError:
        return jsonify({"message": "A Teacher with this email already exists."}), 400
    except errors.PyMongoError as e:
        print(e)
        return jsonify({"message": str(e)}), 500

@app.route("/UpdateStudent")
def update_student():
    """Update an existing student."""
    try:
        data = request.args
        first_name = data.get('FirstName')
        last_name = data.get('LastName')
        email = data.get('Email')
        password = data.get('Password')
        if not email:
            return jsonify({"message": "Email is required"}), 400
        document = {
            "FirstName": first_name, "LastName": last_name,
            "Email": email, "password": password
        }
        update_result=student_collection.update_one({"_id": email}, {"$set": document})
        if update_result.matched_count == 0:
            return jsonify({"message": "No student found with the given email"}), 404
        return jsonify({"message": "Student Updated"}), 200
    except errors.PyMongoError as e:
        return jsonify({"message": str(e)}), 500

@app.route("/UpdateTeacher")
def update_teacher():
    """Update an existing teacher."""
    try:
        data = request.args
        first_name = data.get('FirstName')
        last_name = data.get('LastName')
        email = data.get('Email')
        password = data.get('Password')
        if not email:
            return jsonify({"message": "Email is required"}), 400
        document = {
            "FirstName": first_name, "LastName": last_name,
            "Email": email, "password": password
        }
        teacher_collection.update_one({"_id": email}, {"$set": document})
        return jsonify({"message": "Teacher Updated"}), 200
    except errors.PyMongoError as e:
        return jsonify({"message": str(e)}), 500

@app.route("/DeleteTeacher")
def delete_teacher():
    """Delete a teacher."""
    try:
        data = request.args
        email = data.get('Email')
        result = teacher_collection.delete_one({"_id": email})
        if result.deleted_count > 0:
            return jsonify({"message": "Teacher deleted"}), 200
        return jsonify({"message": "Teacher not found"}), 404
    except errors.PyMongoError as e:
        print(e)
        return jsonify({"message": str(e)}), 500

@app.route("/DeleteStudent")
def delete_student():
    """Delete a student."""
    try:
        data = request.args
        email = data.get('Email')
        result = student_collection.delete_one({"_id": email})
        if result.deleted_count > 0:
            return jsonify({"message": "Student deleted"}), 200
        return jsonify({"message": "Student not found"}), 404
    except errors.PyMongoError as e:
        print(e)
        return jsonify({"message": str(e)}), 500

@app.route("/AllStudents")
def all_students():
    """Retrieve all students."""
    try:
        students_list = []
        documents = student_collection.find()
        for document in documents:
            if isinstance(document, dict):
                document.pop('_id')
                students_list.append(document)
            else:
                if hasattr(document, 'to_dict'):
                    students_list.append(document.to_dict())
                else:
                    students_list.append(str(document))
        print(students_list)
        return jsonify({"message": students_list}), 200
    except errors.PyMongoError as e:
        print(e)
        return jsonify({"message": str(e)}), 500

@app.route("/AllTeachers")
def all_teachers():
    """Retrieve all teachers."""
    try:
        teachers_list = []
        documents = teacher_collection.find()
        for document in documents:
            if isinstance(document, dict):
                document.pop('_id')
                teachers_list.append(document)
            else:
                if hasattr(document, 'to_dict'):
                    teachers_list.append(document.to_dict())
                else:
                    teachers_list.append(str(document))
        print(teachers_list)
        return jsonify({"message": teachers_list}), 200
    except errors.PyMongoError as e:
        print(e)
        return jsonify({"message": str(e)}), 500

@app.route('/login_Demo')
def login_demo():
    """Demo login route."""
    try:
        data = request.args
        email = data.get('Email')
        password = data.get('password')
        if not email:
            return jsonify({"msg": "Missing email"}), 400
        if not password:
            return jsonify({"msg": "Missing password"}), 400
        student = student_collection.find_one({"_id": email})
        if not student:
            return jsonify({"message": "No student found with the given email"}), 404
        passworddb = student.get('password')
        if password==passworddb:
            return jsonify({"msg": "Access guaranteed!"}), 200
        return jsonify({"msg": "Denied"}), 401
    except Exception as e:
        return jsonify({"msg": str(e)}), 500

@app.route('/login', methods=['POST'])
def login():
    """Login route."""
    try:
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400

        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({"msg": "Missing email or password"}), 400

        student = student_collection.find_one({'_id': email})

        if student is None:
            return jsonify({"msg": "User not found"}), 404

        if password != student.get("password"):
            return jsonify({"msg": "Bad credentials"}), 401

        access_token = create_access_token(identity=email)
        return jsonify(access_token=access_token)

    except errors.PyMongoError as e:
        return jsonify({"msg": str(e)}), 500

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    """Protected route."""
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

@socketio.on('screenshot')
def handle_screenshot(data):
    """Handle screenshot event."""
    handle_download(data)
    focus_data = track_focus_screenshot()
    emit('update_image', {'data': focus_data}, broadcast=True)

@app.route('/pepe')
def index():
    """Render the index page."""
    return render_template('index.html')

if __name__ == '__main__':
    URI = "mongodb+srv://achebbi2002:N8vlNANPaejPYiRI@cluster0.dkot1pb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    client = MongoClient(URI, server_api=ServerApi('1'))
    db = client.cluster0
    student_collection = db.Student
    teacher_collection = db.Teacher
    app.run(debug=True)
