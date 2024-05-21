import os
import requests
import json

COR = "\033[38;2;92;92;255m"
BLUE = "\033[38;2;128;163;255m"
VERDE = "\033[38;2;79;205;177m"
VERMELHO = "\033[38;2;255;0;0m"  
LARANJA = "\033[38;2;241;133;30m"
RESET = "\033[0m"

def print_command_list():
    print(BLUE + "Bem-vindo ao Krnl Tools" + RESET)
    print(BLUE + "------------------------------------------------" + RESET)
    print(LARANJA + "IP:" + BLUE)
    print("{1} - ;my ip")
    print("{2} - ;ip info")
    print("{3} - ;my ip")
    print("{4} - ;ip info")
    
def process_command(command):
    if command == ";my ip":
        response = requests.get('https://ipinfo.io/ip')
        return response.text.strip()

    if command == ";ip info":
        def get_ip_info(ip):
            url = f"https://ipinfo.io/{ip}"
            response = requests.get(url)
            if response.status_code == 200:
                data = json.loads(response.text)
                return data
            else:
                return None

        ip = input("IP: ")
        ip_info = get_ip_info(ip)

        if ip_info:
            country = ip_info.get('country', 'N/A')
            state = ip_info.get('region', 'N/A')
            city = ip_info.get('city', 'N/A')
            timezone = ip_info.get('timezone', 'N/A')

            print(f"País: {country}")
            print(f"Estado: {state}")
            print(f"Cidade: {city}")
            print(f"Horário: {timezone}")
        else:
            print("Erro ao obter informações do IP.")

        os.system("clear")
        print_command_list()

while True:
    command = input("\033[34m┌──(Kelvin zv)-[~]\n└─$ \033[0m")
    process_command(command)