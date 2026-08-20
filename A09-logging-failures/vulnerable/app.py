# an intentional vulnerable app to demonstrate vulnerability A09
# purely for educational purposes

from flask import Flask, request, jsonify
app = Flask(__name__)
USERS = {"Emma": "secret"}

@app.route("/login", methods=["POST"])

def login():
    u = request.json["user"]
    p = request.json["pass"]
    if USERS.get(u) == p:
        return jsonify(token="ok")
    #limitation
    return jsonify(error="bad credentials"), 401

@app.route("/export-all-records")

def export():
   return jsonify(records=["..50,000 patient records ..."])

if __name__ == "__main__":
    app.run(port=5006, debug = True)
    