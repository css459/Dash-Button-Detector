#
# Amazon Dash Button Sniffer
# Cole Smith
#
# Scans wireless interface for ARP requests
# by specified MAC address and runs the execution block
#
from scapy.all import *

DASH_MAC_ADDR = "50:f5:da:55:39:90"
WIRELESS_INTERFACE = "wlp3s0"

def arp_display(pkt):
    if pkt[ARP].op == 1: #who-has (request)
        if pkt[ARP].hwsrc == DASH_MAC_ADDR:
            # EXECUTION BLOCK
            print "BUTTON PRESSED"

sniff(prn=arp_display, filter="arp", iface=WIRELESS_INTERFACE)
