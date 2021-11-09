import os
from errors.auth_error import ApiKeyError

class AuthService:
    def __init__(self):
        self.api_key = os.environ.get('API_KEY')

    def check_api_key(self, api_key):
        if api_key == self.api_key:
            return True
        raise ApiKeyError()

auth_service = AuthService()