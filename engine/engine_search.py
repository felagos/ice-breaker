import os
import requests

def make_search(query: str, start=1, num=2):
    payload = {
        'key': os.getenv('SEARCH_KEY'),
        'cx': os.getenv('ENGINE_KEY'),
        'q': query,
        'start': start,
        'num': num
    }

    response = requests.get('https://www.googleapis.com/customsearch/v1', params=payload)

    return response.json()