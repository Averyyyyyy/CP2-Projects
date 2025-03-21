# file handler 
# fix the file name (done)

def read_file(file_name):
    # Reads the content of the given file
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.read()

def write_file(file_name, content):
    # Writes the updated content back to the file
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(content)

def count_words(text):
    # Counts the number of words in the given text
    return len(text.split())

def append_word_count(content, word_count, timestamp):
    # Appends word count and timestamp to the content
    return f"{content.strip()}\n\n---\nWord Count: {word_count}\nLast Updated: {timestamp}\n"