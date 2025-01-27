#Avery password generator

import random
import string

def get_user_preferences():
    """Ask the user for their password requirements."""
    length = int(input("Enter the desired length of the password: "))
    include_uppercase = input("Include uppercase letters? (yes/no): ").lower() == "yes"
    include_lowercase = input("Include lowercase letters? (yes/no): ").lower() == "yes"
    include_numbers = input("Include numbers? (yes/no): ").lower() == "yes"
    include_special_chars = input("Include special characters? (yes/no): ").lower() == "yes"
    return length, include_uppercase, include_lowercase, include_numbers, include_special_chars

def generate_character_pool(include_uppercase, include_lowercase, include_numbers, include_special_chars):
    """Create a pool of characters based on user preferences."""
    character_pool = ""
    if include_uppercase:
        character_pool += string.ascii_uppercase
    if include_lowercase:
        character_pool += string.ascii_lowercase
    if include_numbers:
        character_pool += string.digits
    if include_special_chars:
        character_pool += string.punctuation
    return character_pool

def generate_password(character_pool, length):
    """Generate a random password from the character pool."""
    return ''.join(random.choice(character_pool) for _ in range(length))

def main():
    print("Welcome to the Password Generator!")
    length, include_uppercase, include_lowercase, include_numbers, include_special_chars = get_user_preferences()
    
    # Validate preferences
    if not any([include_uppercase, include_lowercase, include_numbers, include_special_chars]):
        print("You must select at least one character type!")
        return

    if length < 1:
        print("Password length must be at least 1!")
        return
    
    # Generate character pool
    character_pool = generate_character_pool(include_uppercase, include_lowercase, include_numbers, include_special_chars)
    
    # Generate and display 4 possible passwords
    print("\nHere are 4 possible passwords:")
    for i in range(4):
        print(f"Password {i + 1}: {generate_password(character_pool, length)}")

if __name__ == "__main__":
    main()
