"""Demo 5: an in-memory REST-style CRUD JSON API.

Try with curl while this file is running:
    curl http://127.0.0.1:5000/items
    curl -X POST http://127.0.0.1:5000/items -H "Content-Type: application/json" \
         -d "{\"name\":\"Read\",\"description\":\"Read Flask notes\"}"

The list resets whenever the process restarts. See demos/database_crud.py for
persistent SQLite storage.
"""

from flask import Flask, jsonify, request, url_for


app = Flask(__name__)

INITIAL_ITEMS = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"},
]
items = [item.copy() for item in INITIAL_ITEMS]


def find_item(item_id: int):
    return next((item for item in items if item["id"] == item_id), None)


def json_error(message: str, status: int):
    return jsonify({"error": message, "status": status}), status


@app.get("/")
def home():
    return jsonify({"message": "Welcome to the sample to-do API", "items": url_for("get_items")})


@app.get("/items")
def get_items():
    return jsonify({"items": items, "count": len(items)})


@app.get("/items/<int:item_id>")
def get_item(item_id: int):
    item = find_item(item_id)
    if item is None:
        return json_error("Item not found", 404)
    return jsonify(item)


@app.post("/items")
def create_item():
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return json_error("Send a JSON object with Content-Type application/json", 415)
    name = str(data.get("name", "")).strip()
    description = str(data.get("description", "")).strip()
    if not name:
        return json_error("'name' is required", 400)

    new_item = {
        "id": max((item["id"] for item in items), default=0) + 1,
        "name": name,
        "description": description,
    }
    items.append(new_item)
    response = jsonify(new_item)
    response.status_code = 201
    response.headers["Location"] = url_for("get_item", item_id=new_item["id"])
    return response


@app.put("/items/<int:item_id>")
def update_item(item_id: int):
    item = find_item(item_id)
    if item is None:
        return json_error("Item not found", 404)
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return json_error("A JSON object is required", 415)
    if "name" in data and not str(data["name"]).strip():
        return json_error("'name' cannot be empty", 400)
    item["name"] = str(data.get("name", item["name"])).strip()
    item["description"] = str(data.get("description", item["description"])).strip()
    return jsonify(item)


@app.delete("/items/<int:item_id>")
def delete_item(item_id: int):
    item = find_item(item_id)
    if item is None:
        return json_error("Item not found", 404)
    items.remove(item)
    return "", 204


@app.errorhandler(404)
def api_not_found(error):
    return json_error("Endpoint not found", 404)


if __name__ == "__main__":
    app.run(debug=True)
