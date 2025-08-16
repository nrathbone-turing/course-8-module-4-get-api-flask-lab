from flask import Flask, jsonify, request
from data import products

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Product Catalog API!"})

# GET /products (with ability to filter by category)
@app.route("/products", methods=["GET"])
def get_products():
    category = request.args.get("category")  # example - ?category=books
    if category:
        filtered = [p for p in products if p.get("category") == category]
        return jsonify(filtered)
    return jsonify(products)

# GET /products/<id>
@app.route("/products/<int:id>", methods=["GET"])
def get_product_by_id(id):
    for product in products:
        if product.get("id") == id:
            return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
