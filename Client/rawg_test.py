import requests
import os
from dotenv import load_dotenv
load_dotenv()  
Rawg_Api = os.getenv("Rawg_Api")  

def search_game(name):
    url = "https://api.rawg.io/api/games"
    param = {"key":Rawg_Api, "search": name, "page_size":1}
    resp = requests.get(url,params=param)
    results= resp.json()["results"]
    return results[0] if results else None

def obtain_genders_and_tags(name):
     game= obtain_genders_and_tags(name)
     if not game:
          return{"gender": [], "tags":[]}
     gender =[g["name"] for g in game.get("gender",[]) [:10]]
     return {"gender": gender, "tags":tags}