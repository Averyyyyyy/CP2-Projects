# Avery bowman

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg
import os
import io

def create_stat_radar(character):
    # Create a radar chart for character stats
    attributes = ['Health', 'Strength', 'Defense', 'Speed']
    # Scale values to be comparable
    values = [
        character.health / 10,  # Scale down health
        character.strength,
        character.defense,
        character.speed
    ]
    
    # Calculate angles for radar chart
    angles = np.linspace(0, 2*np.pi, len(attributes), endpoint=False).tolist()
    
    # Close the polygon by repeating the first value
    values.append(values[0])
    angles.append(angles[0])
    attributes.append(attributes[0])
    
    # Create the plot
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, polar=True)
    
    # Plot the character stats
    ax.plot(angles, values, 'o-', linewidth=2, label=character.name)
    ax.fill(angles, values, alpha=0.25)
    
    # Set the labels
    ax.set_thetagrids(np.degrees(angles[:-1]), attributes[:-1])
    
    # Add character name and level as title
    plt.title(f"{character.name} (Level {character.level}) - Stats Radar", size=14)
    
    # Save the radar chart
    chart_path = os.path.join('charts', f"{character.name}_radar.png")
    os.makedirs('charts', exist_ok=True)
    plt.savefig(chart_path)
    
    plt.close()
    return chart_path

def create_stat_bars(character):
    # Create a bar chart for character stats
    attributes = ['Health/10', 'Strength', 'Defense', 'Speed']
    values = [
        character.health / 10,  # Scale down health to make bar chart more readable
        character.strength,
        character.defense,
        character.speed
    ]
    
    # Create the plot
    plt.figure(figsize=(10, 6))
    bars = plt.bar(attributes, values, color=['red', 'green', 'blue', 'orange'])
    
    # Add values above bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                 f'{height:.1f}', ha='center', va='bottom')
    
    # Add character name as title
    plt.title(f"{character.name} (Level {character.level}) - Stats", size=14)
    plt.ylim(0, max(values) * 1.2)  # Add 20% space above highest bar
    
    # Save the bar chart
    chart_path = os.path.join('charts', f"{character.name}_bars.png")
    os.makedirs('charts', exist_ok=True)
    plt.savefig(chart_path)
    
    plt.close()
    return chart_path

def create_level_progression(character):
    # Create a line chart showing potential level progression
    current_level = character.level
    exp_to_next = character.exp_to_level
    current_exp = character.experience
    
    # Project future levels
    levels = list(range(current_level, current_level + 5))
    exp_needed = [exp_to_next]
    
    # Calculate exp needed for future levels
    temp_exp = exp_to_next
    for _ in range(3):
        temp_exp = int(temp_exp * 1.5)
        exp_needed.append(temp_exp)
    
    # Create the plot
    plt.figure(figsize=(10, 6))
    
    # Add progress bar for current level
    plt.bar(['Current Level'], [exp_to_next], color='lightgray')
    plt.bar(['Current Level'], [current_exp], color='green')
    
    # Add text to show progress
    plt.text(0, current_exp/2, f"{current_exp}/{exp_to_next}", 
             ha='center', va='center', color='black', fontweight='bold')
    
    # Add projected exp for future levels
    plt.bar(range(1, len(exp_needed)), exp_needed[1:], color='lightgray')
    
    # Set labels
    plt.xticks(range(len(levels)), [f"Lv {level}" for level in levels])
    plt.title(f"{character.name}'s Level Progression", size=14)
    plt.ylabel('Experience Points')
    
    # Save the chart
    chart_path = os.path.join('charts', f"{character.name}_progression.png")
    os.makedirs('charts', exist_ok=True)
    plt.savefig(chart_path)
    
    plt.close()
    return chart_path

def create_character_comparison(characters):
    # Create a grouped bar chart to compare characters
    if len(characters) < 2:
        return None
    
    # Limit to 5 characters for readability
    if len(characters) > 5:
        characters = characters[:5]
    
    # Get character names and stats
    names = [c.name for c in characters]
    health = [c.health / 10 for c in characters]  # Scale down health
    strength = [c.strength for c in characters]
    defense = [c.defense for c in characters]
    speed = [c.speed for c in characters]
    
    # Set width of bar and positions
    bar_width = 0.2
    r1 = np.arange(len(names))
    r2 = [x + bar_width for x in r1]
    r3 = [x + bar_width for x in r2]
    r4 = [x + bar_width for x in r3]
    
    # Create the plot
    plt.figure(figsize=(12, 8))
    plt.bar(r1, health, width=bar_width, label='Health/10', color='red')
    plt.bar(r2, strength, width=bar_width, label='Strength', color='green')
    plt.bar(r3, defense, width=bar_width, label='Defense', color='blue')
    plt.bar(r4, speed, width=bar_width, label='Speed', color='orange')
    
    # Add labels and legend
    plt.xlabel('Characters')
    plt.ylabel('Stat Values')
    plt.title('Character Comparison')
    plt.xticks([r + bar_width*1.5 for r in range(len(names))], names)
    plt.legend()
    
    # Save the chart
    chart_path = os.path.join('charts', 'character_comparison.png')
    os.makedirs('charts', exist_ok=True)
    plt.savefig(chart_path)
    
    plt.close()
    return chart_path

