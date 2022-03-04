from scapy.all import *
from scapy.layers.http import HTTPRequest # import HTTP packet
from colorama import init, Fore

nima=sniff(count=20)
nima.summary()