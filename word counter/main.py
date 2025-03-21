# Avery bowman word counter

import file_handler
import time_handler

def main():
    file_name = input("Enter the name of the file you want to analyze: ")
   
    try:
        content = file_handler.read_file(file_name)
        word_count = file_handler.count_words(content)
        timestamp = time_handler.get_current_timestamp()
       
        updated_content = file_handler.append_word_count(content, word_count, timestamp)
        file_handler.write_file(file_name, updated_content)

    # prints if it worked or didn't work
        print(f"Updated '{file_name}' with word count ({word_count}) and timestamp ({timestamp}).")
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    main()
