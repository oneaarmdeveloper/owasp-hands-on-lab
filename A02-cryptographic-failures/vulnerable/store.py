import hashlib

#Insecure, fast , unsalted 
#For educational purposes

def hash_password(pw: str) -> str:
    return hashlib.md5(pw.encode()).hexdigest()

users = {
    "oneaarmdeveloper": hash_password("sunshine"),
    "Emma": hash_password("p@ssword2026"),
}

if __name__ == "__main__":
    for user, h in users.items():
        print(f"{user}: {h}")
        