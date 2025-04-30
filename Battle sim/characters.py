# characters.py
import random
from faker import Faker
import pandas as pd
from utils import display_character, plot_character_stats
from file import characters

fake = Faker()

def character_menu():
    def create_character():
        use_random = input("Generate random character? (y/n): ").lower()
        if use_random == 'y':
            name = fake.first_name()
            backstory = fake.sentence(nb_words=12)
            skills = [fake.word() for _ in range(3)]
        else:
            name = input("Enter the character's name: ")
            backstory = input("Enter a backstory: ")
            skills = input("Enter 3 skills separated by commas: ").split(',')

        if name in characters:
            print("Character already exists.")
            return

        characters[name] = {
            'name': name,
            'health': random.randint(80, 120),
            'strength': random.randint(10, 20),
            'defense': random.randint(5, 15),
            'speed': random.randint(5, 15),
            'level': 1,
            'xp': 0,
            'backstory': backstory,
            'skills': [s.strip() for s in skills]
        }
        print(f"Character '{name}' created!")

    def view_characters():
        if not characters:
            print("No characters to display.")
            return
        for char in characters.values():
            display_character(char)

    def visualize_character():
        if not characters:
            print("No characters to display.")
            return
        name = input("Enter character name to visualize: ")
        if name in characters:
            plot_character_stats(characters[name])
            (characters[name])
        else:
            print("Character not found.")

    def analyze_characters():
        if not characters:
            print("No characters to analyze.")
            return
        df = pd.DataFrame(characters.values())
        print("\nStatistical Summary:")
        print(df[['health', 'strength', 'defense', 'speed']].describe())
        print("\nVariance:")
        print(df[['health', 'strength', 'defense', 'speed']].var())  # bonus feature

    while True:
        print("\nCharacter Menu:")
        print("1. Create Character")
        print("2. View Characters")
        print("3. Visualize Character Stats")
        print("4. Analyze All Characters")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ")
        if choice == '1':
            create_character()
        elif choice == '2':
            view_characters()
        elif choice == '3':
            visualize_character()
        elif choice == '4':
            analyze_characters()
        elif choice == '5':
            break
        else:
            print("Invalid option.")
