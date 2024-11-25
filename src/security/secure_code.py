import hashlib
import os

def hash_content(content: str) -> str:
    salt = os.urandom(16)
    return hashlib.sha256(salt + content.encode()).hexdigest()
