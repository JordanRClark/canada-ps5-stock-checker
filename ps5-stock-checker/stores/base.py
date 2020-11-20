import time
import logging

from settings import SLEEP
from alerts import send_alert

logger = logging.getLogger(__name__)

class NotImplementedError(Exception):
    pass

class Store:
    '''
    Base class for store checkers.
    Subclass this class into stores
    '''
    def check(self) -> None:
        raise NotImplementedError('Subclass this class with a specific store')

    def run(self) -> None:
        self.found = False
        while not self.found:
            try:
                self.check()
            except Exception as e:
                logger.error(e)
            time.sleep(SLEEP)

    async def stock_alert(self, provider: str=None, link: str=None) -> None:
        await send_alert(provider, link)
