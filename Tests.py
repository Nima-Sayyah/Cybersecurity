from itertools import count
from scapy.all import *
# import HTTP packet
from scapy.layers.http import HTTPRequest 


nima = sniff(count=3)
nima