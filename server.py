from flask import Flask, request, jsonify
from send import send
from datetime import datetime
import atexit
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from config import Config

last_verify = [datetime.now()]


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


@app.route("/verify", methods=['POST'])
def verify():
    data = request.get_json()
    if data["key"] == Config.secret_key:
        last_verify[0] = datetime.now()
        return jsonify({"success": True})
    else:
        print('denied!')
        return jsonify({"success": False})

if __name__ == "__main__":
    app.run()
