import shodan
import time
import requests
import re

# shodan API key
SHODAN_API_KEY = ''
api = shodan.Shodan(SHODAN_API_KEY)

# requests a page of data from shodan
def request_page_from_shodan(query, page=1):
    while True:
        try:
            instances = api.search(query, page=page)
            return instances

        except shodan.APIError as e:
            print(f"Error: {e}")
            time.sleep(5)
