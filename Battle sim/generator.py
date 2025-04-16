# Avery bowman

from faker import Faker
import random
from character import Character

# Initialize Faker
fake = Faker()

def generate_random_name(gender=None):
    # Generate a fantasy-style name using Faker
    if gender == 'male':
        first_name = fake.first_name_male()
    elif gender == 'female':
        first_name = fake.first_name_female()
    else:
        first_name = fake.first_name()
    
    # Fantasy name suffixes and prefixes
    suffixes = ['ius', 'or', 'ion', 'eon', 'ian', 'wyn', 'wen', 'wyth', 'ith', 'alas', 'aran', 'thor', 'dor', 'dan']
    prefixes = ['El', 'Gal', 'Ar', 'Thal', 'Mal', 'Cal', 'Aer', 'Thaer', 'Kael', 'Dor', 'Fin', 'Thor', 'Ven', 'Zin']
    
    # Decide on name style (50% chance of fantasy style)
    if random.random() < 0.5:
        if random.random() < 0.5:
            # Use fantasy prefix with normal name
            name = random.choice(prefixes) + first_name
        else:
            # Use normal name with fantasy suffix
            name = first_name + random.choice(suffixes)
    else:
        # Use completely unique fantasy name
        name = random.choice(prefixes) + random.choice(suffixes).lower()
    
    return name

def generate_random_backstory(character_name, character_class=None):
    # Generate a random backstory for a character
    
    # Define possible classes if none provided
    if character_class is None:
        classes = ['Warrior', 'Mage', 'Rogue', 'Paladin', 'Ranger', 'Cleric', 'Druid', 'Monk', 'Bard']
        character_class = random.choice(classes)
    
    # Define possible origins
    origins = [
        'a small village in the mountains',
        'a bustling port city',
        'a secluded forest community',
        'the vast northern plains',
        'an underground dwarven city',
        'a nomadic desert tribe',
        'a prestigious academy',
        'the slums of a great city',
        'a merchant family always on the move',
        'a mysterious island'
    ]
    
    # Define possible motivations
    motivations = [
        'seek revenge for the destruction of their homeland',
        'restore their family\'s honor',
        'prove their worth to their skeptical mentors',
        'find a legendary artifact',
        'break a family curse',
        'discover the truth about their mysterious parentage',
        'protect the innocent from growing darkness',
        'attain mastery of their craft',
        'repay a life debt to a mysterious benefactor',
        'fulfill an ancient prophecy'
    ]
    
    # Define possible complications
    complications = [
        'but they are plagued by visions of a coming catastrophe',
        'but they suffer from a magical affliction that threatens their life',
        'but they are being pursued by agents of a powerful enemy',
        'though their greatest challenge is overcoming their own self-doubt',
        'despite being mistrusted due to their unusual abilities',
        'while struggling to control dangerous powers they don\'t fully understand',
        'though they must keep their true identity secret',
        'but they are bound by a magical oath that limits their actions',
        'although they have sworn never to use their most powerful abilities',
        'while searching for their long-lost sibling'
    ]
    
    # Define possible companions or tokens
    companions = [
        'Accompanied by a loyal animal companion',
        'Guided by an ancient spirit bound to a family heirloom',
        'Protected by a mysterious guardian who appears in times of need',
        'Carrying an enchanted weapon with a mind of its own',
        'Followed by a small magical creature only they can see',
        'Mentored by the ghost of a legendary hero',
        'Bearing a magical mark that grants them special powers',
        'Possessing a map to a place no one else believes exists',
        'Entrusted with an ancient tome of forgotten knowledge',
        'Wielding a family heirloom with powers yet to be fully discovered'
    ]
    
    # Generate backstory
    origin = random.choice(origins)
    motivation = random.choice(motivations)
    complication = random.choice(complications)
    companion = random.choice(companions)
    
    backstory = f"{character_name} is a {character_class} from {origin}. They journey to {motivation}, {complication}. {companion}."
    
    # 20% chance to add a twist
    if random.random() < 0.2:
        twists = [
            f"What {character_name} doesn't know is that their true destiny is far greater than they imagine.",
            f"Unknown to {character_name}, they are the last descendant of an ancient line of heroes.",
            f"Little does {character_name} realize that their trusted mentor has been manipulating them all along.",
            f"The truth about {character_name}'s past is hidden behind memories magically locked away.",
            f"In a strange twist of fate, {character_name} is unwittingly working for the very forces they seek to defeat."
        ]
        backstory += " " + random.choice(twists)
    
    return backstory

