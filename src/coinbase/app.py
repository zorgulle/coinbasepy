from flask_api import FlaskAPI

from coinbase.connector import Connector

app = FlaskAPI(__name__)
app.config.from_object("src.coinbase.config.Dev")

connector = Connector(client_id=app.config["CLIENT_ID"], redirect_uri=app.config["REDIRECT_URI"], scope=app.config["SCOPE"])

@app.route("/authorize", methods=["GET"])
def index():
    return connector.authorize()

def main():
    app.run('0.0.0.0', debug=True)

if __name__ == "__main__":
    main()
