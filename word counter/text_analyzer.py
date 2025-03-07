# Module for text analysis and timestamp generation

import re
from datetime import datetime


def count_words(text):
    # Remove extra whitespaces and split into words
    # Use regex to handle multiple whitespaces and strip punctuation
    cleaned_text = re.sub(r'[^\w\s]', '', text)
    words = cleaned_text.split()
    
    return len(words)


def get_current_timestamp():
    # Generate a formatted timestamp
    return datetime.now().strftime()