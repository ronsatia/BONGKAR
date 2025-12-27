#!/bin/bash

# --- WARNA ---
G='\033[0;32m'
C='\033[0;36m'
Y='\033[1;33m'
R='\033[0;31m'
W='\033[0m'

clear
echo -e "${C}===========================================${W}"
echo -e "${C}     B O N G K A R  -  INSTALLER           ${W}"
echo -e "${C}          Script By Ronis                  ${W}"
echo -e "${C}===========================================${W}"
echo ""

# 1. Cek Python3
echo -e "${Y}[*] Checking Python3...${W}"
if command -v python3 &>/dev/null; then
    echo -e "${G}[+] Python3 is installed.${W}"
else
    echo -e "${R}[-] Python3 not found. Please install it first.${W}"
    exit 1
fi

# 2. Cek Pip3
echo -e "${Y}[*] Checking Pip3...${W}"
if command -v pip3 &>/dev/null; then
    echo -e "${G}[+] Pip3 is installed.${W}"
else
    echo -e "${Y}[!] Pip3 not found. Trying to install...${W}"
    sudo apt-get update && sudo apt-get install python3-pip -y
fi

# 3. Install Dependensi
echo -e "${Y}[*] Installing required libraries...${W}"
pip3 install jsbeautifier uncompyle6 colorama

# 4. Set Permission
echo -e "${Y}[*] Setting permissions...${W}"
chmod +x bongkar.py
if [ $? -eq 0 ]; then
    echo -e "${G}[+] Permissions set successfully.${W}"
else
    echo -e "${R}[-] Failed to set permissions.${W}"
fi

echo ""
echo -e "${C}-------------------------------------------${W}"
echo -e "${G} INSTALLATION COMPLETE! ${W}"
echo -e "${Y} Type 'python3 bongkar.py' to start the tool. ${W}"
echo -e "${C}-------------------------------------------${W}"
