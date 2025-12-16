import pytest
import logging
from wallet_utils import map_wallets_by_currency
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from api import BVNKClient

logging.basicConfig(level=logging.INFO)

@pytest.fixture(scope="session")
def api():
    client = BVNKClient()
    client.init()
    return client

@pytest.fixture(scope="session")
def wallets(api):
    return api.list_wallets()

@pytest.fixture(scope="session")
def wallet_map(wallets):
    return map_wallets_by_currency(wallets)
