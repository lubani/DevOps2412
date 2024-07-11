from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Using a dictionary for faster lookups
data = {
    1: {"id": 1, "name": "John"},
    2: {"id": 2, "name": "Jane"},
    3: {"id": 3, "name": "Mary"},
}


# Root URL route
@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Welcome to the API. Use /items to access the items."})


# GET method to retrieve all items
@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(list(data.values()))


# GET method to retrieve a specific item by ID
@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = data.get(item_id)
    if item:
        return jsonify(item)
    return jsonify({"error": "Item not found"}), 404


# DELETE method to delete a specific item by ID
@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    item = data.pop(item_id, None)
    if item:
        logging.info(f"Deleted item: {item}")
        return jsonify({"message": "Item deleted successfully", "item": item})
    logging.warning(f"Item not found: {item_id}")
    return jsonify({"error": "Item not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
