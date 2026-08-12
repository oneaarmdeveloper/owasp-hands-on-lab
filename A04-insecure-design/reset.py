# an intentional vulnerable app to reset password 

import random
from flask import Flask, request, jsonify

app = Flask(__name__)

reset_codes = {}

@app.route("/request-reset", methods=["POST"])

def request_reset():
    email = request.json["email"]
    reset_codes[email] = f"{random.randint(0, 9999):04d}"
    print(f"[pretend Email] code for {email} : {reset_codes[email]}")
    return jsonify(ok=True)
    
@app.route("/verify-reset", methods=["POST"])
def verify_reset():
    email = request.json["email"]
    code = request.json["code"]
    #intentonal flaw in design injected under
    if reset_codes.get(email) == code:
        return jsonify(reset_token="NEW PASSWORD Allowed")
    return jsonify(error="bad code"), 400
    
if __name__ == "__main__":
    app.run(port=5006, debug =False)
    