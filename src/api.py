import requests
from logging_utils import log_request_response

class BVNKClient:
    # Update address there if required
    BASE_URL = "https://bvnksimulator.pythonanywhere.com"

    def __init__(self):
        self.session = requests.Session()

    def set_token(self, token):
        self.session.headers["Authorization"] = f"Bearer {token}"

    def init(self):
        r = self.session.get(f"{self.BASE_URL}/init")
        log_request_response(r)
        token = r.json()["access_token"]
        self.set_token(token)
        return token

    def echo(self, payload=None):
        r = self.session.post(f"{self.BASE_URL}/echo", json=payload)
        log_request_response(r)
        return r.json()

    def list_wallets(self):
        r = self.session.get(f"{self.BASE_URL}/api/wallet")
        log_request_response(r)
        return r.json()

    def get_wallet(self, wallet_id):
        r = self.session.get(f"{self.BASE_URL}/api/wallet/{wallet_id}")
        log_request_response(r)
        return r.json()

    def create_quote(self, payload):
        r = self.session.post(f"{self.BASE_URL}/api/v1/quote", json=payload)
        log_request_response(r)
        return r.json()

    def accept_quote(self, uuid):
        r = self.session.put(f"{self.BASE_URL}/api/v1/quote/accept/{uuid}")
        log_request_response(r)
        return r.json()

    def get_quote(self, uuid):
        r = self.session.get(f"{self.BASE_URL}/api/v1/quote/{uuid}")
        log_request_response(r)
        return r.json()
