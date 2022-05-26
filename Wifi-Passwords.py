import subprocess
import os
import re
from collections import namedtuple
import configparser

def get_linux_saved_wifi_passwords(verbose=1):
    """Extracts saved Wi-Fi passwords saved in a Linux machine, this function extracts data in the
    `/etc/NetworkManager/system-connections/` directory
    Args:
        verbose (int, optional): whether to print saved profiles real-time. Defaults to 1.
    Returns:
        [list]: list of extracted profiles, a profile has the fields ["ssid", "auth-alg", "key-mgmt", "psk"]
    """
    network_connections_path = "/etc/NetworkManager/system-connections/"
    fields = ["ssid", "auth-alg", "key-mgmt", "psk"]
    Profile = namedtuple("Profile", [f.replace("-", "_") for f in fields])
    profiles = []
    for file in os.listdir(network_connections_path):
        data = { k.replace("-", "_"): None for k in fields }
        config = configparser.ConfigParser()
        config.read(os.path.join(network_connections_path, file))
        for _, section in config.items():
            for k, v in section.items():
                if k in fields:
                    data[k.replace("-", "_")] = v
        profile = Profile(**data)
        if verbose >= 1:
            print_linux_profile(profile)
