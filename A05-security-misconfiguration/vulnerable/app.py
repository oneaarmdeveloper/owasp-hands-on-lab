from flask import Flask
app= Flask(__name__)

SECRET = "prod-db-password-123456"

@app.route("/")
def home():
    return "Welcome to DataNest"

@app.route("/balance")

def balance():
    #injecting a deliberate crash here to see what debug mofde will show
    x = 1 / 0
    return "never reached"

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)