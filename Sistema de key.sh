#!/bin/bash

clear

BLUE='\033[34m'
COR="\033[38;2;92;92;255m"
GREEN='\033[32m'
green='\033[1;32m'
red='\033[1;31m'
yellow='\033[1;33m'
RESET='\033[0m'

echo -e "${BLUE}Krnl Sistema de Key (0):${RESET}"
echo -e "${BLUE}Escreva \"key 1\" para fazer a key 1${RESET}"

read -r input

if [ "$input" = "key 1" ]; then
  echo -e "${yellow}Espere 3 segundos para continuar...${RESET}"
  sleep 3
  clear
  echo -e "${BLUE}Krnl Sistema de Key (1):${RESET}"
  echo -e "${BLUE}Escreva \"key 2\" para fazer a key 2${RESET}"

  read -r input

  if [ "$input" = "key 2" ]; then
    echo -e "${yellow}Espere 3 segundos para continuar...${RESET}"
    sleep 3
    clear
    echo -e "${BLUE}Krnl Sistema de Key (2):${RESET}"
    echo -e "${BLUE}Escreva \"key 3\" para terminar o sistema de key${RESET}"

    read -r input

    if [ "$input" = "key 3" ]; then
      echo -e "${yellow}Espere 4 segundos para continuar...${RESET}"
      sleep 4
      clear
      echo -e "${BLUE}Key: 2e6ce0f1197608fa5b0127fae8f1ed56${RESET}"
      
      echo -n -e "${yellow}insira sua Key aqui:${RESET}"
read -p " " input
      
    fi
  fi
fi

if [ "$input" = "key 2e6ce0f1197608fa5b0127fae8f1ed56" ]; then
    echo -e "${GREEN}Key correta!${RESET}"
  sleep 3
   echo -e "${yellow}iniciando...${RESET}"
    sleep 4
    clear
    git clone https://github.com/porrinha09/Krnl-Tools.git ; cd Krnl-Tools ; wget https://raw.githubusercontent.com/porrinha09/Krnl-Tools/main/Krnl.sh
fi
