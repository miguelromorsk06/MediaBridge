#!/usr/bin/env python3

import requests
import os
from dotenv import load_dotenv
load_dotenv()  
STEAM_API = os.getenv("STEAM_API")  
STEAM_ID = os.getenv("STEAM_ID")

def obtain_games_and_hours():
    url = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/"
    params = {
        "key": STEAM_API,
        "steamid": STEAM_ID,
        "include_appinfo":True,
        "format":"json"
    }
    resp= requests.get(url,params=params)
    data=resp.json()
    return data["response"]["games"]
