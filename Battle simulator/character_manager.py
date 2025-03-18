# character_manager.py
import csv
import os

def create_character_manager(clear_screen, pause):
    # Create and return a character manager with inner functions.
    
    # File operation helper functions
    def save_character_to_csv(character):
        """Save a character to the CSV file."""
        file_exists = os.path.isfile("characters.csv")
        with open("characters.csv", mode='a', newline='') as file:
            fieldnames = ['name', 'class', 'level', 'experience', 'health', 'max_health', 
                         'strength', 'defense', 'speed', 'abilities']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            
            # Write header if file is being created for the first time
            if not file_exists:
                writer.writeheader()
            
            # Convert abilities list to string for storage
            character_copy = character.copy()
            if 'abilities' in character_copy and character_copy['abilities']:
                character_copy['abilities'] = ','.join(character_copy['abilities'])
            else:
                character_copy['abilities'] = ''
            
            writer.writerow(character_copy)
        print(f"\nCharacter '{character['name']}' saved successfully!")

    def load_characters_from_csv():
        # Load all characters from the CSV file.
        characters = []
        if not os.path.isfile("characters.csv"):
            print("\nNo character data found.")
            return characters
        
        try:
            with open("characters.csv", mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Convert numeric strings to appropriate types
                    row['level'] = int(row['level'])
                    row['experience'] = int(row['experience'])
                    row['health'] = int(row['health'])
                    row['max_health'] = int(row['max_health'])
                    row['strength'] = int(row['strength'])
                    row['defense'] = int(row['defense'])
                    row['speed'] = int(row['speed'])
                    
                    # Convert abilities string back to list
                    if row['abilities']:
                        row['abilities'] = row['abilities'].split(',')
                    else:
                        row['abilities'] = []
                    
                    characters.append(row)
            return characters
        except Exception as e:
            print(f"\nError loading characters: {e}")
            return []
    
    # Helper function for displaying character information
    def display_character_info(character):
        # Display detailed information about a character.
        print("\n" + "-"*50)
        print(f"Name: {character['name']} (Lvl {character['level']} {character['class']})")
        print(f"Experience: {character['experience']} / {character['level'] * 100}")
        print(f"Health: {character['health']} / {character['max_health']}")
        print(f"Strength: {character['strength']}")
        print(f"Defense: {character['defense']}")
        print(f"Speed: {character['speed']}")
        
        if character['abilities']:
            print("Abilities:", ", ".join(character['abilities']))
        print("-"*50)
    
    # Inner function for character creation
    def create_character():
        #Handle character creation process.
        #This is one of the two main inner functions
        clear_screen()
        print("\n" + "="*50)
        print("CHARACTER CREATION".center(50))
        print("="*50)
        
        #Get basic character info
        name = input("Enter character name: ").strip()
        if not name:
            print("Character name cannot be empty!")
            pause()
            return
        
        #Check if character already exists
        existing_characters = load_characters_from_csv()
        if any(char['name'] == name for char in existing_characters):
            print(f"Character '{name}' already exists!")
            pause()
            return
        
        # Choose character class
        print("\nCharacter Classes:")
        print("1. Warrior (High strength and defense)")
        print("2. Mage (High health and magical abilities)")
        print("3. Rogue (High speed and critical hits)")
        
        class_choice = input("\nChoose a class (1-3): ")
        
        # Set base attributes based on class
        if class_choice == '1':
            char_class = "Warrior"
            health = 100
            strength = 15
            defense = 12
            speed = 8
            abilities = ["Power Strike"]
        elif class_choice == '2':
            char_class = "Mage"
            health = 80
            strength = 8
            defense = 8
            speed = 10
            abilities = ["Fireball"]
        elif class_choice == '3':
            char_class = "Rogue"
            health = 90
            strength = 10
            defense = 7
            speed = 15
            abilities = ["Backstab"]
        else:
            print("Invalid class selection! Defaulting to Warrior.")
            char_class = "Warrior"
            health = 100
            strength = 15
            defense = 10
            speed = 8
            abilities = ["Power Strike"]
        
        # Create character dictionary
        character = {
            'name': name,
            'class': char_class,
            'level': 1,
            'experience': 0,
            'health': health,
            'max_health': health,
            'strength': strength,
            'defense': defense,
            'speed': speed,
            'abilities': abilities
        }
        
        # Confirm character creation
        clear_screen()
        display_character_info(character)
        confirm = input("\nCreate this character? (y/n): ").lower()
        
        if confirm == 'y':
            save_character_to_csv(character)
        else:
            print("\nCharacter creation cancelled.")
        
        pause()
    
    # Inner function for viewing characters
    def view_characters():
        """Display all available characters."""
        clear_screen()
        print("\n" + "="*50)
        print("CHARACTER ROSTER".center(50))
        print("="*50)
        
        characters = load_characters_from_csv()
        
        if not characters:
            print("No characters found. Create some first!")
            pause()
            return
        
        for i, character in enumerate(characters, 1):
            print(f"\n{i}. {character['name']} (Lvl {character['level']} {character['class']})")
        
        while True:
            try:
                choice = input("\nEnter character number to view details (or 0 to return): ")
                if choice == '0':
                    return
                
                char_index = int(choice) - 1
                if 0 <= char_index < len(characters):
                    clear_screen()
                    display_character_info(characters[char_index])
                    pause()
                    view_characters()  # Return to character list
                    return
                else:
                    print("Invalid character number!")
            except ValueError:
                print("Please enter a valid number!")
    
    # Return a dictionary of functions
    return {
        'create_character': create_character,
        'view_characters': view_characters,
        'load_characters_from_csv': load_characters_from_csv,
        'display_character_info': display_character_info,
        'save_character_to_csv': save_character_to_csv
    }