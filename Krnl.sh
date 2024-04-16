clear

BLUE='\033[34m'
COR="\033[38;2;92;92;255m"
GREEN='\033[32m'
green='\033[1;32m'
red='\033[1;31m'
yellow='\033[1;33m'
RESET='\033[0m'

echo -e "${COR}Bem-vindo ao Moon Tool, escolha uma opção:${RESET}"
echo -e "${COR}------------------------------------------------------------
{1} - IP info
{2} - View my ip
{3} - View device information

{99} - Sair
------------------------------------------------------------"

echo -n -e "${COR}┌──(Kelvin zv)-[~]
└─$ ${RESET}"
read -p " " input

if [ "$input" -eq 1 ]; then
 read -p "IP: " ip

response=$(curl -s https://ipinfo.io/$ip)

country=$(echo "$response" | grep -o '"country": "[^"]*' | cut -d'"' -f4)
region=$(echo "$response" | grep -o '"region": "[^"]*' | cut -d'"' -f4)
city=$(echo "$response" | grep -o '"city": "[^"]*' | cut -d'"' -f4)

echo "País: $country"
echo "Estado/Região: $region"
echo "Cidade: $city"
fi

if [ "$input" -eq 2 ]; then
  ip=$(curl -s ifconfig.me)
  "seu ip: $ip"
fi

if [ "$input" -eq 3 ]; then
device_name=$(getprop ro.product.brand)
device_model=$(getprop ro.product.model)
android_version=$(getprop ro.build.version.release)

echo "Nome do dispositivo: $device_name"
echo "Modelo do dispositivo: $device_model"
echo "Versão do Android: $android_version"
fi

if [ "$input" -eq 99 ]; then
  clear
fi
