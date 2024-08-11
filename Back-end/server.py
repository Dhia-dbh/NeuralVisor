import os
import base64
from flask import Flask, jsonify, request, render_template
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_socketio import SocketIO, emit
from CRUD_OP.database import get_database
from CRUD_OP.student_db import add_student, update_student, delete_student, get_all_students
from CRUD_OP.teacher_db import add_teacher, update_teacher, delete_teacher, get_all_teachers
from CRUD_OP.files_db import add_File
from track import track_focus_screenshot
from pymongo import errors
import secrets
app = Flask(__name__)
socketio = SocketIO(app)

app.config['JWT_SECRET_KEY'] = secrets.token_hex(32)
jwt = JWTManager(app)

student_collection, teacher_collection, Files_collection = get_database()

if student_collection is None or teacher_collection is None:
    raise SystemExit("Failed to connect to the database. Check your URI or database server.")

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

@app.route("/addStudent", methods=['POST'])
def add_student_route():
    """Add a new student."""
    data = request.get_json()
    return jsonify(add_student(student_collection, data))

@app.route("/addTeacher", methods=['POST'])
def add_teacher_route():
    """Add a new teacher."""
    data = request.get_json()
    return jsonify(add_teacher(teacher_collection, data))

@app.route("/addFile",methods=["POST"])
def add_file_route():
    """Add a new File."""
    return jsonify(add_File(Files_collection, request))    

@app.route("/UpdateStudent", methods=['POST'])
def update_student_route():
    """Update an existing student."""
    data = request.get_json()
    return jsonify(update_student(student_collection, data))

@app.route("/UpdateTeacher", methods=['POST'])
def update_teacher_route():
    """Update an existing teacher."""
    data = request.get_json()
    return jsonify(update_teacher(teacher_collection, data))

@app.route("/DeleteTeacher", methods=['DELETE'])
def delete_teacher_route():
    """Delete a teacher."""
    data = request.get_json()
    email = data.get('Email')
    return jsonify(delete_teacher(teacher_collection, email))

@app.route("/DeleteStudent", methods=['DELETE'])
def delete_student_route():
    """Delete a student."""
    data = request.get_json()
    email = data.get('Email')
    return jsonify(delete_student(student_collection, email))

@app.route("/AllStudents")
def all_students_route():
    """Retrieve all students."""
    return jsonify(get_all_students(student_collection))

@app.route("/AllTeachers")
def all_teachers_route():
    """Retrieve all teachers."""
    return jsonify(get_all_teachers(teacher_collection))

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
        if password == passworddb:
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
    app.run(debug=True)