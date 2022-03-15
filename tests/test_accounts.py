import json
from unittest import TestCase

from src.coinbase.models.account import Account, Balance
from src.coinbase.crawler.crawler import Crawler, MockHttpHandler


class TestAccounts(TestCase):
    def setup_class(self):
        with open("tests/data/accounts.json", "r") as f:
            self.accounts = json.load(f)
        http_handler = MockHttpHandler("tests/data/")
        self.crawler = Crawler(http_handler)

    def test_get_accounts(self):
        expected = [
            Account(id="58542935-67b5-56e1-a3f9-42686e07fa40",
                    name="My Vault",
                    primary=False,
                    type="vault",
                    currency="BTC",
                    balance=Balance(amount="4.00000000", currency="BTC"),
                    created_at="2015-01-31T20:49:02Z",
                    updated_at="2015-01-31T20:49:02Z",
                    resource="account",
                    resource_path="/v2/accounts/58542935-67b5-56e1-a3f9-42686e07fa40",
                    ready=True),
            Account(id="2bbf394c-193b-5b2a-9155-3b4732659ede")
        ]
        self.assertListEqual(self.crawler.get_accounts(), expected)



