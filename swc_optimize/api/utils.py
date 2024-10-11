import requests

def fetch_monster_data(monster_id=None):
    base_url = 'https://swarfarm.com/api/v2/monsters/'
    if monster_id:
        url = f'{base_url}{monster_id}/'
    else:
        url = base_url
    response = requests.get(url)
    response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
    return response.json()