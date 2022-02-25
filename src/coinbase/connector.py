from urllib.error import HTTPError
from flask import redirect
import requests
from urllib.parse import urlencode, urljoin


class Connector:
    """Interact with the API"""

    def __init__(
        self,
        client_id: str,
        redirect_uri: str,
        scope: str,
        client_secret: str,
        callback_url: str,
    ):
        super(Connector, self).__init__()
        self.client_id = client_id
        self.redirect_uri = redirect_uri
        self.scope = scope
        self.client_secret = client_secret
        self.callback_url = callback_url

    def authorize(self):
        params = {
            "response_type": "code",
            "client_id": self.client_id,
            "redirect_uri": self.redirect_uri,
            "state": "astate",
            "scope": self.scope,
        }

        encoded_params = urlencode(params)

        return redirect(
            urljoin("https://www.coinbase.com/oauth/authorize?", encoded_params)
        )

    def get_token(self, code: str):
        payload = {
            "grant_type": "authorization_code",
            "code": code,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "redirect_uri": self.callback_url,
        }
        response = requests.post("https://www.coinbase.com/oauth/token", json=payload)
        return response.json(), response.status_code
