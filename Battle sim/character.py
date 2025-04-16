# Avery bowman, charcter.py

class Character:
    # Class representing an RPG character with attributes and leveling system
    
    def __init__(self, name, health, strength, defense, speed, level=1, experience=0):
        self.name = name
        self.health = max(1, min(200, health))  # Cap health between 1-200
        self.max_health = self.health
        self.strength = max(1, min(30, strength))  # Cap strength between 1-30
        self.defense = max(0, min(20, defense))  # Cap defense between 0-20
        self.speed = max(1, min(20, speed))  # Cap speed between 1-20
        self.level = level
        self.experience = experience
        self.exp_to_level = 100  # Base XP needed for leveling up
    
    def gain_experience(self, amount):
        # Add experience points and level up if threshold is reached
        self.experience += amount
        
        # Check if character can level up
        while self.experience >= self.exp_to_level:
            self.level_up()
    
    def level_up(self):
        # Increase character stats when leveling up
        self.level += 1
        self.experience -= self.exp_to_level
        
        # Increase exp_to_level for next level
        self.exp_to_level = int(self.exp_to_level * 1.5)
        
        # Improve stats
        self.max_health += 20
        self.health = self.max_health  # Heal to full when leveling up
        self.strength += 2
        self.defense += 1
        self.speed += 1
        
        print(f"\n🎉 {self.name} leveled up to level {self.level}!")
        print(f"Health: {self.max_health} | Strength: {self.strength} | Defense: {self.defense} | Speed: {self.speed}")
    
    def heal(self, amount=None):
        # Restore health, optionally by a specific amount
        if amount:
            self.health = min(self.max_health, self.health + amount)
        else:
            self.health = self.max_health
    
    def is_defeated(self):
        # Check if character has been defeated (health <= 0)
        return self.health <= 0
    
    def attack(self, target):
        # Attack another character and return damage dealt
        # Base damage calculation
        base_damage = max(0, self.strength - target.defense // 2)
        
        # Minimum damage is 1 if characters aren't too mismatched
        damage = max(1, base_damage)
        
        # Apply damage to target
        target.health -= damage
        target.health = max(0, target.health)  # Prevent negative health
        
        return damage
    
    def __str__(self):
        # String representation of the character for display
        return (f"{self.name} (Level {self.level}) - "
                f"HP: {self.health}/{self.max_health}, "
                f"STR: {self.strength}, DEF: {self.defense}, SPD: {self.speed}, "
                f"EXP: {self.experience}/{self.exp_to_level}")