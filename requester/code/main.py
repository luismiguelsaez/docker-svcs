import requests
from time import sleep
import logging
from sys import stdout
from os import environ

def setup_logging(name="main"):

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler(stdout)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger

def main():

    logger = setup_logging()

    if "REQ_ENDPOINT" not in environ:
        REQ_ENDPOINT = "https://ifconfig.co/ip"
    else:
        REQ_ENDPOINT = environ["REQ_ENDPOINT"]

    while True:
        res = requests.get(REQ_ENDPOINT)
        if res.status_code == 200:
            logger.info("Request successful with HTTP code " + str(res.status_code) + ": " + res.text.strip() )
        else:
            logger.error("Request error with HTTP code " + str(res.status_code) + ": " + res.text.strip() )
        sleep(2)

if __name__ == "__main__":
    main()
