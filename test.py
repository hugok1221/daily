import nmap
from pnmap import scan

x = '127.0.0.1'
nm = scan(x)
print("\n[+] Host : "+nm['scan'][x]['status']['state'])
print("\n[+] Address :"+nm['scan'][x]['addresses']['ipv4'])
print("\n[+] Vendor :",nm['scan'][x]['vendor'])
print("\n[+] port :",nm['scan'][x]['tcp'])
