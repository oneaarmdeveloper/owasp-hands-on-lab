#fix for store.py by adding salt to the hash to increase security 
from argon2 import PasswordHasher

ph = PasswordHasher() 

def hash_password(pw: str) -> str:
    return ph.hash(pw)

def verify(stored_hash: str, pw: str) -> bool:
    try:
        return ph.verify(stored_hash, pw)
    
    except Exception:
        return False
    

if __name__ == "__main__":
    h1 = hash_password("sunshine")
    h2 = hash_password("sunshine")
    
    print("Same password, different hash:", h1 != h2)
    print("correct password verifies:", verify(h1, "sunshine"))
    print("Wrong password rejected: ", verify(h1, "Wrong123"))
    
    