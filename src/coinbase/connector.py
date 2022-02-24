from flask import redirect
from urllib.parse import urlencode, urljoin


class Connector:
    """Interact with the API
    """
    def __init__(self, client_id: str, redirect_uri: str, scope:str):
        super(Connector, self).__init__()
        self.client_id = client_id
        self.redirect_uri = redirect_uri
        self.scope = scope

    def authorize(self):
        #GET https://www.coinbase.com/oauth/authorize?response_type=code&client_id=YOUR_CLIENT_ID&redirect_uri=YOUR_REDIRECT_URL&state=SECURE_RANDOM&scope=wallet:accounts:read
        #Need to redirect to this url
        params = {
            "response_type": "code",
            "client_id": self.client_id,
            "redirect_uri": self.redirect_uri,
            "state": "astate",
            "scope": self.scope
        }

        encoded_params = urlencode(params)

        return redirect(urljoin("https://www.coinbase.com/oauth/authorize?", encoded_params))
    