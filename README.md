# dead-mans-switch
A dead man's switch which will send out a prerecorded message via email to predetermined people

## Why?
Let's say you know something really important. But people are coming after you because of it. Set up this on a computer somewhere, and keep sending a key to it. If, at some time, the key is no longer sent, this program assumes you're dead and sends out the message. If the process is ended, this program assumes you're dead and sends out the mssage. It's the perfect insurance!

## Setting it up
You'll need Python 3, `pip`, and all the packages in `requirements.txt`.

* Type your message into `text.txt`.
* Rename `wrapper.py` to something innocuous.
* Set the variables at the top of `send.py` according to your email server settings.
* Set your password and key in `server.py` and `deactivator.py`. **Make sure they're the same!**
* Set `url` in `deactivator.py` to the address of your running server.

## Running it
To run it, just call `exec python3 wrapper.py` or whatever you renamed `wrapper.py` to in a console and leave your computer on!