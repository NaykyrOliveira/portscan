import socket

ports = [20, 21, 22, 23, 25, 80, 109, 110, 115, 143, 220, 443, 445, 465, 587, 1433, 1434, 1521, 1522, 2483, 2484, 3306, 5432]

for port in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.1)
    if client.connect_ex(("bancocn.com", port)) == 0:
        print(port, "open")



