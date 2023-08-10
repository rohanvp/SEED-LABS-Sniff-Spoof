# TASK 1.1

from scapy.all import *

def print_pkt(pkt):
    pkt.show()
pkt = sniff(iface='br-cac777b0fc3e', filter='icmp', prn=print_pkt)