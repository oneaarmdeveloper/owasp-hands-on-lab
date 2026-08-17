import pickle, base64
from flask import Flask, request

app = Flask(__name__)

@app.route("/load", methods=["POST"])

def load():

    #limitation: using pickle.loads on user-supplied data allows RCE
    blob = base64.b64decode(request.data)
    obj = pickle.loads(blob)
    return f"loaded: {obj}"

if __name__ == "__main__":
    app.run(port=5005, debug=True)