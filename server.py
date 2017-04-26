from flask import Flask, request, jsonify
from send import send
from datetime import datetime
import atexit
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# modify these!
secret_key = "keyboard catt"
password = b"password"

last_verify = [datetime.now()]
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

def check_verify():
    temp_date = datetime.now() - last_verify[0]
    if temp_date.days < 1:
        print('OK!')
    else:
        send()

scheduler = BackgroundScheduler()
scheduler.start()
scheduler.add_job(
    func=check_verify,
    trigger=IntervalTrigger(hours=24),
    id='verify_job',
    name='Verify that the dead mans switch is still active',
    replace_existing=True)
atexit.register(lambda: scheduler.shutdown())

app = Flask(__name__)


@app.route("/verify")
def verify():
    data = request.get_json()
    if f.decrypt(data["key"]) == secret_key:
        last_verify[0] = datetime.now()
        return jsonify({"success": True})
    else:
        return jsonify({"success": False})

if __name__ == "__main__":
    app.run()
