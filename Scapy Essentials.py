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

#p=sr1(IP(dst="192.168.1.254")/UDP()/DNS(rd=1,qd=DNSQR(qname="citrix.com",qtype= "NS")))

#p=traceroute(["www.google.com"], maxttl=20)

#p=traceroute(["192.168.1.254"], maxttl=20)

#p=traceroute (["192.168.1.254"],dport=23,maxttl=20)

#p=traceroute(["192.168.1.254", "www.google.com","www.citrix.com"],maxttl=20)

#ans,unans=sr(IP(dst="192.168.1.254")/TCP(dport=[80,666],flags="A"))

#ans,unans=sr(IP(dst="192.168.1.254",proto=(0,255))/"SCAPY",retry=2)

#p=arping("192.168.1.*")

#ans,unans=sr(IP(dst="192.168.1.1-254")/ICMP())

# error #ans,unans=sr(IP(dst="192.168.1.*")/TCP(dport=80,flags=”S”))

#ans,unans=sr(IP(dst="192.168.1.*"/UDP(dport=0))

#--------------------------------------------

#packet number (0000), frame type (Ether), internet layer (IP), transport layer (TCP), application layer (DNS), packet data (daisy.ubuntu.com)
#sniff()
#a=_
#a.nsummary()

#p=sniff(iface="eth0", filter="icmp", count=10)
#p
#--------------------------------------------
#pkts = rdpcap("/Users/NS/Desktop/read1.pcap")

#--------------------------------------------

#pkts=sniff(iface="eth0",filter="tcp and port 80",count=10)
#wrpcap("/tmp/write1.pcap",pkts)

#--------------------------------------------
#Viewing packets with Wireshark

#packets=Ether()/IP(dst="www.google.com")/ICMP()
#packets ----> <Ether  type=IPv4 |<IP  frag=0 proto=icmp dst=Net("www.google.com/32") |<ICMP  |>>>

#wireshark(packets)

#--------------------------------------------
#pkts=rdpcap(“/tmp/attack.pcap”)

#for pkt in pkts:
    #send(pkt)

#--------------------------------------------

#IP()

#IP()/TCP()

#Ether()/IP()/TCP()

#IP()/TCP()/"GET / HTTP/1.0\r\n\r\n"

#Ether()/IP()/IP()/UDP()

#--------------------------------------------

#a=Ether() 
#b=IP() 
#c=TCP()

#a.show()
#b.show()
#c.show()

#--------------------------------------------

#Fuzzing:

#send(IP(dst=”your_target”)/fuzz(UDP()/NTP(version=4)(loop=1)

#send( Ether(dst=clientMAC)/ARP(op=”who-has”, psrc=gateway, pdst=client). inter=RandNum(10,40), loop=1)

#send( Ether(dst=clientMAC)/Dot1Q(vlan=1)/Dot1Q(vlan=2) /ARP(op="who-has", psrc=gateway, pdst=client), inter=RandNum(10,40), loop=1 )

#arpcachepoison(target, victim, interval=60)


#--------------------------------------------
#VLAN Hopping

#sendp(Ether()/Dot1Q(vlan=2)/Dot1Q(vlan=7)/IP(dst=target)/ICMP())

#import sys
#from scapy.all import sr1,IP,ICMP
#p=sr1(IP(dst=sys.argv[1])/ICMP()) 
#if p:
    #p.show()

#--------------------------------------------

ls()  ---> display all of the available protocols
lsc() ---> display all the Scapy command functions 
ls(protocol)
ls(ARP) 
