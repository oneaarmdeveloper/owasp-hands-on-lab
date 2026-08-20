import requests
from flask import Flask , request, jsonify

app = Flask(__name__)

@app.route("/fetch")
def fetch():
    url = request.args.get("url")
    #limitation
    r = requests.get(url, timeout=3)
    return jsonify(status=r.status_code, body=r.text[:500])

if __name__ == "__main__":
    app.run(port=5007, debug=True)

    