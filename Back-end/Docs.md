# NeuralVisor Back-end Documentation

This module provides a Flask application with routes for student and teacher management,
authentication,and real-time communication using Socket.IO with Ai integration.

## Installation

python version 3.10.14 is recomended for this project

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required libaries.

The project already containes the requirments.txt file wich containes the nessasary libaries with the required version

```bash
pip install -r requirements.txt
```

## Routes

- `/`: Home route
- `/addStudent`: Add a new student
- `/addTeacher`: Add a new teacher
- `/UpdateStudent`: Update an existing student
- `/UpdateTeacher`: Update an existing teacher
- `/DeleteStudent`: Delete a student
- `/DeleteTeacher`: Delete a teacher
- `/AllStudents`: Retrieve all students
- `/AllTeachers`: Retrieve all teachers
- `/login_Demo`: Demo login route
- `/login`: Login route
- `/protected`: Protected route

## Socket.IO Events

- `screenshot`: Handle screenshot event

### Connection URI

The application connects to MongoDB using the following URI: `mongodb+srv://achebbi2002
@cluster0.dkot1pb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0`

- **URI Explanation:**
  - `mongodb+srv://` specifies the use of a MongoDB Atlas connection.
  - `achebbi2002` is the username.
  - `N8vlNANPaejPYiRI` is the password.
  - `cluster0.dkot1pb.mongodb.net` is the cluster endpoint.
  - `retryWrites=true` ensures that write operations are retried on network errors.
  - `w=majority` specifies write concern level.

### Collections

The application uses the following MongoDB collections:

1. **Student Collection**
   - **Name:** `Student`
   - **Purpose:** Stores student information.
   - **Document Structure:**
     ```json
     {
       "_id": "email@example.com",
       "FirstName": "John",
       "LastName": "Doe",
       "Email": "email@example.com",
       "password": "hashed_password"
     }
     ```
2. **Teacher Collection**
   - **Name:** `Teacher`
   - **Purpose:** Stores teacher information.
   - **Document Structure:**
     ```json
     {
       "_id": "email@example.com",
       "FirstName": "Jane",
       "LastName": "Smith",
       "Email": "email@example.com",
       "password": "hashed_password"
     }
     ```

## Error Handling

The application handles errors using try-except blocks. Common exceptions include:

**DuplicateKeyError**: Raised when attempting to insert a document with a duplicate key.
**PyMongoError**: General exception for errors encountered during MongoDB operations.

## Backup and Restore

**backup**: Regularly back up your MongoDB database using MongoDB’s backup tools or Atlas backup features.

**Restore**: Use MongoDB’s restore tools or Atlas restore features to restore the database from backups.
