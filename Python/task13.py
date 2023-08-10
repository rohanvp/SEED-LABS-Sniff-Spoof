# TASK 1.3

from scapy.all import *

ans, unans = sr(IP(dst='10.9.0.5', ttl=(4,25),id=RandShort())/TCP(flags=0x2))

for snd,rcv in ans:
    print(snd.ttl, rcv.src, isinstance(rcv.payload, TCP))