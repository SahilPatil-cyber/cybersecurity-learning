#!/usr/bin/env python3
# port_scanner.py — 2025-09-24
# Educational script — only run on your own lab/VM
# Simple port scanner: checks if specific ports on a host are open or closed

import socket  # Import the socket module to create network connections

# Ask the user to input a host IP address or domain name
host = input("Enter host IP or domain: ")

# List of ports to scan (common ports for learning purposes)
ports = [22, 80, 443]

# Print a message showing which host and ports will be scanned
print(f"Scanning {host} ports {ports} ...")

# Loop through each port in the list
for port in ports:
    s = socket.socket()        # Create a TCP socket
    s.settimeout(0.5)          # Set a timeout of 0.5 seconds for the connection attempt
    try:
        s.connect((host, port))  # Try to connect to the host on the current port
        print(f"[OPEN] Port {port}")  # If connection succeeds, port is open
    except:
        print(f"[CLOSED] Port {port}")  # If connection fails, port is closed
    finally:
        s.close()  # Always close the socket to free resources

# Code Overview
# This script is a simple port scanner in Python. It checks if certain ports on a given host are open or closed. Think of it like trying to “knock” on doors (ports) of a computer to see which ones respond.