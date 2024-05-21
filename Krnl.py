import os
import requests

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
    print(LARANJA + "IP:" + RESET)
    print(BLUE + "{1} - my ip" + RESET)

def get_ip():
    response = requests.get('https://ipinfo.io/ip')
    return response.text.strip()

def process_command(command):
    if command == ";my ip":
        ip = get_ip()
        print(f"Seu IP: {ip}")

    print_command_list()

def main():
    while True:
        command = input("\033[34m┌──(Kelvin zv)-[~]\n└─$ \033[0m")
        process_command(command)

if __name__ == "__main__":
    main()