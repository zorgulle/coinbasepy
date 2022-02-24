from flask_api import FlaskAPI

from coinbase.connector import Connector

app = FlaskAPI(__name__)
connector = Connector()

@app.route("/authorize", methods=["GET"])
def index():
    return connector.authorize()

def main():
    app.run('0.0.0.0', debug=True)

if __name__ == "__main__":
    main()
