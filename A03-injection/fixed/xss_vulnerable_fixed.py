# Applying fix to the XSS_vulnerable.py to protect against XSS Attack

from flask import Flask, request, make_response
from markupsafe import escape


app = Flask(__name__)

@app.route("/")
def index():
    #source of attack from user input
    comment = request.args.get("comment", "")
    
    #Applying fix here through contextual output encoding
    safe_comment = escape(comment)
    
    html = f"""
    
    <h2>leave a comment</h2>
    <form method="GET">
    <input type="text" name="comment" placeholder="Type something.." style="width:300px;">
    <button type="submit">Post</button>
    </form>
    <hr>
    <h3>Latest comment: </h3>
    <div style="border: 1px solid #ccc; padding:100px; background: #f9f9f9;">
    {safe_comment}
    </div>
    """
    
    # Applying fix 2: Defense in depth  with Belt and Suspenders, which tells server to only run script from owners server
    response = make_response(html)
    response.headers["content_securuty_policy"]  = "default-src 'self'"
    return response 

if __name__ == "__main__":
    app.run(port=5005, debug=True) 
    