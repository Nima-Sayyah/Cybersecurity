import subprocess
import string
import random
import re

def get_random_mac_address():
"""Generate and return a MAC address in the format of Linux"""
    # get the hexdigits uppercased
    uppercased_hexdigits = ''.join(set(string.hexdigits.upper()))
    # 2nd character must be 0, 2, 4, 6, 8, A, C, or E
    mac = ""
    for i in range(6):
        for j in range(2):
            if i == 0:
                mac += random.choice("02468ACE")
            else:
                mac += random.choice(uppercased_hexdigits)
        mac += ":"
    return mac.strip(":")

def get_current_mac_address(iface):
    # use the ifconfig command to get the interface details, including the MAC address
    output = subprocess.check_output(f"ifconfig {iface}", shell=True).decode()
    return re.search("ether (.+) ", output).group().split()[1].strip()
