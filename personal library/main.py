#Avery personal library program

# Initialize the library as an empty list
music_library = []

def add_item():
    """Add a new item to the library."""
    title = input("Enter the title of the song: ").strip()
    artist = input("Enter the artist's name: ").strip()
    album = input("Enter the album name: ").strip()
    year = input("Enter the release year: ").strip()

    # Add the new item as a dictionary to the library
    music_library.append({
        "title": title, 
        "artist": artist, 
        "album": album, 
        "year": year
    })
    print(f"'{title}' by {artist} added to your library.")

def display_items(detailed=False):
    """Display all items in the library."""
    if not music_library:
        print("Your music library is empty.")
    else:
        print("\nYour Music Library:")
        for i, item in enumerate(music_library, start=1):
            if detailed:
                print(f"{i}. Title: '{item['title']}'\n   Artist: {item['artist']}\n   Album: {item['album']}\n   Year: {item['year']}\n")
            else:
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

def update_item():
    """Update details of an existing item."""
    title_to_update = input("Enter the title of the song to update: ").strip().lower()
    
    for item in music_library:
        if item['title'].lower() == title_to_update:
            print("\nEnter new details (Press Enter to keep existing values):")
            new_title = input(f"New title [{item['title']}]: ").strip() or item['title']
            new_artist = input(f"New artist [{item['artist']}]: ").strip() or item['artist']
            new_album = input(f"New album [{item['album']}]: ").strip() or item['album']
            new_year = input(f"New year [{item['year']}]: ").strip() or item['year']

            # Update the dictionary with new values
            item.update({
                "title": new_title,
                "artist": new_artist,
                "album": new_album,
                "year": new_year
            })
            print(f"'{new_title}' by {new_artist} has been updated.")
            return
    
    print("No item with that title found.")

def remove_item():
    """Remove an item from the library by title."""
    title_to_remove = input("Enter the title of the song to remove: ").strip().lower()

    for item in music_library:
        if item['title'].lower() == title_to_remove:
            music_library.remove(item)
            print(f"'{item['title']}' has been removed from your library.")
            return
    
    print("No item with that title found.")

def run_program():
    """Run the program with a menu and loop."""
    while True:
        print("\nMusic Library Menu:")
        print("1. Add a new item")
        print("2. Display all items (Simple List)")
        print("3. Display all items (Detailed List)")
        print("4. Search for an item")
        print("5. Update an item")
        print("6. Remove an item")
        print("7. Exit")
        
        # Get user choice
        choice = input("Choose an option (1-7): ").strip()
        
        if choice == "1":
            add_item()
        elif choice == "2":
            display_items(detailed=False)
        elif choice == "3":
            display_items(detailed=True)
        elif choice == "4":
            search_item()
        elif choice == "5":
            update_item()
        elif choice == "6":
            remove_item()
        elif choice == "7":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

# Run the program
if __name__ == "__main__":
    run_program()