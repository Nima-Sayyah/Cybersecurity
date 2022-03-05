from scapy.all import *
# import HTTP packet
from scapy.layers.http import HTTPRequest 
from colorama import init, Fore

# initialize colorama
init()

nima=sniff(count=3)
nima