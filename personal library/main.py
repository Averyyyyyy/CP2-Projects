#Avery personal library program

# Initialize the library as an empty list
music_library = []

def add_item():
    """Add a new item to the library."""

    # Ask the user for item details
    title = input("Enter the title of the song: ").strip()
    artist = input("Enter the artist's name: ").strip()
    
    # Add the new item as a dictionary to the library
    music_library.append({"title": title, "artist": artist})
    print(f"'{title}' by {artist} added to your library.")

def display_items():
    """Display all items in the library."""
    if not music_library:
        print("Your music library is empty.")
    else:
        print("\nYour Music Library:")
        for i, item in enumerate(music_library, start=1):
            print(f"{i}. '{item['title']}' by {item['artist']}")
        print()  # Add blank line for spacing

def search_item():
    """Search for an item in the library by title or artist."""
    search_term = input("Enter the title or artist to search for: ").strip().lower()
    found_items = [
        item for item in music_library 
        if search_term in item['title'].lower() or search_term in item['artist'].lower()
    ]
    
    if found_items:
        print("\nSearch Results:")
        for item in found_items:
            print(f"'{item['title']}' by {item['artist']}")
    else:
        print("No matching items found.")

def remove_item():
    """Remove an item from the library by title."""
    title_to_remove = input("Enter the title of the song to remove: ").strip().lower()

    # Use a set to track indices for removal
    found = False
    for item in music_library:
        if item['title'].lower() == title_to_remove:
            found = True
            music_library.remove(item)
            print(f"'{item['title']}' has been removed from your library.")
            break
    
    if not found:
        print("No item with that title found.")

def run_program():
    """Run the program with a menu and loop."""
    while True:
        print("\nMusic Library Menu:")
        print("1. Add a new item")
        print("2. Display all items")
        print("3. Search for an item")
        print("4. Remove an item")
        print("5. Exit")
        
        # Get user choice
        choice = input("Choose an option (1-5): ").strip()
        
        if choice == "1":
            add_item()
        elif choice == "2":
            display_items()
        elif choice == "3":
            search_item()
        elif choice == "4":
            remove_item()
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Run the program
if __name__ == "__main__":
    run_program()