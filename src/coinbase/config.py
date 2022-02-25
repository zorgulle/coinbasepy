import os
from pickle import TRUE


class Dev:
    SCOPE = "wallet:accounts:read"
    REDIRECT_URI = os.environ.get("REDIRECT_URI")
    CALLBACK_URL = os.environ.get("CALLBACK_URL")

    CLIENT_ID = os.environ.get("CLIENT_ID")
    CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
    DEBUG = TRUE
