import socket
import subprocess

def scan_ports(hostname, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((hostname, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

def get_users():
    output = subprocess.check_output("last", shell=True)
    lines = output.decode("utf-8").split("\n")
    users = set()
    for line in lines:
        parts = line.split()
        if len(parts) > 0:
            users.add(parts[0])
    return users

# Kërkimi i URL-së së uebfaqes nga përdoruesi
website = input("Ju lutem jepni URL-në e uebfaqes: ")

# Kontrolli nëse URL-ja fillon me "http://" ose "https://"
if not website.startswith("http://") and not website.startswith("https://"):
    website = "http://" + website

# Skanimi i portave
start_port = 1
end_port = 1000
open_ports = scan_ports(website, start_port, end_port)
print(f"Portat e hapura në {website}:")
for port in open_ports:
    print(f"Porti {port} është i hapur.")

# Gjetja e përdoruesve
users = set()
search_command = f"last | grep {website}"
try:
    output = subprocess.check_output(search_command, shell=True)
    lines = output.decode("utf-8").split("\n")
    for line in lines:
        parts = line.split()
        if len(parts) > 0:
            users.add(parts[0])
except subprocess.CalledProcessError:
    print("Gabim gjatë gjetjes së përdoruesve.")

print("Përdoruesit që janë përdorur për të hyrë në uebfaqen:")
for user in users:
    print(user)
