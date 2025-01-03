from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample product data
products = [
    {"id": 1, "name": "Product 1", "price": 10.00},
    {"id": 2, "name": "Product 2", "price": 20.00},
    {"id": 3, "name": "Product 3", "price": 30.00}
]

# Cart data (in-memory for simplicity)
cart = []

# Home route
@app.route('/')
def home():
    return "Welcome to the Local Store API!"

# Get all products
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

# Add product to cart
@app.route('/cart', methods=['POST'])
def add_to_cart():
    product_id = request.json.get('product_id')
    product = next((p for p in products if p['id'] == product_id), None)

    if product:
        cart.append(product)
        return jsonify({"message": f"{product['name']} added to cart.", "cart": cart}), 200
    else:
        return jsonify({"error": "Product not found."}), 404

# View cart
@app.route('/cart', methods=['GET'])
def view_cart():
    return jsonify(cart)

# Remove product from cart
@app.route('/cart/<int:product_id>', methods=['DELETE'])
def remove_from_cart(product_id):
    global cart
    cart = [item for item in cart if item['id'] != product_id]
    return jsonify({"message": "Product removed from cart.", "cart": cart})

if __name__ == '__main__':
    app.run(debug=True)
