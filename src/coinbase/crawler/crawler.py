import os
import json

from src.coinbase.models.account import Account


class MockHttpHandler:
    def __init__(self, mock_data_path):
        self.path = mock_data_path

    def get_accounts(self):
        with open(os.path.join(self.path, "accounts.json")) as f:
            return json.load(f)


class Crawler:
    def __init__(self, http_handler):
        self.http_handler = http_handler

    def get_accounts(self):
        coinbase_accounts = self.http_handler.get_accounts()
        accounts = []
        for coinbase_account in coinbase_accounts.get("data", []):
            account = Account()
            account.id = coinbase_account["id"]
            accounts.append(account)
        return accounts
