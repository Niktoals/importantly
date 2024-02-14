import scapy.all as scapy
import argparse

# print(scapy.arping('192.168.0.1/24'))

def get_args():
    parser=argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Target IP / IP range")
    options=parser.parse_args()
    return options

def scan(ip):
    arp_req=scapy.ARP(pdst=ip)
    broadcast=scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    pkt=broadcast/arp_req
    answered = scapy.srp(pkt, timeout=1)[0]
    clients_list=[]
    for el in answered:
        client_dict={"IP": el[1].psrc, "MAC":el[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list

def print_results(res_list):
    print('IP\t\t\t\tMAC Adress\n-----------------------------------------------')
    for el in res_list:
        print(el.get("IP") + '\t\t' + el.get("MAC"))
        print('-----------------------------------------------')

# options=get_args()
# scan_result=scan(options.target)
# print_results(scan_result)

