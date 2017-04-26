import base64
import os
import requests
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# modify these!
secret_key = "keyboard catt"
password = b"password"
url = "10.244.130.4:135"

salt = os.urandom(16)
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(password))
f = Fernet(key)
token = f.encrypt(str.encode(secret_key))

r = requests.post(url, data={'key': token})
print(r.json())
