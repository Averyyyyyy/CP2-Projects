# Avery bowman, battle simulator
# The code is having a hard time calling the functin sand printing them after the main menu (where you select what number you want to do in the very beggining)

# main.py
import csv
import os
import time
from character_manager import create_character_manager
from battle_system import create_battle_system

def main():
    #Main function that initiates the RPG character manager program.
    
    # Inner function for displaying the main menu and getting user choice
    def display_main_menu():
        #Display the main menu and return user selection.
        print("\n" + "="*50)
        print("RPG CHARACTER MANAGER".center(50))
        print("="*50)
        print("1. Create a new character")
        print("2. View all characters")
        print("3. Battle characters")
        print("4. Exit program")
        print("-"*50)
        return input("Enter your choice (1-4): ")
    
    # Helper function to clear the screen
    def clear_screen():
        #Clear the console screen.
        os.system('cls' if os.name == 'nt' else 'clear')
    
    # Helper function for pausing execution
    def pause():
        #Pause execution until user presses Enter.
        input("\nPress Enter to continue...")
    
    # Import character manager functionality with inner functions
    character_manager = create_character_manager(clear_screen, pause)
    
    # Import battle system functionality with inner functions
    battle_system = create_battle_system(clear_screen, pause)
    
    # Main program loop
    while True:
        clear_screen()
        choice = display_main_menu()
        
        if choice == '1':
            character_manager.create_character()
        elif choice == '2':
            character_manager.view_characters()
        elif choice == '3':
            battle_system.battle_characters()
        elif choice == '4':
            print("\nThank you for playing! Goodbye!")
            break
        else:
            print("\nInvalid choice! Please try again.")
            pause()

if __name__ == "__main__":
    main()