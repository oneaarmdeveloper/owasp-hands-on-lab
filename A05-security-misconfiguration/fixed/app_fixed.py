import os
from flask import Flask, jsonify
app = Flask(__name__)

SECRET = os.environ.get("DB_PASSWORD", "set-DB_PASSWORD-env-var")

@app.errorhandler(Exception)
def handle(e):
    app.logger.error(f"internal error: {e}")
    return jsonify(error="internal server error"), 500

@app.after_request
def security_headers(resp):
    resp.headers["X-Content-Type-options"] = "nosniff"
    resp.headers["X-Frame-options"] = "DENY"
    resp.headers["Strict-Transport-Security"] = "max-age=315360000"
    return resp

@app.route("/")
def balance():
    x = 1 / 0
    return "never reached"

if __name__ == "__main__": 
    #setting debug to be False to as measure against security misconfiguration
    app.run(host="127.0.0.1", port= 5013, debug=False)
    