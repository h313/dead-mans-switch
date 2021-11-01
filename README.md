# dead-mans-switch
A dead man's switch which will send out a prerecorded message via email to predetermined people after a time limit if not deactivated

# DON'T ACTUALLY USE THIS FOR REAL STUFF

This was an old hobby project, and I haven't tested the reliability of it. Don't use it for real stuff.

## Why?
Let's say you know something really important. But people are coming after you because of it. Set up this on a computer somewhere, and keep sending a key to it. If, at some time, the key is no longer sent, this program assumes you're dead and sends out the message. If the process is ended, this program assumes you're dead and sends out the message. It's the perfect insurance!

## Setting it up
You'll need Python 3, `pip`, and all the packages in `requirements.txt`.

* Type your message into `text.txt`
* Rename `wrapper.py` to something innocuous.
* Set the variables in `config.py`  like your SMTP server and the address of your dead man's switch
* Set `testing` in `config.py` to `False` if you're actually ready to use it

## Running it
To run it, just call `exec python3 wrapper.py` or whatever you renamed `wrapper.py` to in a console and leave your computer on!
