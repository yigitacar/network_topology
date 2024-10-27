from definitions import NUM_OCTETS, OCTET_LENGTH
from dicts import ip_classes
## TODO add boundary checks such as > 255 or < 0
class Host:
    def __init__(self, ip_address):
        self.ip_address = ip_address
        self.ip_dotted_decimal = self.get_ip_address()
        self.ip_octets = self.get_ip_octets()

        self.subnet_mask = self.get_subnet_mask()
        self.subnet_octets = self.get_subnet_octets()
        self.subnet_dotted_decimal = self.get_dotted_decimal()

        self.ip_class = self.get_class()
        self.ip_block = self.generate_ip_block()

    def get_ip_address(self):
        return self.ip_address[0 : self.ip_address.find("/")]
    def get_ip_octets(self):
        return [int(octet) for octet in self.ip_dotted_decimal.split(".")]
    def get_subnet_mask(self):
        return int(self.ip_address[self.ip_address.find("/") + 1 :])
    ## Loop through each octet: For each octet, check if subnet_mask is greater than or equal to 8.
    ## If it is, set the octet to 255 (since 8 bits all set to 1 equals 255), and subtract 8 from subnet_mask.
    ## Otherwise, calculate the partial octet by setting the appropriate number of bits and update subnet_mask
    ## to 0 to break out of further modifications.
    def get_subnet_octets(self):
        subnet_mask = self.subnet_mask
        octets = [0, 0, 0, 0]
        for i in range(NUM_OCTETS):
            if subnet_mask >= OCTET_LENGTH:
                octets[i] = 255
                subnet_mask -= OCTET_LENGTH
            else:
                ## Bitwise calculation: 256 - (1 << (8 - subnet_mask)) calculates the appropriate value
                ## for octets with fewer than 8 bits in the mask.
                octets[i] = (256 - (1 << (OCTET_LENGTH - subnet_mask))) if subnet_mask > 0 else 0
                subnet_mask = 0
        return octets
    def get_dotted_decimal(self):
        return ".".join(map(str, self.subnet_octets))
    def get_class(self):
        for cl, key in ip_classes.items():
            if self.ip_octets[0] <= key['First Octet End']:
                return cl
    def generate_ip_block(self):
        ip_block = {
            "IP Address" : self.ip_address,
            "Dotted Decimal" : self.ip_dotted_decimal,
            "Octets" : self.ip_octets,
            "Class" : self.ip_class,
            "Subnet Mask" : {
                "Decimal" : self.subnet_mask,
                "Dotted Decimal": self.subnet_dotted_decimal,
                "Octets": self.subnet_octets
            }
        }
        return ip_block







