import random
from utils import display_character
from file import characters

def character_menu():
    def create_character():
        name = input("Enter the characters name: ")
        if name in characters:
            print("The character already exists.")
            return
        characters[name] = {
            'name': name,
            'health': random.randint(80, 120),
            'strength': random.randint(10, 20),
            'defense': random.randint(5, 15),
            'speed': random.randint(5, 15),
            'level': 1,
            'xp': 0
        }
        print(f"Character '{name}' created!")

    def view_characters():
        if not characters:
            print("No characters to display.")
            return
        for char in characters.values():
            display_character(char)

    while True:
        print("\nCharacter Menu:")
        print("1. Create your Character")
        print("2. View all the Characters")
        print("3. Back to Main Menu")
        choice = input("Choose an option: ")
        if choice == '1':
            create_character()
        elif choice == '2':
            view_characters()
        elif choice == '3':
            break
        else:
            print("Invalid option.")