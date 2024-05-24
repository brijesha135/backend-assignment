from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')  # MongoDB connection

# Database and collection
db = client['books']
collection = db['books']

# Sample data
initial_data = [
    {
        "name": "Harry Potter and the Order of the Phoenix",
        "img": "https://bit.ly/2IcnSwz",
        "summary": "Harry Potter and Dumbledore's warning about the return of Lord Voldemort is not heeded by the wizard authorities who, in turn, look to undermine Dumbledore's authority at Hogwarts and discredit Harry."
    },
    {
        "name": "The Lord of the Rings: The Fellowship of the Ring",
        "img": "https://bit.ly/2tC1Lcg",
        "summary": "A young hobbit, Frodo, who has found the One Ring that belongs to the Dark Lord Sauron, begins his journey with eight companions to Mount Doom, the only place where it can be destroyed."
    },
    {
        "name": "Avengers: Endgame",
        "img": "https://bit.ly/2Pzczlb",
        "summary": "Adrift in space with no food or water, Tony Stark sends a message to Pepper Potts as his oxygen supply starts to dwindle. Meanwhile, the remaining Avengers -- Thor, Black Widow, Captain America, and Bruce Banner -- must figure out a way to bring back their vanquished allies for an epic showdown with Thanos -- the evil demigod who decimated the planet and the universe."
    }
]

# Insert initial data to MongoDB
collection.insert_many(initial_data)

# Routes
@app.route('/books', methods=['GET'])
def get_books():
    books = list(collection.find({}, {'_id': 0}))
    return jsonify(books)

@app.route('/books/<name>', methods=['GET'])
def get_book(name):
    book = collection.find_one({'name': name}, {'_id': 0})
    if book:
        return jsonify(book)
    else:
        return jsonify({'error': 'Book not found'}), 404

@app.route('/books', methods=['POST'])
def add_book():
    data = request.json
    if data:
        collection.insert_one(data)
        return jsonify({'message': 'Book added successfully'}), 201
    else:
        return jsonify({'error': 'No data provided'}), 400

@app.route('/books/<name>', methods=['PUT'])
def update_book(name):
    data = request.json
    if data:
        collection.update_one({'name': name}, {'$set': data})
        return jsonify({'message': 'Book updated successfully'})
    else:
        return jsonify({'error': 'No data provided'}), 400

@app.route('/books/<name>', methods=['DELETE'])
def delete_book(name):
    result = collection.delete_one({'name': name})
    if result.deleted_count:
        return jsonify({'message': 'Book deleted successfully'})
    else:
        return jsonify({'error': 'Book not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
