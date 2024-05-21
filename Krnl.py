import os
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
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
    print(LARANJA + "OSINT:" + BLUE)
    print("{1} - sherlock")
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
    elif command == ";sherlock":
    	social_media_sites = {
    "Twitter": "https://twitter.com/{}",
    "Facebook": "https://www.facebook.com/{}",
    "Instagram": "https://www.instagram.com/{}",
    # Adicione mais sites conforme necessário
}

def check_site(site, url, username):
    full_url = url.format(username)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(full_url, headers=headers)
        if response.status_code == 200:
            # Verifique o conteúdo da página para confirmação
            if "profile not found" in response.text.lower() or "page not found" in response.text.lower():
                return site, "Usuário não encontrado"
            else:
                return site, full_url
        else:
            return site, "Usuário não encontrado"
    except requests.RequestException as e:
        return site, f"Erro ao acessar {site}: {e}"

def check_username(username):
    results = {}
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(check_site, site, url, username) for site, url in social_media_sites.items()]
        for future in as_completed(futures):
            site, result = future.result()
            results[site] = result
            time.sleep(1)  # Atraso entre requisições para evitar bloqueios
    
    return results

def main():
    print(f"{VERDE}Digite um nome:{RESET}")
    username = input()
    print(f"{VERDE}[{LARANJA}*{VERDE}] Verificando nome de usuário {RESET}{username}{VERDE} em: {RESET}")
    results = check_username(username)
    
    for site, result in results.items():
        print(f"{VERDE}[{LARANJA}*{VERDE}] {site}: {RESET}{result}")

if __name__ == "__main__":
    main()
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