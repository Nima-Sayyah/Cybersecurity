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

# Try the default credentials on a given instance of DVWA, simulating a real user trying the credentials
# visits the login.php page to get the CSRF token, and tries to login with admin:password
def has_valid_credentials(instance):
    sess = requests.Session()
    proto = ('ssl' in instance) and 'https' or 'http'
    try:
        res = sess.get(f"{proto}://{instance['ip_str']}:{instance['port']}/login.php", verify=False)
    except requests.exceptions.ConnectionError:
        return False
