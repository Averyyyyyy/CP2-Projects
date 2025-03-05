# Filename: main.py
# Main entry point for the word counting application

# Import necessary modules
import sys
import os
import argparse
from file_handler import read_file_content, update_file_with_stats
from web_handler import fetch_web_content
from text_analyzer import count_words, get_current_timestamp


def setup_argument_parser():
    # Create an argument parser to handle different input types
    parser = argparse.ArgumentParser(description="Word Counter Tool")
    
    # Mutually exclusive group for input source
    input_group = parser.add_mutually_exclusive_group(required=True)
    
    # Option for local file input
    input_group.add_argument('-f', '--file', 
                             help='Path to the local file to analyze')
    
    # Option for web URL input
    input_group.add_argument('-u', '--url', 
                             help='URL of the web page to analyze')
    
    return parser


def process_file_document(file_path):
    # Read the content of the document
    file_content = read_file_content(file_path)
    
    # Count the words in the document
    word_count = count_words(file_content)
    
    # Get current timestamp
    timestamp = get_current_timestamp()
    
    # Update the file with word count and timestamp
    update_file_with_stats(file_path, word_count, timestamp)
    
    # Print results to console
    print(f"File processed: {file_path}")
    print(f"Word Count: {word_count}")
    print(f"Timestamp: {timestamp}")
    
    return word_count


def process_web_document(url):
    # Fetch content from the web
    web_content = fetch_web_content(url)
    
    # Count the words in the web content
    word_count = count_words(web_content)
    
    # Get current timestamp
    timestamp = get_current_timestamp()
    
    # Print results to console
    print(f"Web page scanned: {url}")
    print(f"Word Count: {word_count}")
    print(f"Timestamp: {timestamp}")
    
    return word_count


def main():
    # Set up argument parser
    parser = setup_argument_parser()
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Process based on input type
    if args.file:
        process_file_document(args.file)
    elif args.url:
        process_web_document(args.url)


# Ensure the script is run directly
if __name__ == "__main__":
    main()