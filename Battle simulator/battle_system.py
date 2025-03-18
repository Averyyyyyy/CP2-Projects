# battle_system.py
import random
import time
import os

def create_battle_system(clear_screen, pause):
    # Create and return a battle system with inner functions
    
    # Inner function for battles
    def battle_characters():
        # Handle character battles
        # This is the second main inner function
        
        # We need to import here to avoid circular import
        from character_manager import create_character_manager
        character_manager = create_character_manager(clear_screen, pause)
        load_characters_from_csv = character_manager['load_characters_from_csv']
        display_character_info = character_manager['display_character_info']
        save_character_to_csv = character_manager['save_character_to_csv']
        
        # Helper function for battle calculations
        def calculate_damage(attacker, defender):
            # Calculate damage dealt by attacker to defender. Returns (damage, is_critical)
            # Base damage calculation
            base_damage = max(1, attacker['strength'] - defender['defense'] // 2)
            
            # Critical hit chance (based on speed)
            critical_chance = min(40, attacker['speed'] * 2)
            is_critical = random.randint(1, 100) <= critical_chance
            
            if is_critical:
                damage = int(base_damage * 1.5)
                return damage, True
            else:
                return base_damage, False
        
        # Helper function to update character after battle
        def update_character_after_battle(character, won, opponent_level):
            # Update character stats after battle and save to CSV
            # Restore health
            character['health'] = character['max_health']
            
            # Award experience based on battle outcome and opponent level
            if won:
                exp_gain = 20 * opponent_level
                print(f"{character['name']} gained {exp_gain} experience!")
                character['experience'] += exp_gain
                
                # Level up if enough experience
                while character['experience'] >= character['level'] * 100:
                    character['experience'] -= character['level'] * 100
                    character['level'] += 1
                    character['max_health'] += 10
                    character['health'] = character['max_health']
                    character['strength'] += 3
                    character['defense'] += 2
                    character['speed'] += 2
                    
                    print(f"\n{character['name']} leveled up to level {character['level']}!")
                    print("All stats increased!")
                    
                    # Add new ability at certain levels
                    if character['level'] == 3 and character['class'] == 'Warrior':
                        character['abilities'].append("Shield Bash")
                        print(f"{character['name']} learned Shield Bash!")
                    elif character['level'] == 3 and character['class'] == 'Mage':
                        character['abilities'].append("Ice Shard")
                        print(f"{character['name']} learned Ice Shard!")
                    elif character['level'] == 3 and character['class'] == 'Rogue':
                        character['abilities'].append("Shadow Step")
                        print(f"{character['name']} learned Shadow Step!")
            
            # Update character in CSV by replacing the entire file
            characters = load_characters_from_csv()
            for i, char in enumerate(characters):
                if char['name'] == character['name']:
                    characters[i] = character
                    break
            
            # Create new CSV with updated characters
            with open("characters_temp.csv", mode='w', newline='') as file:
                import csv
                fieldnames = ['name', 'class', 'level', 'experience', 'health', 'max_health', 
                             'strength', 'defense', 'speed', 'abilities']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                
                for char in characters:
                    char_copy = char.copy()
                    char_copy['abilities'] = ','.join(char_copy['abilities'])
                    writer.writerow(char_copy)
            
            # Replace original file with updated file
            os.replace("characters_temp.csv", "characters.csv")
        
        # Helper function for using abilities
        def use_ability(character, opponent):
            # Use a special ability and return the damage dealt.
            clear_screen()
            print(f"\n{character['name']}'s Abilities:")
            
            for i, ability in enumerate(character['abilities'], 1):
                print(f"{i}. {ability}")
            
            try:
                choice = int(input("\nChoose an ability (or 0 to cancel): "))
                if choice == 0:
                    return 0
                
                ability_index = choice - 1
                if 0 <= ability_index < len(character['abilities']):
                    ability = character['abilities'][ability_index]
                    
                    # Apply ability effects
                    base_damage = max(1, character['strength'] - opponent['defense'] // 2)
                    
                    if ability == "Power Strike":
                        damage = int(base_damage * 1.7)
                        print(f"\n{character['name']} uses Power Strike for {damage} damage!")
                        return damage
                    elif ability == "Shield Bash":
                        damage = int(base_damage * 1.2)
                        print(f"\n{character['name']} uses Shield Bash for {damage} damage!")
                        print(f"{opponent['name']} is stunned and loses their next turn!")
                        opponent['stunned'] = True
                        return damage
                    elif ability == "Fireball":
                        damage = int(base_damage * 2.0)
                        print(f"\n{character['name']} casts Fireball for {damage} damage!")
                        return damage
                    elif ability == "Ice Shard":
                        damage = int(base_damage * 1.5)
                        print(f"\n{character['name']} casts Ice Shard for {damage} damage!")
                        print(f"{opponent['name']}'s speed is reduced!")
                        opponent['speed'] = max(1, opponent['speed'] - 3)
                        return damage
                    elif ability == "Backstab":
                        damage = int(base_damage * 2.2)
                        print(f"\n{character['name']} performs Backstab for {damage} damage!")
                        return damage
                    elif ability == "Shadow Step":
                        damage = int(base_damage * 1.3)
                        print(f"\n{character['name']} uses Shadow Step for {damage} damage!")
                        print(f"{character['name']}'s speed increases temporarily!")
                        character['speed'] += 5  # Temporary speed boost
                        return damage
                    else:
                        print(f"Unknown ability: {ability}")
                        return 0
                else:
                    print("Invalid ability selection!")
                    return 0
            except ValueError:
                print("Please enter a valid number!")
                return 0
        
        # Start battle sequence
        clear_screen()
        print("\n" + "="*50)
        print("BATTLE SYSTEM".center(50))
        print("="*50)
        
        characters = load_characters_from_csv()
        
        if len(characters) < 2:
            print("You need at least 2 characters to battle!")
            pause()
            return
        
        # Select characters for battle
        print("\nSelect first character:")
        for i, character in enumerate(characters, 1):
            print(f"{i}. {character['name']} (Lvl {character['level']} {character['class']})")
        
        try:
            first_char_idx = int(input("\nEnter character number: ")) - 1
            if not (0 <= first_char_idx < len(characters)):
                print("Invalid character selection!")
                pause()
                return
            
            first_char = characters[first_char_idx]
            
            print("\nSelect second character:")
            for i, character in enumerate(characters, 1):
                if i - 1 != first_char_idx:  # Don't show the already selected character
                    print(f"{i}. {character['name']} (Lvl {character['level']} {character['class']})")
            
            second_char_idx = int(input("\nEnter character number: ")) - 1
            if not (0 <= second_char_idx < len(characters)) or second_char_idx == first_char_idx:
                print("Invalid character selection!")
                pause()
                return
            
            second_char = characters[second_char_idx]
            
            # Create battle copies to avoid modifying originals until battle is complete
            char1 = first_char.copy()
            char2 = second_char.copy()
            
            # Add battle-specific flags
            char1['stunned'] = False
            char2['stunned'] = False
            
            # Battle loop
            clear_screen()
            print("\n" + "="*50)
            print(f"BATTLE: {char1['name']} vs {char2['name']}".center(50))
            print("="*50)
            
            # Determine who goes first based on speed
            first_attacker = char1 if char1['speed'] >= char2['speed'] else char2
            second_attacker = char2 if first_attacker == char1 else char1
            
            print(f"\n{first_attacker['name']} moves first due to higher speed!")
            time.sleep(1.5)
            
            turn = 1
            while char1['health'] > 0 and char2['health'] > 0:
                print(f"\n--- Turn {turn} ---")
                print(f"{char1['name']}: {char1['health']}/{char1['max_health']} HP")
                print(f"{char2['name']}: {char2['health']}/{char2['max_health']} HP")
                
                # Process first attacker's turn
                current = first_attacker
                target = second_attacker
                
                if current['stunned']:
                    print(f"\n{current['name']} is stunned and cannot move!")
                    current['stunned'] = False
                else:
                    print(f"\n{current['name']}'s turn!")
                    print("1. Basic Attack")
                    print("2. Use Ability")
                    
                    try:
                        action = input("Choose action (1-2): ")
                        
                        if action == '1':  # Basic attack
                            damage, critical = calculate_damage(current, target)
                            crit_text = " (CRITICAL HIT!)" if critical else ""
                            print(f"\n{current['name']} attacks for {damage} damage{crit_text}!")
                            target['health'] = max(0, target['health'] - damage)
                        elif action == '2':  # Use ability
                            damage = use_ability(current, target)
                            if damage > 0:
                                target['health'] = max(0, target['health'] - damage)
                        else:
                            print("Invalid action! Performing basic attack instead.")
                            damage, critical = calculate_damage(current, target)
                            print(f"\n{current['name']} attacks for {damage} damage!")
                            target['health'] = max(0, target['health'] - damage)
                    except ValueError:
                        print("Invalid input! Performing basic attack instead.")
                        damage, critical = calculate_damage(current, target)
                        print(f"\n{current['name']} attacks for {damage} damage!")
                        target['health'] = max(0, target['health'] - damage)
                
                # Check if battle is over
                if target['health'] <= 0:
                    print(f"\n{target['name']} has been defeated!")
                    print(f"\n{current['name']} wins the battle!")
                    
                    # Update character stats after battle
                    update_character_after_battle(first_char, first_char == current, second_char['level'])
                    update_character_after_battle(second_char, second_char == current, first_char['level'])
                    
                    pause()
                    return
                
                time.sleep(1)
                
                # Process second attacker's turn
                current = second_attacker
                target = first_attacker
                
                if current['stunned']:
                    print(f"\n{current['name']} is stunned and cannot move!")
                    current['stunned'] = False
                else:
                    print(f"\n{current['name']}'s turn!")
                    print("1. Basic Attack")
                    print("2. Use Ability")
                    
                    try:
                        action = input("Choose action (1-2): ")
                        
                        if action == '1':  # Basic attack
                            damage, critical = calculate_damage(current, target)
                            crit_text = " (CRITICAL HIT!)" if critical else ""
                            print(f"\n{current['name']} attacks for {damage} damage{crit_text}!")
                            target['health'] = max(0, target['health'] - damage)
                        elif action == '2':  # Use ability
                            damage = use_ability(current, target)
                            if damage > 0:
                                target['health'] = max(0, target['health'] - damage)
                        else:
                            print("Invalid action! Performing basic attack instead.")
                            damage, critical = calculate_damage(current, target)
                            print(f"\n{current['name']} attacks for {damage} damage!")
                            target['health'] = max(0, target['health'] - damage)
                    except ValueError:
                        print("Invalid input! Performing basic attack instead.")
                        damage, critical = calculate_damage(current, target)
                        print(f"\n{current['name']} attacks for {damage} damage!")
                        target['health'] = max(0, target['health'] - damage)
                
                # Check if battle is over
                if target['health'] <= 0:
                    print(f"\n{target['name']} has been defeated!")
                    print(f"\n{current['name']} wins the battle!")
                    
                    # Update character stats after battle
                    update_character_after_battle(first_char, first_char == current, second_char['level'])
                    update_character_after_battle(second_char, second_char == current, first_char['level'])
                    
                    pause()
                    return
                
                turn += 1
                time.sleep(1)
        
        except ValueError:
            print("Please enter valid numbers!")
            pause()
            return
    
    # Return a dictionary of functions
    return {
        'battle_characters': battle_characters
    }