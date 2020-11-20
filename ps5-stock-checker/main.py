#!/usr/bin/env python3
import asyncio
import time, threading

import requests

import settings

from stores import az, bb, sdm, wm

def main():
    '''
    Main loop for the program
    We don't want to spam the endpoints are get throttled
    '''
    if settings.CHECK_AMAZON:
        az_thread = threading.Thread(target=az.run)
        az_thread.start()
    if settings.CHECK_BESTBUY:
        bb_thread = threading.Thread(target=bb.run)
        bb_thread.start()
    if settings.CHECK_SHOPPERS:
        sdm_thread = threading.Thread(target=sdm.run)
        sdm_thread.start()
    if settings.CHECK_WALMART:
        wm_thread = threading.Thread(target=wm.run)
        wm_thread.start()


if __name__ == '__main__':
    main()
