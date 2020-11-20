import json
import requests
import logging
import asyncio

from stores.base import Store

logger = logging.getLogger(__name__)

PS5_PRODUCT_ID = 14962185
BASE_URL = (
    "https://bestbuy.ca/ecomm-api/availability/products",
    "?accept=application%2Fvnd.bestbuy.standardproduct.v1",
    f"%2Bjson&accept-language=en-CA&skus={PS5_PRODUCT_ID}",
)


class BestBuy(Store):
    def check(self) -> bool:
        self.found = False
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                " (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
            )
        }
        response = requests.get(BASE_URL, headers=headers, timeout=10)
        try:
            response.raise_for_status()
            raw_response = response.content.decode("utf-8")
            json_response = raw_response.replace("\ufeff", "")
            json_response = json_response.replace("\r\n", "")
            self.parse_payload(json.loads(json_response))
        except Exception as e:
            logger.error(e)
        print(f"Checked bestbuy.  Purchasable: {self.found}")

    def parse_payload(self, raw_json: dict) -> None:
        availabilities = raw_json.get("availabilities")
        for availability in availabilities:
            shipping_availability = availability.get("shipping")
            purchasable = shipping_availability.get("purchaseable")
            if purchasable:
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                loop.run_until_complete(
                    self.stock_alert(
                        provider="Bestbuy",
                        link=(
                            "https://www.bestbuy.ca/en-ca/product/",
                            f"{PS5_PRODUCT_ID}",
                        ),
                    )
                )
                self.found = True
