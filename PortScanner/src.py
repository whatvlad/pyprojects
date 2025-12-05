import socket
from datetime import datetime

common_services = {
    20: "ftp-data",
    21: "ftp",
    22: "ssh",
    23: "telnet",
    25: "smtp",
    53: "dns",
    67: "dhcp",
    68: "dhcp",
    69: "tftp",
    80: "http",
    110: "pop3",
    111: "rpcbind",
    123: "ntp",
    135: "msrpc",
    139: "netbios",
    143: "imap",
    161: "snmp",
    389: "ldap",
    443: "https",
    445: "smb",
    587: "smtp-tls",
    631: "ipp",
    3306: "mysql",
    3389: "rdp",
}

target = str(input("Enter your target ip: "))

print(f"Starting scan on {target}")
start_time = datetime.now()

for port in range(1, 65536):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.1)
    result = s.connect_ex((target, port))

    if result == 0:
        protocol = "tcp"
        service = common_services.get(port, "unknown")
        state = "open"

        print(f"{target:<15} {port:<6} {state:<6} {protocol:<5} {service}")
    s.close()

end_time = datetime.now()
print(f"Scan completed in: {end_time - start_time}")
