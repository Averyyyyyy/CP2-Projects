# Avery bowman. battle sim

from characters import character_menu, characters
from battle import battle_menu
from file import save_characters, load_characters

def main():
    load_characters()
    while True:
        print("\n~~~ Battle Simulator ~~~")
        print("1. Direct Characters")
        print("2. Fight")
        print("3. Save Characters")
        print("4. Exit")
        option = input("Choose an option: ")
        if option == '1':
            character_menu()
        elif option == '2':
            battle_menu()
        elif option == '3':
            save_characters()
            print("Characters are saved.")
        elif option == '4':
            save_characters()
            print("Have a nice day!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()