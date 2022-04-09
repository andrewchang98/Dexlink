from datetime import datetime

class Account:
    def __init__(self, api_key, secret_key):
        self.api_key = api_key
        self.secret_key = secret_key
        self.time = datetime.now()

    def get_api_key()
