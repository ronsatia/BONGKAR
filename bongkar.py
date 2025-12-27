import os
import sys
import time
import base64
import binascii
import codecs

# --- KONFIGURASI WARNA (TACTICAL THEME) ---
# Jika di Windows terminal tidak berwarna, install 'colorama' atau gunakan terminal baru
G = "\033[92m"  # Green
C = "\033[96m"  # Cyan
R = "\033[91m"  # Red
Y = "\033[93m"  # Yellow
W = "\033[0m"   # White/Reset
B = "\033[1m"   # Bold

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def loading_anim(text):
    for x in range(3):
        sys.stdout.write(f"\r{C}[*] {text}.{W}")
        time.sleep(0.2)
        sys.stdout.write(f"\r{C}[*] {text}..{W}")
        time.sleep(0.2)
        sys.stdout.write(f"\r{C}[*] {text}...{W}")
        time.sleep(0.2)
    print(f"\r{G}[+] {text} COMPLETED!{W}   ")

def banner():
    clear_screen()
    print(C + B + r"""
      :::  :::::::::   ::::::::  ::::    :::  ::::::::  :::    :::      :::     :::::::::
     :+:  :+:    :+: :+:    :+: :+:+:   :+: :+:    :+: :+:   :+:      :+:     :+:    :+:
    +:+  +:+    +:+ +:+    +:+ :+:+:+  +:+ +:+        +:+  +:+      +:+:+    +:+    +:+
   +#+  +#++:++#+  +#+    +:+ +#+ +:+ +#+ :#:        +#++:++      +#+ +:+   +#++:++#:
  +#+  +#+    +#+ +#+    +#+ +#+  +#+#+# +#+   +#+# +#+  +#+    +#+  +#+  +#+    +#+
 #+#  #+#    #+# #+#    #+# #+#   #+#+# #+#    #+# #+#   #+#  +#+#+#+#+# #+#    #+#
###  #########   ########  ###    ####  ########  ###    ### ###     ### ###    ###
    """ + W)
    print(f"   {G}[+] SYSTEM: ONLINE         [+] TARGET: OBFUSCATION      [+] MODE: AGGRESSIVE{W}")
    print(f"   {C}----------------------------------------------------------------------------{W}")
    print(f"              {Y}< B O N G K A R - DECRYPTION FRAMEWORK v1.0 >{W}")
    print(f"                        {R}>> Script By Ronis <<{W}")
    print("\n")

# --- MODUL LOGIC ---

def decode_universal():
    print(f"\n{Y}[ UNIVERSAL DECODER MENU ]{W}")
    print(" 1. Base64 Decode")
    print(" 2. Hex to String")
    print(" 3. ROT13 (Caesar Cipher)")
    print(" 4. Reverse Text")
    print(" 0. Kembali")
    
    p = input(f"\n{C}BONGKAR/Universal > {W}")
    
    if p == '1':
        try:
            data = input(" Masukkan String Base64: ")
            res = base64.b64decode(data).decode('utf-8', errors='ignore')
            print(f"\n{G}[RESULT]:{W}\n{res}")
        except Exception as e:
            print(f"{R}[ERROR] Format Base64 salah!{W}")
            
    elif p == '2':
        try:
            data = input(" Masukkan String Hex (tanpa 0x): ")
            res = bytes.fromhex(data).decode('utf-8', errors='ignore')
            print(f"\n{G}[RESULT]:{W}\n{res}")
        except:
            print(f"{R}[ERROR] Format Hex salah!{W}")

    elif p == '3':
        data = input(" Masukkan Text: ")
        print(f"\n{G}[RESULT]:{W}\n{codecs.decode(data, 'rot_13')}")

    elif p == '4':
        data = input(" Masukkan Text: ")
        print(f"\n{G}[RESULT]:{W}\n{data[::-1]}")

