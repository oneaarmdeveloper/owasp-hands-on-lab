# An intentional vulnerable Flask App to simulate and demonstrate XSS Attacks: cross Scripting Attack

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    #source of attack from user input
    comment = request.args.get("comment", "")
    
    
    html = f"""
    
    <h2>leave a comment</h2>
    <form method="GET">
    <input type="text" name="comment" placeholder="Type something.." style="width:300px;">
    <button type="submit">Post</button>
    </form>
    <hr>
    <h3>Latest comment: </h3>
    <div style="border: 1px solid #ccc; padding:100px; background: #f9f9f9;">{comment}</div>
    """
    
    return html

if __name__ == "__main__":
    app.run(port=5004, debug=True) 
    
    