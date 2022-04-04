from scapy.all import ARP, Ether, srp

target_ip = "192.168.1.1/24"
# IP Address for the destination
# create ARP packet
arp = ARP(pdst=target_ip)
# create the Ether broadcast packet
# ff:ff:ff:ff:ff:ff MAC address indicates broadcasting
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
# stack them
packet = ether/arp
result = srp(packet, timeout=3)[0]


clients = []

for sent, received in result:

    clients.append({'ip': received.psrc, 'mac': received.hwsrc})


print("Available devices in the network:")
print("IP" + " "*18+"MAC")


for client in clients:
    print("{:12}    {}".format(client['ip'], client['mac']))
