from flask import Flask, request, jsonify

app = Flask(__name__)

USERS = {"Emma": "password1",
         "John": "password2"}

@app.route("/login", methods = ["POST"])
def login():
    u = request.json["user"]
    p = request.json["pass"]

    if USERS.get(u) == p:
        return jsonify(token=f"session-for-{u}")
    return jsonify(error="bad credentials"), 401

if __name__ == "__main__":
    app.run(port=5004, debug= True)