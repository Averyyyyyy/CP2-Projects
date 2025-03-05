# Filename: web_handler.py
# Module for fetching and processing web content

import requests
from bs4 import BeautifulSoup


def fetch_web_content(url):
    # Fetch content from the provided URL
    try:
        # Send a GET request to the URL
        response = requests.get(url, 
                                headers={
                                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
                                },
                                timeout=10)
        
        # Raise an exception for bad status codes
        response.raise_for_status()
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()
        
        # Get text and remove extra whitespace
        text = soup.get_text()
        
        # Remove multiple whitespaces and newlines
        lines = (line.strip() for line in text.splitlines())
        text = ' '.join(line for line in lines if line)
        
        return text
    
    except requests.RequestException as e:
        print(f"Error fetching web content: {e}")
        sys.exit(1)