def generate_random_character(name=None, backstory=None):
    # Generate a random character with balanced stats
    
    # Generate name if not provided
    if name is None:
        name = generate_random_name()
    
    # Generate base stats with some randomness
    health = random.randint(80, 120)
    strength = random.randint(8, 12)
    defense = random.randint(4, 8)
    speed = random.randint(6, 10)
    
    # Create character
    character = Character(name, health, strength, defense, speed)
    
    # Randomly level up character (10% chance per level, up to 5 levels)
    for _ in range(5):
        if random.random() < 0.1:
            exp_to_level = character.exp_to_level
            character.gain_experience(exp_to_level)
    
    # Generate backstory if requested but not provided
    if backstory is None:
        character.backstory = generate_random_backstory(name)
    else:
        character.backstory = backstory
    
    return character

def generate_random_battle_scenario():
    # Generate a random battle scenario description
    
    locations = [
        'an ancient temple overgrown with vines',
        'a crumbling stone bridge spanning a chasm',
        'a dimly lit tavern filled with suspicious patrons',
        'a foggy graveyard at midnight',
        'a royal tournament arena lined with cheering spectators',
        'a narrow mountain pass during a snowstorm',
        'the burning ruins of a village under attack',
        'a magical forest clearing bathed in moonlight',
        'the depths of a monster-infested dungeon',
        'a grand ballroom now used as a fighting pit'
    ]
    
    stakes = [
        'Their honor depends on victory.',
        'The fate of an innocent hangs in the balance.',
        'Ancient treasure awaits the victor.',
        'The loser will be exiled from their homeland.',
        'They fight to determine who will lead the resistance.',
        'Only one can claim the title of champion.',
        'The duel will decide which deity receives the town\'s worship.',
        'The winner will be granted a single wish.',
        'They battle for the hand of their beloved.',
        'The victor will be deemed worthy of learning a legendary technique.'
    ]
    
    complications = [
        'But beware: the ground is unstable and may collapse at any moment.',
        'However, an ancient curse affects all who fight here, draining their strength.',
        'Unknown to both, a third party watches from the shadows, waiting to strike.',
        'The area is exposed to unpredictable bursts of wild magic.',
        'Deadly traps are scattered throughout the battlefield.',
        'A violent storm rages, affecting visibility and movement.',
        'Spectral beings occasionally interfere with the combatants.',
        'The enclosed space leaves little room for maneuvering.',
        'Venomous creatures lurk in the surroundings, ready to strike the unwary.',
        'Time flows strangely here, sometimes speeding up or slowing down unexpectedly.'
    ]
    
    scenario = f"The battle takes place in {random.choice(locations)}. {random.choice(stakes)} {random.choice(complications)}"
    
    return scenario

def generate_random_item():
    # Generate a random magical item or weapon
    
    prefixes = [
        'Ancient', 'Gleaming', 'Cursed', 'Blessed', 'Venomous', 'Fiery', 
        'Frozen', 'Astral', 'Shadow', 'Divine', 'Demonic', 'Thunderous',
        'Enchanted', 'Spectral', 'Eldritch', 'Void-touched', 'Radiant'
    ]
    
    item_types = [
        'Sword', 'Dagger', 'Bow', 'Staff', 'Shield', 'Helmet', 'Armor',
        'Gauntlets', 'Boots', 'Cloak', 'Ring', 'Amulet', 'Wand', 'Tome',
        'Axe', 'Mace', 'Spear', 'Orb', 'Crystal', 'Belt', 'Bracers'
    ]
    
    effects = [
        'increases strength by 2',
        'enhances defense by 3',
        'boosts speed by 2',
        'regenerates health slowly',
        'allows limited teleportation',
        'strikes with lightning damage',
        'burns enemies with magical fire',
        'freezes opponents occasionally',
        'drains life from enemies',
        'negates magical attacks',
        'increases critical hit chance',
        'enhances magical abilities',
        'provides resistance to poison',
        'glows in the presence of danger',
        'grants limited invisibility',
        'allows the wielder to see in darkness',
        'creates a protective barrier when health is low'
    ]
    
    histories = [
        'It once belonged to a legendary hero.',
        'It was forged in the heart of a dying star.',
        'It was crafted by master artisans of a lost civilization.',
        'It contains the bound spirit of an ancient entity.',
        'It was retrieved from the hoard of a fearsome dragon.',
        'It is said to be one piece of a powerful set of artifacts.',
        'It was created during an age when magic was far stronger.',
        'It is sought by collectors and warriors alike.',
        'Its creation is chronicled in ancient texts.',
        'It appears in the dreams of those destined to wield it.'
    ]
    
    # Generate item name and description
    prefix = random.choice(prefixes)
    item_type = random.choice(item_types)
    effect = random.choice(effects)
    history = random.choice(histories)
    
    item_name = f"{prefix} {item_type}"
    item_description = f"The {item_name} {effect}. {history}"
    
    return {
        'name': item_name,
        'description': item_description,
        'type': item_type.lower(),
        'effect': effect
    }