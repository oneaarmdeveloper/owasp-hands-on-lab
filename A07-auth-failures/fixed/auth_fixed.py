from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import secrets

app = Flask(__name__)

# FIX 1:
USERS = {
    "Emma": generate_password_hash("password1"),
    "John": generate_password_hash("password2"),
}

SESSIONS = {}
FAILS = {}

@app.route("/login", methods=["POST"])
def login():
    u = request.json.get("user", "")
    p = request.json.get("pass", "")

    # FIX 3: lock the account after 2 failed attempts
    if FAILS.get(u, 0) >= 2:
        return jsonify(error="account locked, try later"), 429

    if u in USERS and check_password_hash(USERS[u], p):
        FAILS[u] = 0

        # FIX : 
        token = secrets.token_hex(16)
        SESSIONS[token] = u
        return jsonify(token=token)

    FAILS[u] = FAILS.get(u, 0) + 1
    return jsonify(error="bad credentials"), 401

if __name__ == "__main__":
    app.run(port=5004, debug=False)

    