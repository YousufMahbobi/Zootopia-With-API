import json

def load_data():
    with open('data/animals_data.json', 'r') as handle:
        return json.load(handle)
