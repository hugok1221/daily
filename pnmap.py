import nmap

def scan(x):
    x = str(x)
    nm_scan = nmap.PortScanner()
    nm_scanner = nm_scan.scan(hosts=x, ports=None, arguments='-sC -sV -O')
    return nm_scanner
