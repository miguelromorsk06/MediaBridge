#!/usr/bin/env python3

import requests
import os
from dotenv import load_dotenv

load_dotenv()

TMDB_API_KEY = os.getenv("TMDB_API_KEY")
SESSION_ID = os.getenv("TMDB_SESSION_ID")
ACCOUNT_ID = os.getenv("TMDB_ACCOUNT_ID")

def obtain_film_rating():
    url = f"https://api.themoviedb.org/3/account/{ACCOUNT_ID}/rated/movies"
    params = {"api_key": TMDB_API_KEY, "session_id": SESSION_ID}
    resp = requests.get(url, params=params)
    return resp.json()["results"]

def Search_film(name):
    url ="https://api.themoviedb.org/3/search/movie"
    params  = {"api_key":TMDB_API_KEY, "query":name, "language": "es-ES"}
    resp =requests.get(url,params=params)
    resultados= resp.json()["results"]
    return resultados[0] if resultados else None

def Genders(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {"api_key": TMDB_API_KEY, "language": "es-ES"}
    resp = requests.get(url, params=params)
    return resp.json()

def keywords(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/keywords"
    params = {"api_key": TMDB_API_KEY}
    resp = requests.get(url, params=params)
    return resp.json()["keywords"]
