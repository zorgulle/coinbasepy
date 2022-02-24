from flask import redirect

class Connector:
    """Interact with the API
    """
    def __init__(self, client_id: str, redirect_uri: str):
        super(Connector, self).__init__()
        self.client_id = client_id
        self.redirect_uri = redirect_uri

    def authorize(self):
        #GET https://www.coinbase.com/oauth/authorize?response_type=code&client_id=YOUR_CLIENT_ID&redirect_uri=YOUR_REDIRECT_URL&state=SECURE_RANDOM&scope=wallet:accounts:read
        #Need to redirect to this url
        params = {
            "response_type": "code",
            "client_id": self.client_id,
            "redirect_uri": self.redirect_uri,
            "state": state
        }
        return redirect("http://google.com")
    