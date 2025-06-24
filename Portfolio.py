from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Yokie.@05",
    database='portfolio'
)
cursor = conn.cursor()

@app.route("/api/contact", methods=["POST"])
def save_messasge():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    message = data.get("message")

    if not name or not email or not message:
        return jsonify({"error": "All fields are required"}), 400
    
    query= "INSERT INTO messages (name, email, message) VALUES (%s, %s, %s) "
    values = (name, email, message)
    cursor.execute(query, values)
    conn.commit()

    return jsonify({"success": True, "message": "Message Saved Successfully!"}), 200

if __name__ == "__main__":
    app.run(debug=True) 