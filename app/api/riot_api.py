import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("RIOT_API_KEY")

print(API_KEY)

HEADERS = {
    "X-Riot-Token": API_KEY
}

def get_puuid(game_name, tag_line):
    url = f"https://asia.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}"

    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        print("Error:", response.status_code, response.text)
        return None

    data = response.json()
    return data["puuid"]