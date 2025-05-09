from scapy.all import sniff, Dot11
import pandas as pd

packet_list = []

def packet_handler(pkt):
    if pkt.haslayer(Dot11):
        packet_info = {
            "mac_src": pkt.addr2,
            "mac_dst": pkt.addr1,
            "signal_strength": pkt.dBm_AntSignal if hasattr(pkt, 'dBm_AntSignal') else -100,
            "pkt_type": pkt.type,
            "pkt_subtype": pkt.subtype
        }
        packet_list.append(packet_info)

def start_sniff():
    sniff(iface="wlan0mon", prn=packet_handler, count=200)
    df = pd.DataFrame(packet_list)
    df.to_csv("wifi6_packets.csv", index=False)