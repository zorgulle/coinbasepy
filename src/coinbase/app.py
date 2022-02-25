from pickle import TRUE
from flask_api import FlaskAPI
from flask import request
import dotenv

from coinbase.connector import Connector

dotenv.load_dotenv()

app = FlaskAPI(__name__)
app.config.from_object("src.coinbase.config.Dev")

connector = Connector(
    client_id=app.config["CLIENT_ID"],
    redirect_uri=app.config["REDIRECT_URI"],
    scope=app.config["SCOPE"],
    client_secret=app.config["CLIENT_SECRET"],
    callback_url=app.config["CALLBACK_URL"],
)


@app.route("/oauth/authorize", methods=["GET"])
def authorize():
    return connector.authorize()


@app.route("/oauth/token", methods=["GET"])
def token():
    code: str = request.args.get("code", "")
    state = request.args.get("state")
    content, status_code = connector.get_token(code)
    return content, status_code


@app.route("/oauth/callback", methods=["GET"])
def callback():
    return {"msg": "Callback"}


def main():
    import os

    app.run("0.0.0.0", debug=True)


if __name__ == "__main__":
    main()
