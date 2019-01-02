#!/usr/bin/env python
# ARP requests and responses in specified IP range
import scapy.all as scapy

def scan(ip):
	arp_request = scapy.ARP(pdst=ip) # contains an instance of an ARP Packet with pdst(IPField) set to ip
	arp_request.show() # Shows details of create ARP instance
	# print(arp_request.summary()) # scapy method gives summary of packet created above
	# scapy.ls(scapy.ARP()) # gives options for specified class scapy.ARP()
	broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff') # Creates an ethernet opject instance
	broadcast.show()
	arp_request_broadcast = broadcast/arp_request # Combines broadcast and arp_requet packet using Scapy
	# print(arp_request_broadcast.summary())
	arp_request_broadcast.show()

scan("192.168.1.1/24")