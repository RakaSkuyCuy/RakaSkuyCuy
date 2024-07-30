import os
import subprocess
import time
from colorama import Fore, Style, init
import pyfiglet

# Inisialisasi colorama
init(autoreset=True)

# Definisikan warna
bold = Style.BRIGHT
blue = Fore.BLUE
cyan = Fore.CYAN
green = Fore.GREEN
yellow = Fore.YELLOW
magenta = Fore.MAGENTA
red = Fore.RED
reset = Style.RESET_ALL

# Fungsi untuk membersihkan layar
def clear_screen():
    print('\033c', end='')

# Fungsi untuk mencetak header dengan teks besar
def print_header():
    clear_screen()
    ascii_art = pyfiglet.figlet_format("KennSploit Spam", font="slant")
    print(f"{bold}{blue}{ascii_art}")
    print(f"{bold}{yellow}Author: KennSploit")

# Fungsi untuk menemukan file kensploit.py di semua direktori
def find_kensploit_script():
    try:
        # Mulai pencarian dari direktori saat ini
        for root, dirs, files in os.walk(os.getcwd()):
            if 'kensploit.py' in files:
                return os.path.join(root, 'kensploit.py')
        
        # Jika tidak ditemukan
        print(f"{bold}{red}FILE TIDAK DITEMUKAN!{reset}")
        print(f"{bold}{red}Pastikan file kensploit.py ada di salah satu direktori.{reset}")
        exit(1)
    except Exception as e:
        print(f"{bold}{red}Terjadi kesalahan saat memeriksa file kensploit.py: {str(e)}{reset}")
        exit(1)

# Fungsi untuk menjalankan script kensploit.py dan memasukkan input
def run_kensploit(nomor_hp, serangan_nomor):
    ks_path = find_kensploit_script()
    print(f"{bold}{green}Memulai serangan {serangan_nomor}...")
    # Jalankan kensploit.py menggunakan subprocess
    try:
        process = subprocess.Popen(
            ["python", ks_path],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        stdout, stderr = process.communicate(input=f"1\n{nomor_hp}\n".encode())
        if stderr:
            print(f"{bold}{red}Error: {stderr.decode()}{reset}")
        else:
            print(f"{bold}{magenta}Serangan {serangan_nomor} selesai :)")
    except Exception as e:
        print(f"{bold}{red}Terjadi kesalahan saat menjalankan kensploit.py: {str(e)}{reset}")

# Minta input nomor HP dari pengguna
def main():
    print_header()
    nomor_hp = input("Masukkan nomor HP: ")

    # Inisialisasi nomor serangan
    serangan_nomor = 1

    # Loop untuk menjalankan script berulang kali
    while True:
        print_header()
        run_kensploit(nomor_hp, serangan_nomor)
        serangan_nomor += 1
        # Tambahkan jeda jika perlu untuk mengurangi beban
        time.sleep(1)

if __name__ == "__main__":
    main()

