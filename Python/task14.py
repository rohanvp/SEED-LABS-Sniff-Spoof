# TASK 1.4

from scapy.all import *

# REFERENCE FOR SOME SYNTAX: https://www.dasblinkenlichten.com/packet-actions-python-and-scapy/

def process_packet(pkt):
    
    # THIS FUNCTION WILL BE CALLED ONLY WHEN THE RECEIVED PACKET IS AN ICMP PACKET because the filter FIELD in sniff() is set.

    src=pkt[1].src
    dst=pkt[1].dst

    seq=pkt[2].seq
    icmp_id=pkt[2].id

    data=pkt[3].load


    # ECHO REPLY CODE IS 0. THEREFORE WE SEND ICMP PACKET WITH PACKET CODE 0.
    new_pkt=IP(src=dst,dst=src)/ICMP(type=0,seq=seq,id=icmp_id)/Raw(load=data)
    send(new_pkt)


pkt = sniff(iface='br-cac777b0fc3e',prn=process_packet,filter='icmp')

# THE RESULT OF THE EXPERIMENT IS THAT IT WORKS PERFECTLY FOR 1st IP. 
# GETS REPLY FROM OTHER HOST ON THE LAN THAT THE QUERIED HOST IS NOT REACHABLE. 
# GETS DUPLICATE ECHO REPLIES(ONE FROM ATTACKER MACHINE AND ONE FROM ACTUAL EXISTING HOST ON THE INTERNET.)