from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import random

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Store the current 4-digit code (initially random)
current_code = str(random.randint(1000, 9999))

@app.route("/get-code", methods=["GET"])
def get_code():
    return jsonify({"code": current_code})

@app.route("/use-code", methods=["POST"])
def use_code():
    global current_code
    data = request.get_json()

    if not data or "code" not in data:
        return jsonify({"error": "Invalid request"}), 400

    if data["code"] == current_code:
        current_code = str(random.randint(1000, 9999))  # Generate a new code
        return jsonify({"success": True, "new_code": current_code})

    return jsonify({"error": "Incorrect code"}), 403

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
