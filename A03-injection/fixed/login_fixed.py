#Applying measures to fix the login.py in vulnerable 


import sqlite3

db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE users(user TEXT , pass TEXT, role TEXT)")
db.execute("INSERT INTO users VALUES('Emma', 'sunshine', 'user')")
db.execute("INSERT INTO users VALUES('admin', 'sup3rsecret', 'admin')")
db.commit()

def login(username, password):
    # Applying fixes here by removing cancentated strings and replacing it with placeholder; this is called Query parameterization.. 
    # simplying replacing username and password variable with ? 
    q = "SELECT user, role FROM users WHERE user = ? AND pass = ?"
    return db.execute(q, (username, password)).fetchall() 

if __name__ == "__main__":
    print("Legit login:", login("Emma", "sunshine"))

    # Attack 1: skip the password check entirely
    print("SQLi 1 (admin' --):", login("admin' --", "wrong-password"))

    # Attack 2: log in as EVERYONE without any credentials
    print("SQLi 2 (OR 1=1):", login("' OR '1'='1' --", "x"))

    # Attack 3: steal the whole table, passwords included
    print("SQLi 3 (UNION leak):", login("' UNION SELECT user, pass FROM users --", "x"))
    
    