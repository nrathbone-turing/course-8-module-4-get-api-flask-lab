from flask import Flask, jsonify, request
from data import products

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Product Catalog API!"})

# TODO: Implement GET /products route that returns all products or filters by category

# GET /products (with ability to filter by category)
@app.route("/products", methods=["GET"])
def get_products():
    category = request.args.get("category")  # example - ?category=books
    if category:
        filtered = [p for p in products if p.get("category") == category]
        return jsonify(filtered)
    return jsonify(products)

# TODO: Implement GET /products/<id> route that returns a specific product by ID or 404

@app.route("/products/<int:id>")
def get_product_by_id(id):
    pass  # TODO: Return product by ID or 404

if __name__ == "__main__":
    app.run(debug=True)
