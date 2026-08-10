#An intentional insecure flask App to learn about Broke Access CAONTROL
# purely for educational purposes

from flask import Flask, jsonify, request

app = Flask(__name__)

ACCOUNTS = {
    1041: {"owner": "Oneaarmdeveloper", "balance": 8200.50},
    1042: {"owner": "Emma", "balance": 100.00},
}

# Assumed logged in session
SESSIONS = {"oneaarmdeveloper-token": "oneaarmdeveloper", "Emma-token": "Emma"}

def current_user():
    token = request.headers.get("Authorization", "")
    return SESSIONS.get(token) 

@app.route("/api/accounts/<int:account_id>/statement")

def statement(account_id):
    user = current_user()
    if not user:
        return jsonify(error="not logged in"), 401 
    
    acct = ACCOUNTS.get(account_id)
    if not acct:
        return jsonify(error="no such Account"), 404
    return jsonify(account=account_id, owner=acct["owner"], balance=acct["balance"])

if __name__ == "__main__":
    app.run(port=5001, debug=True)