import nmap
import sys

def nmap_scanner(x):
    x = str(x)
    nm_scan = nmap.PortScanner()
    nm_scanner = nm_scan.scan(hosts=x, ports=None, arguments='-sC -sV -O')
    print("Host is: "+nm_scanner["scan"][x]['status']['state'])
    print("Address: "+nm_scanner["scan"][x]['addresses']['ipv4']['vendor'])
    
