from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS so frontend can call the API

# In-memory account state
account = {
    "balance": 1000.0
}

@app.route('/')
def home():
    return "MCIT Backend Bank is Live"

@app.route('/balance', methods=['GET'])
def get_balance():
    return jsonify({"balance": account["balance"]})

@app.route('/deposit', methods=['POST'])
def deposit():
    data = request.get_json()
    amount = data.get("amount", 0)
    if amount <= 0:
        return jsonify({"error": "Invalid deposit amount"}), 400
    account["balance"] += amount
    return jsonify({"message": "Deposit successful", "balance": account["balance"]})

@app.route('/withdraw', methods=['POST'])
def withdraw():
    data = request.get_json()
    amount = data.get("amount", 0)
    if amount <= 0:
        return jsonify({"error": "Invalid withdrawal amount"}), 400
    if amount > account["balance"]:
        return jsonify({"error": "Insufficient funds"}), 400
    account["balance"] -= amount
    return jsonify({"message": "Withdrawal successful", "balance": account["balance"]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
