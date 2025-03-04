from flask import Flask, request, jsonify
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="qwerty",
    database="password_manager"
)


@app.route('/store', methods=['POST'])
def store_password():
    data = request.json
    username = data.get('username')
    website = data.get('website')
    password = data.get('password')

    if not (username and website and password):
        return jsonify({"error": "Missing fields"}), 400

    cursor = db.cursor()
    cursor.execute("INSERT INTO credentials (username, website, password) VALUES (%s, %s, %s)",
                   (username, website, password))
    db.commit()
    cursor.close()
    return jsonify({"message": "Password stored successfully"})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
