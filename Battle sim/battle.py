# Avery bowman

import time
import random
from utils import clear_screen, print_header

def battle_characters(char1, char2):
    # Conduct a battle between two characters and return the winner
    # Create copies of characters to avoid modifying originals during battle
    char1_battle = char1
    char2_battle = char2
    
    # Reset health at beginning of battle
    original_health1 = char1_battle.health
    original_health2 = char2_battle.health
    char1_battle.heal()
    char2_battle.heal()
    
    # Determine who goes first based on speed
    if char2_battle.speed > char1_battle.speed:
        char1_battle, char2_battle = char2_battle, char1_battle
    elif char1_battle.speed == char2_battle.speed:
        # If speeds are equal, choose randomly
        if random.choice([True, False]):
            char1_battle, char2_battle = char2_battle, char1_battle
    
    # Reference to original characters (not swapped)
    char1_orig = char1
    char2_orig = char2
    
    clear_screen()
    print_header("BATTLE")
    print(f"{char1_battle.name} vs {char2_battle.name}")
    print("\nBattle starting in 3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("FIGHT!")
    time.sleep(1)
    
    round_num = 1
    
    # Battle loop
    while not char1_battle.is_defeated() and not char2_battle.is_defeated():
        clear_screen()
        print_header(f"BATTLE - ROUND {round_num}")
        print(f"{char1_battle.name}: {char1_battle.health}/{char1_battle.max_health} HP")
        print(f"{char2_battle.name}: {char2_battle.health}/{char2_battle.max_health} HP")
        print("\n")
        
        # First character attacks
        damage = char1_battle.attack(char2_battle)
        print(f"{char1_battle.name} attacks {char2_battle.name} for {damage} damage!")
        
        # Check if second character is defeated
        if char2_battle.is_defeated():
            print(f"{char2_battle.name} has been defeated!")
            winner = char1_battle
            loser = char2_battle
            break
        
        time.sleep(1.5)
        
        # Second character attacks
        damage = char2_battle.attack(char1_battle)
        print(f"{char2_battle.name} attacks {char1_battle.name} for {damage} damage!")
        
        # Check if first character is defeated
        if char1_battle.is_defeated():
            print(f"{char1_battle.name} has been defeated!")
            winner = char2_battle
            loser = char1_battle
            break
        
        time.sleep(1.5)
        round_num += 1
    
    # Determine experience gain
    # Level difference affects exp gain
    level_diff = loser.level - winner.level
    base_exp = 50
    
    # More exp for defeating higher level characters
    if level_diff > 0:
        exp_gain = base_exp + (20 * level_diff)
    else:
        # Less exp for defeating lower level characters
        exp_gain = max(10, base_exp + (10 * level_diff))
    
    # Award experience to winner
    print(f"\n{winner.name} wins and gains {exp_gain} experience!")
    winner.gain_experience(exp_gain)
    
    # Restore original health values after battle
    if char1_orig == char1_battle:
        char1_orig.health = char1_battle.health
        char2_orig.health = char2_battle.health
    else:
        char1_orig.health = char2_battle.health
        char2_orig.health = char1_battle.health
        
    # Also give a small amount of exp to loser
    consolation_exp = max(5, int(exp_gain * 0.2))
    print(f"{loser.name} receives {consolation_exp} experience for participating.")
    loser.gain_experience(consolation_exp)
    
    return winner