def php_decoder():
    print(f"\n{Y}[ PHP DECODER UTILITY ]{W}")
    print(" Tools ini mencoba men-decode string base64 yang berlapis (recursive).")
    print(" Berguna untuk script malware/shell sederhana.")
    
    data = input(" Masukkan Raw String (Base64): ")
    iteration = 0
    
    loading_anim("Analyzing PHP Hash")
    
    try:
        current_data = data
        while True:
            # Coba decode
            try:
                decoded = base64.b64decode(current_data).decode('utf-8', errors='ignore')
            except:
                break # Stop jika gagal decode
            
            # Cek apakah hasil decode masih terlihat seperti base64 (alphanumeric only)
            if not decoded.isprintable() or len(decoded) < 5:
                break
                
            current_data = decoded
            iteration += 1
            print(f" Layer {iteration} opened...")
            
        print(f"\n{G}[FINAL RESULT - Layer {iteration}]:{W}\n{current_data[:500]}...")
        if len(current_data) > 500: print(f"{Y}(Output dipotong karena terlalu panjang){W}")
            
    except Exception as e:
        print(f"{R}[ERROR]{W} {e}")

def python_uncompiler():
    print(f"\n{Y}[ PYTHON UNCOMPILER (.pyc) ]{W}")
    print(f"{R}[!] Wajib install 'uncompyle6' dulu (pip install uncompyle6){W}")
    
    path = input(" Masukkan path file .pyc: ")
    if os.path.exists(path):
        loading_anim("Decompiling Bytecode")
        os.system(f"uncompyle6 {path}")
    else:
        print(f"{R}[ERROR] File tidak ditemukan!{W}")

def js_deobfuscator():
    print(f"\n{Y}[ JAVASCRIPT DEOBFUSCATOR ]{W}")
    print(" Tips: Untuk JS Obfuscator.io yang kompleks, gunakan tool online.")
    print(" Menu ini akan merapikan (Beautify) kode JS yang berantakan.")
    
    path = input(" Masukkan path file .js: ")
    if os.path.exists(path):
        try:
            # Simple beautifier logic (basic indentation)
            import jsbeautifier # Perlu pip install jsbeautifier
            loading_anim("Beautifying Code")
            res = jsbeautifier.beautify_file(path)
            
            save_name = path + "_cleaned.js"
            with open(save_name, "w") as f:
                f.write(res)
            print(f"\n{G}[SUCCESS] File disimpan sebagai: {save_name}{W}")
        except ImportError:
            print(f"{R}[ERROR] Library 'jsbeautifier' belum diinstall.{W}")
            print("Ketik: pip install jsbeautifier")
    else:
        print(f"{R}[ERROR] File tidak ditemukan!{W}")

# --- MAIN MENU ---

def main_menu():
    banner()
    print(" [1] JavaScript Deobfuscator (Cleaner)")
    print(" [2] PHP Recursive Decoder (Base64)")
    print(" [3] Python Uncompyle (.pyc to .py)")
    print(" [4] Universal Decoder (B64, Hex, Rot13)")
    print(" [5] About Ronis")
    print(" [0] Exit")
    print(f" {C}-------------------------------------------{W}")
    
    choice = input(f" {Y}root@bongkar:~#{W} ")
    
    if choice == '1':
        js_deobfuscator()
    elif choice == '2':
        php_decoder()
    elif choice == '3':
        python_uncompiler()
    elif choice == '4':
        decode_universal()
    elif choice == '5':
        print(f"\n {G}Script By Ronis{W}")
        print(" GitHub: github.com/ronsatia")
        print(" Tujuan: Edukasi & Audit Keamanan.")
    elif choice == '0':
        print(f"\n {R}Exiting system... Goodbye.{W}")
        sys.exit()
    else:
        print(f"{R} Pilihan tidak valid!{W}")

if __name__ == "__main__":
    try:
        while True:
            main_menu()
            input(f"\n{C}[ Klik Enter untuk kembali ke Hub ]{W}")
    except KeyboardInterrupt:
        print(f"\n{R}Force Close detected.{W}")
        sys.exit()
