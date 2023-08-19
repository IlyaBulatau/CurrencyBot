import os


class Settings:

    def __init__(self):
        self._token: str = os.environ.get("BOT_TOKEN")


    @property
    def token(self):
        return self._token
    
