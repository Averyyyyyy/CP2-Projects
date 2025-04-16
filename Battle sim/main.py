# Avery bowman, battle sim

import os
import csv
import time
from character import Character
from battle import battle_characters
from utils import clear_screen, print_header

def main():
    characters = []
    
    # Load existing characters at startup
    if os.path.exists('characters.csv'):
        characters = load_characters()
    
    def display_menu():
        # Inner function to display the main menu
        print_header("RPG CHARACTER MANAGER")
        print("1. Create New Character")
        print("2. View Characters")
        print("3. Battle Characters")
        print("4. Save & Exit")
        return input("Select an option (1-4): ")
    
    def create_character():
        # Inner function to handle character creation
        clear_screen()
        print_header("CHARACTER CREATION")
        
        # Get character info from user
        name = input("Enter character name: ")
        
        # Check if name already exists
        if any(c.name.lower() == name.lower() for c in characters):
            print("A character with that name already exists!")
            time.sleep(2)
            return
        
        # Set default stats with option to customize
        customize = input("Use default stats (100 HP, 10 STR, 5 DEF, 8 SPD)? (y/n): ").lower()
        
        if customize == 'y':
            new_character = Character(name, 100, 10, 5, 8)
        else:
            try:
                health = int(input("Enter health points (50-150): "))
                strength = int(input("Enter strength points (5-20): "))
                defense = int(input("Enter defense points (1-15): "))
                speed = int(input("Enter speed points (5-15): "))
                new_character = Character(name, health, strength, defense, speed)
            except ValueError:
                print("Invalid input. Using default stats instead.")
                new_character = Character(name, 100, 10, 5, 8)
        
        characters.append(new_character)
        save_characters(characters)
        print(f"\nCharacter '{name}' created successfully!")
        time.sleep(2)
    
    def view_characters():
        # Inner function to display all characters
        clear_screen()
        print_header("CHARACTER ROSTER")
        
        if not characters:
            print("No characters found.")
            input("\nPress Enter to continue...")
            return
        
        for i, character in enumerate(characters, 1):
            print(f"{i}. {character}")
        
        input("\nPress Enter to continue...")
    
    def battle_menu():
        # Inner function to handle character battles
        if len(characters) < 2:
            clear_screen()
            print("You need at least 2 characters to battle!")
            time.sleep(2)
            return
        
        clear_screen()
        print_header("BATTLE MODE")
        
        # Display characters for selection
        for i, character in enumerate(characters, 1):
            print(f"{i}. {character.name} (Level {character.level})")
        
        try:
            choice1 = int(input("\nSelect first character (number): ")) - 1
            choice2 = int(input("Select second character (number): ")) - 1
            
            if choice1 == choice2:
                print("A character cannot battle itself!")
                time.sleep(2)
                return
            
            if 0 <= choice1 < len(characters) and 0 <= choice2 < len(characters):
                winner = battle_characters(characters[choice1], characters[choice2])
                
                # Save updated character stats
                save_characters(characters)
                
                input("\nPress Enter to continue...")
            else:
                print("Invalid character selection!")
                time.sleep(2)
        except ValueError:
            print("Invalid input! Please enter a number.")
            time.sleep(2)
    
    # Main program loop
    while True:
        clear_screen()
        choice = display_menu()
        
        if choice == '1':
            create_character()
        elif choice == '2':
            view_characters()
        elif choice == '3':
            battle_menu()
        elif choice == '4':
            save_characters(characters)
            clear_screen()
            print("Characters saved. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
            time.sleep(1)

def load_characters():
    # Helper function to load characters from CSV
    characters = []
    try:
        with open('characters.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) >= 7:  # Check if we have all needed fields
                    name, health, strength, defense, speed, level, exp = row
                    character = Character(
                        name, 
                        int(health), 
                        int(strength), 
                        int(defense), 
                        int(speed), 
                        int(level), 
                        int(exp)
                    )
                    characters.append(character)
    except FileNotFoundError:
        pass  # If file doesn't exist yet, return empty list
    except Exception as e:
        print(f"Error loading characters: {e}")
    
    return characters

def save_characters(characters):
    # Helper function to save characters to CSV
    try:
        with open('characters.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for character in characters:
                writer.writerow([
                    character.name,
                    character.health,
                    character.strength,
                    character.defense,
                    character.speed,
                    character.level,
                    character.experience
                ])
    except Exception as e:
        print(f"Error saving characters: {e}")

if __name__ == "__main__":
    main()