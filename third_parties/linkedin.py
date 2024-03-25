import json

def scrape_profile():
    with open('profile.json', 'r') as file:
        return json.load(file)