def create_health_histogram(characters):
    # Create a histogram of character health values
    if not characters:
        return None
    
    health_values = [c.health for c in characters]
    
    plt.figure(figsize=(10, 6))
    plt.hist(health_values, bins=10, alpha=0.7, color='red', edgecolor='black')
    
    plt.title('Distribution of Character Health')
    plt.xlabel('Health Points')
    plt.ylabel('Number of Characters')
    plt.grid(True, alpha=0.3)
    
    # Add mean and median lines
    mean_health = np.mean(health_values)
    median_health = np.median(health_values)
    
    plt.axvline(mean_health, color='green', linestyle='dashed', linewidth=2, label=f'Mean: {mean_health:.1f}')
    plt.axvline(median_health, color='blue', linestyle='dashed', linewidth=2, label=f'Median: {median_health:.1f}')
    plt.legend()
    
    # Save the chart
    chart_path = os.path.join('charts', 'health_histogram.png')
    os.makedirs('charts', exist_ok=True)
    plt.savefig(chart_path)
    
    plt.close()
    return chart_path

def create_battle_simulation_chart(character1, character2):
    # Simulate a battle and visualize the results
    # Copy stats (without modifying original characters)
    char1_health = character1.max_health
    char2_health = character2.max_health
    
    # Calculate damage per round (simplified)
    char1_damage = max(1, character1.strength - character2.defense // 2)
    char2_damage = max(1, character2.strength - character1.defense // 2)
    
    # Calculate rounds to defeat each character
    rounds_to_defeat_char2 = char2_health // char1_damage
    if char2_health % char1_damage > 0:
        rounds_to_defeat_char2 += 1
        
    rounds_to_defeat_char1 = char1_health // char2_damage
    if char1_health % char2_damage > 0:
        rounds_to_defeat_char1 += 1
    
    # Calculate who goes first based on speed
    char1_first = character1.speed >= character2.speed
    
    # Calculate maximum rounds
    max_rounds = max(rounds_to_defeat_char1, rounds_to_defeat_char2) + 1
    
    # Create arrays to track health over time
    char1_health_over_time = [char1_health]
    char2_health_over_time = [char2_health]
    
    # Simulate battle
    for i in range(1, max_rounds + 1):
        # First character attacks
        if char1_first:
            char2_health -= char1_damage
            char2_health = max(0, char2_health)
            char2_health_over_time.append(char2_health)
            
            # Second character attacks if still alive
            if char2_health > 0:
                char1_health -= char2_damage
                char1_health = max(0, char1_health)
            char1_health_over_time.append(char1_health)
        else:
            char1_health -= char2_damage
            char1_health = max(0, char1_health)
            char1_health_over_time.append(char1_health)
            
            # Second character attacks if still alive
            if char1_health > 0:
                char2_health -= char1_damage
                char2_health = max(0, char2_health)
            char2_health_over_time.append(char2_health)
            
        # Check if battle is over
        if char1_health <= 0 or char2_health <= 0:
            break
    
    # Create the plot
    plt.figure(figsize=(12, 8))
    rounds = range(len(char1_health_over_time))
    plt.plot(rounds, char1_health_over_time, 'b-', linewidth=2, label=character1.name)
    plt.plot(rounds, char2_health_over_time, 'r-', linewidth=2, label=character2.name)
    
    # Add labels and legend
    plt.xlabel('Round')
    plt.ylabel('Health')
    plt.title(f'Battle Simulation: {character1.name} vs {character2.name}')
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    # Add victor annotation
    if char1_health <= 0 and char2_health <= 0:
        plt.annotate('Draw!', xy=(0.5, 0.5), xycoords='axes fraction', 
                    fontsize=14, ha='center')
    elif char1_health <= 0:
        plt.annotate(f'{character2.name} wins!', xy=(0.5, 0.5), xycoords='axes fraction', 
                    fontsize=14, ha='center')
    elif char2_health <= 0:
        plt.annotate(f'{character1.name} wins!', xy=(0.5, 0.5), xycoords='axes fraction', 
                    fontsize=14, ha='center')
    
    # Save the chart
    chart_path = os.path.join('charts', f'battle_sim_{character1.name}_vs_{character2.name}.png')
    os.makedirs('charts', exist_ok=True)
    plt.savefig(chart_path)
    
    plt.close()
    return chart_path