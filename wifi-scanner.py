from scapy.all import *
from threading import Thread
import pandas
import time
import os

# Initializing the networks dataframe containing all access points nearby
networks = pandas.DataFrame(columns=["BSSID", "SSID", "dBm_Signal", "Channel", "Crypto"])

# Setting the index BSSID (MAC address of the AP)
networks.set_index("BSSID", inplace=True)


def callback(packet):

    if packet.haslayer(Dot11Beacon):

        # Extracting the MAC address of the network
        bssid = packet[Dot11].addr2

        # Getting the name of it
        ssid = packet[Dot11Elt].info.decode()
        try:
            dbm_signal = packet.dBm_AntSignal
        except:
            dbm_signal = "N/A"

        # Extracting network stats
        stats = packet[Dot11Beacon].network_stats()

        # Getting the channel of the AP
        channel = stats.get("channel")

        # Getting the crypto
        crypto = stats.get("crypto")
        networks.loc[bssid] = (ssid, dbm_signal, channel, crypto)


# function to print all
def print_all():
    while True:
        os.system("clear")
        print(networks)
        time.sleep(0.5)



def change_channel():
    ch = 1
    while True:
        os.system(f"iwconfig {interface} channel {ch}")
        # Switching channel from 1 to 14 each 0.5s
        ch = ch % 14 + 1
        time.sleep(0.5)


if __name__ == "__main__":
    # Interface name, check using iwconfig
    interface = "wlan0mon"
    # Starting the thread that prints all the networks
    printer = Thread(target=print_all)
    printer.daemon = True
    printer.start()
    # Starting the channel changer
    channel_changer = Thread(target=change_channel)
    channel_changer.daemon = True
    channel_changer.start()
    # Start sniffing
    sniff(prn=callback, iface=interface)
