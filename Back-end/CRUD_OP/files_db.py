from pymongo import errors


def add_File(Files_collection, request):
    if not request.files:
        return {"message": "No data provided"}, 400

    file = request.files['file']
    if not file:
        return {"message": "Missing file"}, 400

    # Extract file name and content
    file_name = file.filename
    file_content = file.read()

    document = {
        "_id": file_name,
        "file": file_content,
    }

    try:
        Files_collection.insert_one(document)
        return {"message": "File Added"}, 200
    except errors.DuplicateKeyError:
        return {"message": "A file with this name already exists."}, 400
    except errors.PyMongoError as e:
        return {"message": str(e)}, 500