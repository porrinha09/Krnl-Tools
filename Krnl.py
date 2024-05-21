import os

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

def process_command(command):
    if command == "my ip":
        # Adicione aqui a lógica para obter e exibir o endereço IP
        print("Seu endereço IP é 192.168.1.1")  # Exemplo simples

os.system("clear")
print_command_list()

while True:
    print_command_list()
    command = input("\033[34m┌──(Kelvin zv)-[~]\n└─$ \033[0m")
    process_command(command)