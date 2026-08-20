import ipaddress, socket

from urllib.parse import urlparse

import requests

from flask import Flask, request, jsonify

app = Flask (__name__)

ALLOWED_SCHEMES = {"http", "https"}
ALLOWED_HOSTS = {"example.com", "images.example.com"}

def is_safe(url: str) -> bool:
    p = urlparse(url)
    if p.scheme  not in ALLOWED_SCHEMES:
        return False
    if p.hostname not in ALLOWED_HOSTS:
        return False

    try:
        ip = ipaddress.ip_address(socket.gethostbyname(p.hostname))
    except Exception:
        return False

    return not (ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved)

@app.route("/fetch")
def fetch():
    url = request.args.get("url", "")
    if not is_safe(url):
        return jsonify(error="url not allowed"), 400
    r = requests.get(url, timeout=3, allow_redirects=False)
    return jsonify(status= r.status_code, body= r.text[:500])

if __name__ == "__main__":
    app.run(port=5017, debug=True)
