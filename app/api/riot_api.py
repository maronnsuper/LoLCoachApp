import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("RIOT_API_KEY")


HEADERS = {
    "X-Riot-Token": API_KEY
}


class RiotAPIError(Exception):
    def __init__(self, user_message, status_code=None):
        super().__init__(user_message)
        self.user_message = user_message
        self.status_code = status_code


def _build_error_message(status_code, context):
    if status_code == 401:
        return "Riot APIキーが無効です。.env の RIOT_API_KEY を確認してください。"
    if status_code == 403:
        return "Riot APIへのアクセスが拒否されました。APIキーの有効期限や権限を確認してください。"
    if status_code == 404 and context == "puuid":
        return "Riot IDが見つかりません。Game Name と Tag を確認してください。"
    if status_code == 429:
        return "Riot APIのレート制限に達しました。少し待って再試行してください。"
    return "Riot APIの取得に失敗しました。時間をおいて再試行してください。"


def _request_json(url, context, params=None):
    response = requests.get(url, headers=HEADERS, params=params)
    if response.status_code != 200:
        print("Error:", response.status_code, response.text)
        raise RiotAPIError(
            _build_error_message(response.status_code, context),
            status_code=response.status_code,
        )
    return response.json()


def get_puuid(game_name, tag_line):
    url = f"https://asia.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}"
    data = _request_json(url, context="puuid")
    return data["puuid"]


def get_match_ids(puuid, count=20):
    url = f"https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids"
    params = {"start": 0, "count": count}
    return _request_json(url, context="match_ids", params=params)


def get_match_detail(match_id):
    url = f"https://asia.api.riotgames.com/lol/match/v5/matches/{match_id}"
    return _request_json(url, context="match_detail")
