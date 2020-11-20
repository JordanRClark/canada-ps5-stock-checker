import os
import requests
import logging

from stores.base import Store

logger = logging.getLogger(__name__)

PS5_PRODUCT_ID = 14962185
BASE_URL = f'https://amazon.ca/some/search/term?skus={PS5_PRODUCT_ID}'

class Amazon(Store):
    def check(self) -> bool:
        found = False
        response = requests.get(BASE_URL)
        try:
            response.raise_for_status()
            self.parse_payload(response.json())
        except Exception as e:
            logger.error(e)
        return found

    def parse_payload(raw_json: dict) -> bool:
        found = False
        if found:
            self.stock_alert(provider='Amazon', link='https://amazon.ca/link/to/product')
        return found
