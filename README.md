**Backend Assignment: REST API Server**


This project aims to create a REST API server with CRUD (Create, Read, Update, Delete) based routes using Python and Flask framework. The API allows users to interact with a MongoDB database to manage a collection of books.

**Installation Instructions**
Clone the repository to your local machine.
Install Python if not already installed.
Install the required dependencies using pip:
pip install flask pymongo

**Usage**
Run the Flask application:
python app.py
Use an API testing tool like Postman to interact with the endpoints:
GET /books: Retrieve all books.
GET /books/<name>: Retrieve a specific book by its name.
POST /books: Add a new book to the database.
PUT /books/<name>: Update an existing book.
DELETE /books/<name>: Delete a book from the database.
**API Documentation**
GET /books: Retrieve all books stored in the database.
GET /books/<name>: Retrieve details of a specific book by its name.
POST /books: Add a new book to the database. Requires a JSON payload with name, img, and summary fields.
PUT /books/<name>: Update an existing book by its name. Requires a JSON payload with the updated book details.
DELETE /books/<name>: Delete a book from the database by its name.
