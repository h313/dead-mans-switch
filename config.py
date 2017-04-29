# All the config files go here. Modify them!


class Config:
    # no email sent if set to True
    testing = True
    # URL of the server (keep the http!)
    url = "http://127.0.0.1:5000"
    # a password to be used
    secret_key = "keyboard catt"

    # email stuff
    server = 'mail.your-domain.com'
    port = 25
    sender = 'from@fromdomain.com'
    receivers = ['to@todomain.com', 'to@todomain.com']
    subject = 'dead mans switch'
