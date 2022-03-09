from scapy.all import *

#send(IP(dst="10.0.0.1")/ICMP()/"HelloWorld")

#send(IP(src="10.1.99.100", dst="10.0.0.1")/ICMP()/"HelloWorld")

#send(IP(src="10.1.99.100", dst="10.0.0.1", ttl=128)/ICMP(type=0)/"HelloWorld")

#h=sr1(IP(dst="10.0.0.1")/ICMP())
#h.show()

#h=sr1(IP(dst="10.0.0.1")/ICMP()/"HelloWorld")
#h.show()

p=sr(IP(dst="10.0.0.1")/TCP(dport=23))
p