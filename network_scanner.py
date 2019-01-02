#!/usr/bin/env python
# ARP requests and responses in specified IP range
import scapy.all as scapy

def scan(ip):
	scapy.arping(ip)

scan("172.20.10.1/24")