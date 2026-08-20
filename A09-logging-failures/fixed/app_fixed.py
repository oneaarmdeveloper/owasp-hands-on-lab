import json, logging, time
from collections import defaultdict, deque
from flask import Flask, request, jsonify

app = Flask(__name__)
USERS = {"Emma": "secret"}
TOKENS = {"good-token-123": "Emma"}

# FIX 1: persistent, structured security log FILE
log = logging.getLogger("security")
log.setLevel(logging.INFO)
log.addHandler(logging.FileHandler("security.log"))

def sec(event, **fields):
    log.info(json.dumps({"ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                         "event": event, "ip": request.remote_addr, **fields}))

FAILS = defaultdict(deque)

@app.route("/login", methods=["POST"])
def login():
    u = request.json.get("user", "")
    if USERS.get(u) == request.json.get("pass", ""):
        sec("login_success", user=u)
        return jsonify(token="ok")

    sec("login_failed", user=u)                    # FIX 2: every failure recorded
    q = FAILS[request.remote_addr]
    q.append(time.time())
    while q and time.time() - q[0] > 60:
        q.popleft()
    if len(q) >= 5:
        sec("ALERT_brute_force", attempts=len(q))  # FIX 3: detection, not just logging
    return jsonify(error="bad credentials"), 401

@app.route("/export-all-records")
def export():
    tok = request.headers.get("Authorization", "")
    if tok not in TOKENS:                          # FIX 4: auth + audit on sensitive data
        sec("export_denied")
        return jsonify(error="forbidden"), 403
    sec("export_allowed", user=TOKENS[tok])
    return jsonify(records=["..50,000 patient records ..."])

if __name__ == "__main__":
    app.run(port=5006, debug=False)
    