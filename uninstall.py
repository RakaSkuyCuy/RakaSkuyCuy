import sys
import time
import pyfiglet
from colorama import Fore, Style, init
import subprocess
import os

# Inisialisasi colorama untuk output berwarna
init(autoreset=True)

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def tampilkan_progress_bar():
    clear_terminal()
    
    # Tampilkan ASCII art besar dengan warna
    ascii_art = pyfiglet.figlet_format("KenSploit Spam", font="slant")
    print(f"{Fore.BLUE}{ascii_art}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}\nMenghapus kensploitspam, harap tunggu...{Style.RESET_ALL}")

    # Simulasikan progress bar uninstalasi
    for i in range(101):
        if i % 5 == 0:
            sys.stdout.write(f"\r{Fore.RED}Progress: [{'=' * (i // 5)}{' ' * (20 - i // 5)}] {i}%{Style.RESET_ALL}")
            sys.stdout.flush()
        time.sleep(0.05)  # Simulasi waktu uninstalasi

    print()  # Baris baru setelah progress bar selesai

def jalankan_uninstalasi():
    try:
        # Hapus paket dengan pip dan sembunyikan output debug
        print(f"{Fore.CYAN}Menjalankan pip uninstall...{Style.RESET_ALL}")
        subprocess.check_call(["pip", "uninstall", "-y", "kensploitspam"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"\n{Fore.GREEN}kensploitspam telah dihapus.{Style.RESET_ALL}")
    except subprocess.CalledProcessError as e:
        # Cetak pesan error jika uninstalasi gagal
        print(f"\n{Fore.RED}Error selama uninstalasi:{Style.RESET_ALL}")
        print(e.output.decode())

if __name__ == "__main__":
    tampilkan_progress_bar()
    jalankan_uninstalasi()
