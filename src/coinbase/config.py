

import dotenv
import dotenv
import os



class Dev:
    SCOPE = "wallet:accounts:read"
    REDIRECT_URI = os.environ.get("REDIRECT_URI")
    CLIENT_ID = os.environ.get("CLIENT_ID")