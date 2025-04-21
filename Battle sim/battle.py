import random
from file import characters

def battle_menu():
    def battle(c1, c2):
        print(f"\nBattle Start: {c1['name']} vs {c2['name']}")
        char1 = c1.copy()
        char2 = c2.copy()

        def attack(attacker, defender):
            damage = max(0, attacker['strength'] - defender['defense'] + random.randint(-2, 2))
            defender['health'] -= damage
            print(f"{attacker['name']} attacks {defender['name']} for {damage} damage")

        while char1['health'] > 0 and char2['health'] > 0:
            if char1['speed'] >= char2['speed']:
                attack(char1, char2)
                if char2['health'] <= 0:
                    break
                attack(char2, char1)
            else:
                attack(char2, char1)
                if char1['health'] <= 0:
                    break
                attack(char1, char2)

        winner = c1 if char1['health'] > 0 else c2
        print(f"{winner['name']} wins and gains 50 XP")
        winner['xp'] += 50
        if winner['xp'] >= winner['level'] * 100:
            winner['level'] += 1
            winner['xp'] = 0
            winner['health'] += 10
            winner['strength'] += 2
            winner['defense'] += 2
            winner['speed'] += 1
            print(f"{winner['name']} leveled up to level {winner['level']}")

    if len(characters) < 2:
        print("You need at least 2 characters to battle.")
        return

    print("\nAvailable characters:")
    for name in characters:
        print(name)

    name1 = input("Enter name of your first character: ")
    name2 = input("Enter name of your second character: ")

    if name1 not in characters or name2 not in characters:
        print("Character is not found.")
        return
    if name1 == name2:
        print("You can't battle the same character.")
        return

    battle(characters[name1], characters[name2])