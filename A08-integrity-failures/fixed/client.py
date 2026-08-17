import hashlib
import hmac
import json
import requests

SECRET = "server-signing-secret"
data = json.dumps({"hello": "world"}).encode()
sig = hmac.new(SECRET.encode(), data, hashlib.sha256).hexdigest()

# The < > were removed from the URL below
r = requests.post("http://localhost:5005/load", data=data, headers={"X-Signature": sig})
print("Server response:", r.status_code, r.text)