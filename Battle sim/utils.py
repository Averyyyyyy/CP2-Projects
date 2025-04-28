# utils.py
import matplotlib.pyplot as plt
import numpy as np

def display_character(char):
    print(f"\nName: {char['name']}")
    print(f"Level: {char['level']} | XP: {char['xp']}")
    print(f"Health: {char['health']}")
    print(f"Strength: {char['strength']}")
    print(f"Defense: {char['defense']}")
    print(f"Speed: {char['speed']}")
    if 'backstory' in char:
        print(f"Backstory: {char['backstory']}")
    if 'skills' in char and char['skills']:
        print(f"Skills: {', '.join(char['skills'])}")

def plot_character_stats(char):
    stats = ['Health', 'Strength', 'Defense', 'Speed']
    values = [char['health'], char['strength'], char['defense'], char['speed']]
    plt.bar(stats, values, color='skyblue')
    plt.title(f"{char['name']}'s Stats")
    plt.ylabel('Points')
    plt.savefig(f"{char['name']}_stats.png")  # save as image (bonus feature)
    plt.show()
