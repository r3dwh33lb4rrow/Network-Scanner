#### NOTES ####
# Standard TCP ports: 1024 
# All TCP ports: 65535
# All UDP ports: 65535

#socket.SOCK_STREAM = TCP
#socket.SOCK_DGRAM = UDP

#socket.AF_INET = IPV4
#AF_INET6 = IPV6

#### NOTES ####

import socket

# Create function to determine if a port is open
def port_check(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
        print("[-] Open port found on: ", port)
        open_ports.append(port)
        # Port is open
        return True
    except socket.error:
        # Port is not open
        return False
    finally:
        s.close()

# Set host to scan
host = input("Enter an IPV4 address to scan: ")

open_ports = []

# Check each port
for port in range (83):
    port_check(host, port)

# Print out all ports found
if not open_ports:
    print("[-] No ports found :(")
else:
    print(open_ports)
