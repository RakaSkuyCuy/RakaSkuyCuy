from pyfiglet import Figlet
from colorama import Fore, Style, init
import sys
import time
import subprocess
import os

# Initialize colorama
init()

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def display_large_text(text):
    figlet = Figlet(font='slant')
    header_text = figlet.renderText(text)
    print(Fore.GREEN + header_text + Style.RESET_ALL)

def display_progress_bar():
    clear_terminal()
    
    # Display large text header using pyfiglet
    display_large_text('KenSploit Spam')
    print(Fore.YELLOW + "Sedang menginstall, tunggu sebentar..." + Style.RESET_ALL)

    # Simulate a progress bar
    progress_bar_length = 20  # Number of characters in the progress bar
    progress_step = 100 / progress_bar_length  # Percentage increase per step

    # Function to update progress bar
    def update_progress_bar(completed_percentage):
        bar_length = int(completed_percentage / progress_step)
        sys.stdout.write(f"\r{Fore.CYAN}Progress: [{'=' * bar_length}{' ' * (progress_bar_length - bar_length)}] {int(completed_percentage)}%{Style.RESET_ALL}")
        sys.stdout.flush()

    # Update progress bar during installation
    try:
        for i in range(101):
            time.sleep(0.01)  # Simulate work by sleeping
            update_progress_bar(i)  # Update progress bar
        print()  # Print a new line after the progress bar

        # Run j.py and suppress output
        subprocess.run(['python', 'j.py', 'install'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        # Clear the terminal again after installation
        clear_terminal()

        # Display large text again after installation
        display_large_text('KenSploit Spam')

        # Display completion message
        print(Fore.GREEN + "Setup selesai! Pakai dengan cara 'kensploitspam'. Have fun!!! :)" + Style.RESET_ALL)

    except Exception as e:
        # Suppress debug output and show a general error message
        print("\n" + Fore.RED + "Error during installation. Please check the logs." + Style.RESET_ALL)
        sys.exit(1)

if __name__ == "__main__":
    display_progress_bar()
