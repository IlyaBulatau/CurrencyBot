"""
Settings module
"""
import os

        
class BotSettings:

    def __init__(self):
        self._token: str = os.environ.get("BOT_TOKEN")

    @property
    def token(self):
        return self._token
    

class DatabaseSettings:

    def __init__(self):
        self._login = os.environ.get("DB_LOGIN")
        self._password = os.environ.get("DB_PASSWORD")
        self._name = os.environ.get("DB_NAME")
        self._host = os.environ.get("DB_HOST")

    @property
    def login(self):
        return self._login
    
    @property
    def password(self):
        return self._password
    
    @property
    def host(self):
        return self._host
    
    @property
    def name(self):
        return self._name

    @property
    def url(self):
        return f"postgresql+asyncpg://{self._login}:{self._password}@{self._host}/{self._name}"
    
