#!/usr/bin/env python
# ARP requests and responses in specified IP range
import scapy.all as scapy

def scan(ip):
	arp_request = scapy.ARP(pdst=ip) # contains an instance of an ARP Packet with pdst(IPField) set to ip

	# arp_request.show() # Shows details of create ARP instance

	# print(arp_request.summary()) # scapy method gives summary of packet created above

	# scapy.ls(scapy.ARP()) # gives options for specified class scapy.ARP()

	broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff') # Creates an ethernet opject instance... default sends packet to broadcast MAC address

	arp_request_broadcast = broadcast/arp_request # Combines broadcast and arp_requet packet using Scapy

	answered_list = scapy.srp(arp_request_broadcast, timeout=1)[0] # scapy send recieve custom method to send the packets, returns two lists (answered_list captures the first with [0]) second would be unanswered requests

	print("-------------------------------------------")
	print("IP\t\t\tMAC ADDRESS")
	print("-------------------------------------------")

	for element in answered_list: # accesses all list elements individually
		print(element[1].psrc + '\t\t' + element[1].hwsrc)


scan("192.168.1.1/24")