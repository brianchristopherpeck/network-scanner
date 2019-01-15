#!/usr/bin/env python
# ARP requests and responses in specified IP range
import scapy.all as scapy
# Optperse allows options in cli
import optparse

def c_arg():
	parser = optparse.OptionParser()
	parser.add_option("-t", "--target", dest="target", help="Target IP / IP range")
	(options, arguments) = parser.parse_args()
	return options

def scan(ip):
	arp_request = scapy.ARP(pdst=ip) # contains an instance of an ARP Packet with pdst(IPField) set to ip

	# arp_request.show() # Shows details of create ARP instance

	# print(arp_request.summary()) # scapy method gives summary of packet created above

	# scapy.ls(scapy.ARP()) # gives options for specified class scapy.ARP()

	broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff') # Creates an ethernet opject instance... default sends packet to broadcast MAC address

	arp_request_broadcast = broadcast/arp_request # Combines broadcast and arp_requet packet using Scapy

	answered_list = scapy.srp(arp_request_broadcast, timeout=1)[0] # scapy send recieve custom method to send the packets, returns two lists (answered_list captures the first with [0]) second would be unanswered requests

	clients_list = []

	for element in answered_list: # accesses all list elements individually
		client_dict = {"ip": element[1].psrc, "mac":element[1].hwsrc}
		clients_list.append(client_dict)
	return clients_list

def print_result(results_list):
	print("-------------------------------------------")
	print("IP\t\t\tMAC ADDRESS")
	print("-------------------------------------------")
	for client in results_list:
		print(client["ip"] + "\t\t" + client["mac"])

options = c_arg()
scan_result = scan(options.target)
print_result(scan_result)