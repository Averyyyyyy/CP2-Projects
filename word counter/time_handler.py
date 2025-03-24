# time handler

from datetime import datetime

def get_current_timestamp():
    # Returns the current timestamp as a formatted string
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")