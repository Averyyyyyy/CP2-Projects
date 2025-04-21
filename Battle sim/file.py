import csv
import os

characters = {}
CHARACTER_FILE = 'characters.csv'

def save_characters():
    with open(CHARACTER_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Health', 'Strength', 'Defense', 'Speed', 'Level', 'XP'])
        for char in characters.values():
            writer.writerow([char['name'], char['health'], char['strength'], char['defense'],
                             char['speed'], char['level'], char['xp']])

def load_characters():
    if not os.path.exists(CHARACTER_FILE):
        return
    with open(CHARACTER_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            characters[row['Name']] = {
                'name': row['Name'],
                'health': int(row['Health']),
                'strength': int(row['Strength']),
                'defense': int(row['Defense']),
                'speed': int(row['Speed']),
                'level': int(row['Level']),
                'xp': int(row['XP'])
            }
