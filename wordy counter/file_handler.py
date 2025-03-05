# Filename: file_handler.py
# Module for reading and writing file contents

def read_file_content(file_path):
    # Open the file and read its entire content
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        raise


def update_file_with_stats(file_path, word_count, timestamp):
    # Create a stats section at the end of the file
    try:
        with open(file_path, 'a', encoding='utf-8') as file:
            # Add a newline to separate existing content from stats
            file.write('\n\n')
            file.write('--- Document Statistics ---\n')
            file.write(f'Word Count: {word_count}\n')
            file.write(f'Last Updated: {timestamp}\n')
    except Exception as e:
        print(f"Error updating file: {e}")
        raise