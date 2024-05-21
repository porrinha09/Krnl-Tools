import os
import requests
import json

# Definição de constantes para cores de texto
COR = "\033[38;2;92;92;255m"
BLUE = "\033[38;2;128;163;255m"
VERDE = "\033[38;2;79;205;177m"
VERMELHO = "\033[38;2;255;0;0m"  
LARANJA = "\033[38;2;241;133;30m"
RESET = "\033[0m"

# Função para imprimir a lista de comandos disponíveis
def print_command_list():
    print(BLUE + "Bem-vindo ao Krnl Tools" + RESET)
    print(BLUE + "------------------------------------------------" + RESET)
    print(LARANJA + "IP:" + BLUE)
    print("{1} - ;my ip")
    print("{2} - ;ip info")

# Função para obter o endereço IP do usuário
def get_ip():
    response = requests.get('https://ipinfo.io/ip')
    return response.text.strip()

# Função para obter informações do IP fornecido
def get_ip_info(ip):
    url = f"https://ipinfo.io/{ip}"
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
        return data
    else:
        return None

# Função para obter o horário atual com base no fuso horário
def get_current_time(timezone):
    import datetime
    import pytz
    tz = pytz.timezone(timezone)
    current_time = datetime.datetime.now(tz)
    return current_time.strftime("%H:%M")

# Impressão da lista de comandos disponíveis
print_command_list()

# Loop principal para receber e processar comandos
while True:
    command = input("\033[34m┌──(Kelvin zv)-[~]\n└─$ \033[0m")
    if command == ";my ip":
        ip = get_ip()
        print(f"Seu IP: {ip}")
    elif command == ";ip info":
        ip = input("IP: ")
        ip_info = get_ip_info(ip)
        if ip_info:
            country = ip_info.get('country', 'N/A')
            state = ip_info.get('region', 'N/A')
            city = ip_info.get('city', 'N/A')
            timezone = ip_info.get('timezone', 'N/A')
            current_time = get_current_time(timezone)
            print(f"País: {country}")
            print(f"Estado: {state}")
            print(f"Cidade: {city}")
            print(f"Horário: {current_time}")
        else:
            print("Erro ao obter informações do IP.")
    else:
        print("Comando não reconhecido.")