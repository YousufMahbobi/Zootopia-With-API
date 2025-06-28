import requests
import os
from dotenv import load_dotenv

load_dotenv()


def fetch_animal_by_name(name):
    api_url = "https://api.api-ninjas.com/v1/animals"
    params = {"name": name}
    headers = {
        'X-Api-Key': os.getenv("API_KEY")
    }

    response = requests.get(api_url, params=params, headers=headers)
    if response.status_code == requests.codes.ok:
        animals_info = response.json()
        return animals_info, response.status_code, name
    else:
        return 'There is technical error, please contact website owner.', response.status_code, name




