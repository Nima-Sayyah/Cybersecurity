# pip3 install colorama
# set up an FTP server in local network on a machine that runs on Linux

import ftplib
from colorama import Fore, init # for fancy colors, nothing else

# hostname or IP address of the FTP server
host = "192.168.1.113"
# username of the FTP server, root as default for linux
user = "test"
# port of FTP, aka 21
port = 21
