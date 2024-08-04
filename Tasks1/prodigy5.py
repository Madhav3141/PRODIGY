# Network Packet Analyzer

# Develop a packet sniffer tool that captures and analyzes network packets. Display relevant information such as source and destination IP addresses, protocols, and payload data. Ensure the ethical use of the tool for educational purposes.

from scapy.all import *

# Sniff packets
packets = sniff(count=10)

for packet in packets:
    # Print the summary of each packet
    print(packet.summary())
    
    # Check if the packet has an IP layer
    if IP in packet:
        ip_layer = packet[IP]
        print(f'Source IP: {ip_layer.src}')
        print(f'Destination IP: {ip_layer.dst}')
        print(f'Protocol: {ip_layer.proto}')
        print('\n')

    # Check if the packet has a TCP layer
    if TCP in packet:
        tcp_layer = packet[TCP]
        print(f'TCP Source Port: {tcp_layer.sport}')
        print(f'TCP Destination Port: {tcp_layer.dport}')
        print('\n')

    # Check if the packet has a UDP layer
    if UDP in packet:
        udp_layer = packet[UDP]
        print(f'UDP Source Port: {udp_layer.sport}')
        print(f'UDP Destination Port: {udp_layer.dport}')
        print('\n')

    # Check if the packet has an ICMP layer
    if ICMP in packet:
        icmp_layer = packet[ICMP]
        print(f'ICMP Type: {icmp_layer.type}')
        print(f'ICMP Code: {icmp_layer.code}')
        print('\n')
