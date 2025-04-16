# Avery bowman

import os
import csv
import time
import matplotlib.pyplot as plt
from character import Character
from battle import battle_characters
from utils import clear_screen, print_header
from visualization import (create_stat_radar, create_stat_bars, create_character_comparison, 
                          create_health_histogram, create_battle_simulation_chart,
                          create_level_progression)
from analysis import (load_characters_to_dataframe, get_character_stats, get_character_ranking,
                     find_best_matchups, analyze_stat_correlation, export_character_stats)
from generator import (generate_random_name, generate_random_backstory, 
                      generate_random_character, generate_random_battle_scenario,
                      generate_random_item)

def main():
    characters = []
    
    # Create charts directory if it doesn't exist
    os.makedirs('charts', exist_ok=True)
    
    # Load existing characters at startup
    if os.path.exists('characters.csv'):
        characters = load_characters()
    
    def display_menu():
        """Inner function to display the main menu"""
        print_header("RPG CHARACTER MANAGER")
        print("1. Create New Character")
        print("2. View Characters")
        print("3. Battle Characters")
        print("4. Character Visualization")
        print("5. Data Analysis")
        print("6. Random Generation")
        print("7. Save & Exit")
        return input("Select an option (1-7): ")
    
    def create_character():
        """Inner function to handle character creation"""
        clear_screen()
        print_header("CHARACTER CREATION")
        
        print("1. Create Character Manually")
        print("2. Generate Random Character")
        choice = input("Select an option (1-2): ")
        
        if choice == '2':
            # Generate random character
            use_random_name = input("Generate a random name? (y/n): ").lower() == 'y'
            name = None if use_random_name else input("Enter character name: ")
            
            new_character = generate_random_character(name)
            print(f"\nCharacter '{new_character.name}' created successfully!")
            print(f"Backstory: {new_character.backstory}")
            characters.append(new_character)
            save_characters(characters)
            input("\nPress Enter to continue...")
            return
            
        # Manual character creation
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
        
        # Add backstory option
        add_backstory = input("Add a backstory? (y/n): ").lower()
        if add_backstory == 'y':
            print("1. Enter custom backstory")
            print("2. Generate random backstory")
            backstory_choice = input("Select an option (1-2): ")
            
            if backstory_choice == '1':
                backstory = input("Enter character backstory: ")
                new_character.backstory = backstory
            elif backstory_choice == '2':
                class_options = ['Warrior', 'Mage', 'Rogue', 'Paladin', 'Ranger', 'Cleric', 'Druid', 'Monk', 'Bard']
                print("Character class options:")
                for i, c_class in enumerate(class_options, 1):
                    print(f"{i}. {c_class}")
                
                try:
                    class_idx = int(input("Select a class (or 0 for random): ")) - 1
                    if 0 <= class_idx < len(class_options):
                        character_class = class_options[class_idx]
                    else:
                        character_class = None
                except ValueError:
                    character_class = None
                
                new_character.backstory = generate_random_backstory(name, character_class)
                print(f"\nBackstory: {new_character.backstory}")
        
        characters.append(new_character)
        save_characters(characters)
        print(f"\nCharacter '{name}' created successfully!")
        input("\nPress Enter to continue...")
    
    def view_characters():
        """Inner function to display all characters"""
        while True:
            clear_screen()
            print_header("CHARACTER ROSTER")
            
            if not characters:
                print("No characters found.")
                input("\nPress Enter to continue...")
                return
            
            for i, character in enumerate(characters, 1):
                print(f"{i}. {character.name} (Level {character.level})")
            
            print("\nOptions:")
            print("1. View character details")
            print("2. Return to main menu")
            
            choice = input("\nSelect an option (1-2): ")
            
            if choice == '1':
                try:
                    char_idx = int(input("Enter character number to view: ")) - 1
                    if 0 <= char_idx < len(characters):
                        clear_screen()
                        selected_char = characters[char_idx]
                        print_header(f"CHARACTER: {selected_char.name}")
                        print(f"{selected_char}")
                        
                        # Show backstory if available
                        if hasattr(selected_char, 'backstory') and selected_char.backstory:
                            print(f"\nBackstory:\n{selected_char.backstory}")
                        
                        print("\nOptions:")
                        print("1. Create stat visualization")
                        print("2. Return to character list")
                        
                        viz_choice = input("\nSelect an option (1-2): ")
                        if viz_choice == '1':
                            # Create and show visualization
                            print("\nGenerating character visualizations...")
                            radar_path = create_stat_radar(selected_char)
                            bar_path = create_stat_bars(selected_char)
                            prog_path = create_level_progression(selected_char)
                            
                            print(f"\nVisualizations saved to:\n- {radar_path}\n- {bar_path}\n- {prog_path}")
                            input("\nPress Enter to continue...")
                    else:
                        print("Invalid character number!")
                        time.sleep(1.5)
                except ValueError:
                    print("Please enter a valid number!")
                    time.sleep(1.5)
            elif choice == '2':
                return
            else:
                print("Invalid option!")
                time.sleep(1)
    
    def battle_menu():
        """Inner function to handle character battles"""
        if len(characters) < 2:
            clear_screen()
            print("You need at least 2 characters to battle!")
            time.sleep(2)
            return
        
        clear_screen()
        print_header("BATTLE MODE")
        
        print("1. Select characters manually")
        print("2. Find balanced matchups")
        print("3. Battle simulation preview")
        print("4. Return to main menu")
        
        battle_choice = input("\nSelect an option (1-4): ")
        
        if battle_choice == '1':
            # Manual character selection
            clear_screen()
            print_header("SELECT BATTLE CHARACTERS")
            
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
                    # Option to generate a battle scenario
                    if input("Generate a random battle scenario? (y/n): ").lower() == 'y':
                        scenario = generate_random_battle_scenario()
                        print("\nBattle Scenario:")
                        print(scenario)
                        print("\n")
                        time.sleep(2)
                    
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
                
        elif battle_choice == '2':
            # Find balanced matchups
            clear_screen()
            print_header("BALANCED MATCHUPS")
            
            matchups = find_best_matchups(characters)
            if not matchups:
                print("Couldn't determine matchups!")
                time.sleep(2)
                return
                
            print("Most balanced matchups (lowest power difference):")
            for i, matchup in enumerate(matchups[:5], 1):
                char1 = matchup['character1']
                char2 = matchup['character2']
                diff = matchup['power_diff_pct']
                print(f"{i}. {char1.name} (Lv.{char1.level}) vs {char2.name} (Lv.{char2.level}) - {diff:.1f}% difference")
            
            try:
                match_choice = int(input("\nSelect a matchup to battle (or 0 to return): "))
                if 1 <= match_choice <= min(5, len(matchups)):
                    selected = matchups[match_choice-1]
                    char1 = selected['character1']
                    char2 = selected['character2']
                    
                    # Option to generate a battle scenario
                    if input("Generate a random battle scenario? (y/n): ").lower() == 'y':
                        scenario = generate_random_battle_scenario()
                        print("\nBattle Scenario:")
                        print(scenario)
                        print("\n")
                        time.sleep(2)
                    
                    winner = battle_characters(char1, char2)
                    save_characters(characters)
                    input("\nPress Enter to continue...")
            except ValueError:
                print("Invalid input!")
                time.sleep(1.5)
                
        elif battle_choice == '3':
            # Battle simulation (preview only)
            clear_screen()
            print_header("BATTLE SIMULATION")
            
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
                    print("\nGenerating battle simulation chart...")
                    char1 = characters[choice1]
                    char2 = characters[choice2]
                    
                    chart_path = create_battle_simulation_chart(char1, char2)
                    print(f"\nBattle simulation chart saved to: {chart_path}")
                    
                    # Ask if they want to proceed with actual battle
                    if input("\nProceed with actual battle? (y/n): ").lower() == 'y':
                        winner = battle_characters(char1, char2)
                        save_characters(characters)
                    
                    input("\nPress Enter to continue...")
                else:
                    print("Invalid character selection!")
                    time.sleep(2)
            except ValueError:
                print("Invalid input! Please enter a number.")
                time.sleep(2)
    
    def visualization_menu():
        """Inner function for visualization options"""
        while True:
            clear_screen()
            print_header("VISUALIZATION OPTIONS")
            
            print("1. Character Stat Comparison")
            print("2. Health Distribution Histogram")
            print("3. Battle Simulation Chart")
            print("4. Return to Main Menu")
            
            choice = input("\nSelect an option (1-4): ")
            
            if choice == '1':
                if len(characters) < 2:
                    print("You need at least 2 characters for comparison!")
                    time.sleep(2)
                    continue
                
                print("\nGenerating character comparison chart...")
                chart_path = create_character_comparison(characters)
                print(f"\nChart saved to: {chart_path}")
                input("\nPress Enter to continue...")
                
            elif choice == '2':
                if not characters:
                    print("No characters available for analysis!")
                    time.sleep(2)
                    continue
                
                print("\nGenerating health distribution histogram...")
                chart_path = create_health_histogram(characters)
                print(f"\nChart saved to: {chart_path}")
                input("\nPress Enter to continue...")
                
            elif choice == '3':
                if len(characters) < 2:
                    print("You need at least 2 characters for battle simulation!")
                    time.sleep(2)
                    continue
                
                # Select characters for battle simulation
                clear_screen()
                print_header("BATTLE SIMULATION")
                
                for i, character in enumerate(characters, 1):
                    print(f"{i}. {character.name} (Level {character.level})")
                
                try:
                    choice1 = int(input("\nSelect first character (number): ")) - 1
                    choice2 = int(input("Select second character (number): ")) - 1
                    
                    if choice1 == choice2 or not (0 <= choice1 < len(characters) and 0 <= choice2 < len(characters)):
                        print("Invalid selection!")
                        time.sleep(2)
                        continue
                    
                    print("\nGenerating battle simulation chart...")
                    chart_path = create_battle_simulation_chart(characters[choice1], characters[choice2])
                    print(f"\nChart saved to: {chart_path}")
                    input("\nPress Enter to continue...")
                except ValueError:
                    print("Invalid input!")
                    time.sleep(1.5)
                    
            elif choice == '4':
                return
            else:
                print("Invalid option!")
                time.sleep(1)
    
    def analysis_menu():
        """Inner function for data analysis options"""
        while True:
            clear_screen()
            print_header("DATA ANALYSIS")
            
            print("1. Character Statistics Summary")
            print("2. Character Rankings")
            print("3. Stat Correlation Analysis")
            print("4. Export Character Data to CSV")
            print("5. Return to Main Menu")
            
            choice = input("\nSelect an option (1-5): ")
            
            if choice == '1':
                if not characters:
                    print("No characters available for analysis!")
                    time.sleep(2)
                    continue
                
                clear_screen()
                print_header("CHARACTER STATISTICS")
                
                stats = get_character_stats(characters)
                if not stats:
                    print("No statistics available!")
                    input("\nPress Enter to continue...")
                    continue
                
                # Display stats
                for stat_name, values in stats.items():
                    print(f"\n{stat_name}:")
                    print(f"  Mean:   {values['mean']:.2f}")
                    print(f"  Median: {values['median']:.2f}")
                    print(f"  Min:    {values['min']:.2f}")
                    print(f"  Max:    {values['max']:.2f}")
                    print(f"  StdDev: {values['std']:.2f}")
                
                input("\nPress Enter to continue...")
                
            elif choice == '2':
                if not characters:
                    print("No characters available for ranking!")
                    time.sleep(2)
                    continue
                
                clear_screen()
                print_header("CHARACTER RANKINGS")
                
                rankings = get_character_ranking(characters)
                print("Characters ranked by overall power:\n")
                
                for i, (_, row) in enumerate(rankings.iterrows(), 1):
                    print(f"{i}. {row['Name']} (Level {row['Level']}) - Power Score: {row['Power_Score']:.1f}")
                    print(f"   HP: {row['Health']}, STR: {row['Strength']}, DEF: {row['Defense']}, SPD: {row['Speed']}")
                
                input("\nPress Enter to continue...")
                
            elif choice == '3':
                if len(characters) < 3:
                    print("Need at least 3 characters for correlation analysis!")
                    time.sleep(2)
                    continue
                
                clear_screen()
                print_header("STAT CORRELATION ANALYSIS")
                
                corr = analyze_stat_correlation(characters)
                if corr is None:
                    print("Correlation analysis not available!")
                    input("\nPress Enter to continue...")
                    continue
                
                # Display correlation matrix
                print("Correlation Matrix:\n")
                print(corr.round(2))
                
                # Explain strongest correlations
                print("\nStrongest correlations:")
                
                # Get upper triangle of correlation matrix
                upper = corr.where(np.triu(np.ones(corr.shape), k=1).astype(bool))
                
                # Find strongest positive and negative correlations
                strongest_pos = upper.max().max()
                strongest_neg = upper.min().min()
                
                # Find which pairs have these values
                for i, row in enumerate(upper.index):
                    for j, col in enumerate(upper.columns):
                        if i < j:  # Upper triangle only
                            if abs(upper.iloc[i, j]) > 0.5:  # Threshold for "strong"
                                print(f"- {row} and {col}: {upper.iloc[i, j]:.2f}")
                
                input("\nPress Enter to continue...")
                
            elif choice == '4':
                if not characters:
                    print("No characters available to export!")
                    time.sleep(2)
                    continue
                
                filename = input("Enter filename for export (default: character_stats.csv): ")
                if not filename:
                    filename = "character_stats.csv"
                
                if not filename.endswith('.csv'):
                    filename += '.csv'
                
                success = export_character_stats(characters, filename)
                if success:
                    print(f"\nCharacter data exported successfully to {filename}!")
                else:
                    print("\nError exporting character data!")
                
                input("\nPress Enter to continue...")
                
            elif choice == '5':
                return
            else:
                print("Invalid option!")
                time.sleep(1)
    
    def random_generation_menu():
        # Inner function for random generation features
        while True:
            clear_screen()
            print_header("RANDOM GENERATION")
            
            print("1. Generate Random Name")
            print("2. Generate Random Backstory")
            print("3. Generate Battle Scenario")
            print("4. Generate Magic Item")
            print("5. Return to Main Menu")
            
            choice = input("\nSelect an option (1-5): ")
            
            if choice == '1':
                clear_screen()
                print_header("RANDOM NAME GENERATOR")
                
                print("1. Any gender")