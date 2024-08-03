from pymongo import errors

def add_student(student_collection, data):
    if not data:
        return {"message": "No data provided"}, 400

    first_name = data.get('FirstName')
    last_name = data.get('LastName')
    email = data.get('Email')
    password = data.get('Password')

    if not all([first_name, last_name, email, password]):
        return {"message": "Missing data"}, 400

    document = {
        "_id": email,
        "FirstName": first_name,
        "LastName": last_name,
        "Email": email,
        "Password": password
    }

    try:
        student_collection.insert_one(document)
        return {"message": "Student Added"}, 200
    except errors.DuplicateKeyError:
        return {"message": "A Student with this email already exists."}, 400
    except errors.PyMongoError as e:
        return {"message": str(e)}, 500

def update_student(student_collection, data):
    if not data:
        return {"message": "No data provided"}, 400

    first_name = data.get('FirstName')
    last_name = data.get('LastName')
    email = data.get('Email')
    password = data.get('Password')

    if not email:
        return {"message": "Email is required"}, 400

    document = {
        "FirstName": first_name,
        "LastName": last_name,
        "Email": email,
        "Password": password
    }

    try:
        update_result = student_collection.update_one({"_id": email}, {"$set": document})
        if update_result.matched_count == 0:
            return {"message": "No student found with the given email"}, 404
        return {"message": "Student Updated"}, 200
    except errors.PyMongoError as e:
        return {"message": str(e)}, 500

def delete_student(student_collection, email):
    if not email:
        return {"message": "Email is required"}, 400

    try:
        result = student_collection.delete_one({"_id": email})
        if result.deleted_count > 0:
            return {"message": "Student deleted"}, 200
        return {"message": "Student not found"}, 404
    except errors.PyMongoError as e:
        return {"message": str(e)}, 500

def get_all_students(student_collection):
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
        return {"message": students_list}, 200
    except errors.PyMongoError as e:
        return {"message": str(e)}, 500