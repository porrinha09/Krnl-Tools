import os
import requests
from time import sleep
import subprocess

COR = "\033[38;2;92;92;255m"
BLUE = "\033[38;2;128;163;255m"
VERDE = "\033[38;2;79;205;177m"
VERMELHO = "\033[38;2;255;0;0m"  
LARANJA = "\033[38;2;241;133;30m"
RESET = "\033[0m"

def print_command_list():
    os.system("clear")
    print(BLUE + "Bem-vindo ao Krnl Tools" + RESET)
    print(BLUE + "------------------------------------------------" + RESET)
    print(LARANJA + "IP:" + BLUE)
    print("{1} - ;my ip")
    print("{2} - ;my mac")
    print("{3} - ;all my mac")
    print(LARANJA + "CONFIGS:" + BLUE)
    print("{99} - ;clear")
    print("{200} - ;reset")
    print("{100} - ;exit")
    print(BLUE + "------------------------------------------------" + RESET)

print_command_list()

def process_command(command):
    if command == ";my ip":
        def get_ip():
            response = requests.get('https://ipinfo.io/ip')
            return response.text.strip()

        ip = get_ip()
        print(f"Seu IP: {ip}")
    elif command == ";clear":
        os.system("clear")
    elif command == ";my mac":
output = subprocess.check_output(["ip", "link", "show"]).decode("utf-8")

for line in output.split('\n'):
    if "ether" in line:
        mac_address = line.split()[1]
        break

print("Seu MAC:", mac_address)
    elif command == ";all my mac":
output = subprocess.check_output(["ip", "link", "show"]).decode("utf-8")

mac_addresses = []

for line in output.split('\n'):
    if "ether" in line:
        mac_address = line.split()[1]
        mac_addresses.append(mac_address)

print("Seus MAC:", ", ".join(mac_addresses))
    elif command == ";reset":
        os.system("clear")
        sleep(1)
        print_command_list()
    elif command == ";exit":
        os.system("clear")
        exit()

while True:
    command = input("\033[34m┌──(Kelvin zv)-[~]\n└─$ \033[0m")
    process_command(command)