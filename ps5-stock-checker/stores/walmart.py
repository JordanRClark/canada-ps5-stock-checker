import os
import requests
import logging

from stores.base import Store

logger = logging.getLogger(__name__)

PS5_PRODUCT_ID = 14962185
BASE_URL = f'https://walmart.ca/products/{PS5_PRODUCT_ID}'

class Walmart(Store):
    def check(self) -> bool:
        found = False
        response = requests.get(BASE_URL)
        try:
            response.raise_for_status()
            self.check_payload(response.json())
        except Exception as e:
            logger.error(e)
        return found

    def parse_payload(raw_json: dict) -> bool:
        found = False
        availabilities = raw_json.get('availabilities')
        for availability in availabilities:
            purchasable = availability.get('purchaseable')
            if purchasable:
                self.stockself.stock_alertt(provider='Walmart', link='https://walmart.ca/en-ca/product/{PS5_PRODUCT_ID}')
                # End script?  We don't want to keep sending out alert after alert every SLEEP seconds
                found = True
        return found
