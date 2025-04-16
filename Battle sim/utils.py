# Avery bowman

import os
import platform

def clear_screen():
    # Clear the console screen for better UI experience
    # Check the operating system and use the appropriate command
    if platform.system() == "Windows":
        os.system('cls')
    else:  # For Linux and MacOS
        os.system('clear')

def print_header(title):
    # Print a formatted header with the title
    width = 50
    print("=" * width)
    print(f"{title.center(width)}")
    print("=" * width)
    print()