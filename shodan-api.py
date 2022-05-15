import shodan
import time
import requests
import re

# shodan API key
SHODAN_API_KEY = ''
api = shodan.Shodan(SHODAN_API_KEY)
