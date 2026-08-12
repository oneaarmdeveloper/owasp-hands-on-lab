# A04-insecure-design/fixed/app.py
import secrets
import time
from flask import Flask, request, jsonify

app = Flask(__name__)

reset_codes = {}   #
attempts = {}     

CODE_TTL = 300        
MAX_ATTEMPTS = 5      

@app.route("/request-reset", methods=["POST"])
def request_reset():
    email = request.json["email"]
    code = secrets.token_urlsafe(32)          # 256-bit entropy, unguessable
    reset_codes[email] = (code, time.time() + CODE_TTL)
    attempts.pop(email, None)
    print(f"[pretend Email] code for {email} : {code}")
    return jsonify(ok=True)

@app.route("/verify-reset", methods=["POST"])
def verify_reset():
    email = request.json["email"]
    code = request.json["code"]

    if not isinstance(code, str):             
        return jsonify(error="bad code"), 400

    
    if attempts.get(email, 0) >= MAX_ATTEMPTS:
        return jsonify(error="too many attempts, reset locked"), 429

    entry = reset_codes.get(email)

    
    if entry is None or time.time() > entry[1]:
        return jsonify(error="bad code"), 400

    stored_code, _ = entry

    
    if secrets.compare_digest(stored_code, code):
        #use one time
        del reset_codes[email]                
        attempts.pop(email, None)
        return jsonify(reset_token="NEW PASSWORD Allowed")

    attempts[email] = attempts.get(email, 0) + 1
    return jsonify(error="bad code"), 400

if __name__ == "__main__":
    app.run(port=5007, debug=False)