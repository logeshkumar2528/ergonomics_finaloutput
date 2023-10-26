from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')  # Change the MongoDB URI as needed
db = client['ergonomics']  # Replace 'your_database_name' with your database name
collection = db['values']  # Replace 'your_collection_name' with your collection name

@app.route('/data', methods=['GET'])
def get_data():
    # Retrieve data from MongoDB
    data = list(collection.find({}, {'_id': 0}))  # Exclude _id field
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
