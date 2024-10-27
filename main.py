from definitions import NUM_OCTETS
from host import Host
from dicts import ip_classes

ip = "10.24.1.254/17"

h1 = Host(ip)
print(h1.ip_block)


