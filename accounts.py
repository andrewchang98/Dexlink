from datetime import datetime

# ACCOUNT CLASS FOR STORING LOGIN INFO
class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.created = datetime.now()
