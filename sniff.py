#
# Amazon Dash Button Sniffer
# Cole Smith
#
# Scans wireless interface for ARP requests
# by specified MAC address and runs the runfile
#
from scapy.all import *
from subprocess import Popen

DASH_MAC_ADDR = "50:f5:da:55:39:90"
WIRELESS_INTERFACE = "wlp3s0"

def arp_display(pkt):
    if pkt[ARP].op == 1: #who-has (request)
        if pkt[ARP].hwsrc == DASH_MAC_ADDR:
            # EXECUTION BLOCK
            print "BUTTON PRESSED"
            Popen(["python", "runfile.py"])
sniff(prn=arp_display, filter="arp", iface=WIRELESS_INTERFACE)
