#Avery, simple morse code translator

# Create two lists, one for english letters and one for Morse Code symbols
english_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
morse_code_symbols = [
    ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-",
    ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", 
    ".--", "-..-", "-.--", "--..", "-----", ".----", "..---", "...--", "....-", 
    ".....", "-....", "--...", "---..", "----."
]

# Create dictionaries for translation
english_to_morse = dict(zip(english_letters, morse_code_symbols))
morse_to_english = dict(zip(morse_code_symbols, english_letters))

# Function to translate English to Morse Code
def translate_to_morse(text):
    # Convert input text to uppercase
    text = text.upper()
    
    # Translate each character, handling unknown characters
    translated = []
    for char in text:
        if char in english_to_morse:
            translated.append(english_to_morse[char])
        elif char == " ":
            translated.append("/")  # Use '/' to separate words
        else:
            translated.append("?")  # Unknown characters replaced with '?'
    
    # Join the Morse Code symbols with spaces and return
    return " ".join(translated)

# Function to translate Morse Code to English
def translate_to_english(morse):
    # Split Morse Code into individual symbols
    words = morse.split(" / ")
    translated_words = []

    # Process each Morse Code word
    for word in words:
        letters = word.split()
        translated_word = ""

        # Convert Morse Code symbols to letters
        for symbol in letters:
            if symbol in morse_to_english:
                translated_word += morse_to_english[symbol]
            else:
                translated_word += "?"  # Handle unknown symbols

        # Add translated word to the list
        translated_words.append(translated_word)
    
    # Join translated words with spaces and return
    return " ".join(translated_words)

# Main loop for user interaction
while True:
    # Display menu options
    print("\nMorse Code Translator")
    print("1. English to Morse Code")
    print("2. Morse Code to English")
    print("3. Exit")
    
    # Get user choice
    choice = input("Enter your choice (1-3): ").strip()

    if choice == "1":
        # Translate English to Morse
        text = input("Enter English text: ")
        print("Morse Code:", translate_to_morse(text))

    elif choice == "2":
        # Translate Morse to English
        morse = input("Enter Morse Code (use '/' to separate words): ")
        print("English Text:", translate_to_english(morse))

    elif choice == "3":
        # Exit the program
        print("Goodbye!")
        break

    else:
        # Handle invalid menu input
        print("Invalid choice. Please enter 1, 2, or 3.")
