from scapy.all import *

#send(IP(dst="10.0.0.1")/ICMP()/"HelloWorld")

#send(IP(src="10.1.99.100", dst="10.0.0.1")/ICMP()/"HelloWorld")

#send(IP(src="10.1.99.100", dst="10.0.0.1", ttl=128)/ICMP(type=0)/"HelloWorld")

#h=sr1(IP(dst="10.0.0.1")/ICMP())
#h.show()

#h=sr1(IP(dst="10.0.0.1")/ICMP()/"HelloWorld")
#h.show()

#p=sr(IP(dst="10.0.0.1")/TCP(dport=22))
#p #(this only works using Scapy directly )
#p.show() #(this only works using Scapy directly )
#ans,unans=_ #(this only works using Scapy directly )
#ans.summary() #(this only works using Scapy directly )


#p=sr(IP(dst="10.0.0.1")/TCP(dport=[23,80,53]))
#p 
#ans,unans=_
#ans.summary()


#p=sr(IP(dst="192.168.1.254")/TCP(sport=666,dport=[22,80,21,443], flags="S"))


#p=sr(IP(dst="192.168.1.254")/TCP(sport=888,dport=[21,22,80,443], flags="A"))


#p=sr(IP(src="10.1.99.100", dst="192.168.1.254")/TCP(sport=RandShort(), dport=[20,21,80,3389]),inter=0.5,retry=2,timeout=1)

#p=sr1(IP(dst="192.168.1.254")/UDP()/DNS(rd=1,qd=DNSQR(qname="www.citrix.com")))