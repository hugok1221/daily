import nmap

def scan(x):
    x = str(x)
    nm_scan = nmap.PortScanner()
    nm_scanner = nm_scan.scan(hosts=x, ports=None, arguments='-sC -sV -O')  #ports=None = for port 1-65535
    print("Host is: "+nm_scanner["scan"][x]['status']['state'])
    print("Address: "+nm_scanner["scan"][x]['addresses']['ipv4'])
    
