# TASK 1.2
from scapy.all import *

a = IP()
a.dst = '10.9.0.6'
a.src = '10.0.5.4'
b = ICMP()
pkt = a/b 
send(pkt) 