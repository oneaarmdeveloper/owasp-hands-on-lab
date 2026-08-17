import hashlib
import hmac
import json
from flask import Flask, request

app = Flask(__name__)

SECRET = "server-signing-secret"

def sign(data: bytes) -> str:
    return hmac.new(SECRET.encode(), data, hashlib.sha256).hexdigest()

@app.route("/load", methods=["POST"])
def load():
   #applxing fix
   sig = request.headers.get("X-Signature", "")
   if not hmac.compare_digest(sig, sign(request.data)):
       return "invalid signature", 403

   #fix 2
   obj = json.loads(request.data)
   return f"loaded: {obj}"

if __name__ == "__main__":
    app.run(port=5005, debug=False)
