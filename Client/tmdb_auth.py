#!/usr/bin/env python3
import requests
import os
from dotenv import load_dotenv

load_dotenv()

TMDB_API_KEY = os.getenv("TMDB_API_KEY")

def obtener_request_token():
    url = "https://api.themoviedb.org/3/authentication/token/new"
    resp = requests.get(url, params={"api_key": TMDB_API_KEY})
    return resp.json()["request_token"]

def crear_session_id(request_token):
    url = "https://api.themoviedb.org/3/authentication/session/new"
    resp = requests.post(url, params={"api_key": TMDB_API_KEY}, json={"request_token": request_token})
    return resp.json()["session_id"]

def obtener_account_id(session_id):
    url = "https://api.themoviedb.org/3/account"
    resp = requests.get(url, params={"api_key": TMDB_API_KEY, "session_id": session_id})
    return resp.json()["id"]

if __name__ == "__main__":
    token = obtener_request_token()
    print(f"Ve a esta URL y autoriza la app:\nhttps://www.themoviedb.org/authenticate/{token}\n")
    input("Pulsa Enter cuando hayas autorizado...")

    session_id = crear_session_id(token)
    account_id = obtener_account_id(session_id)

    print("\n✅ Copia estos valores a tu .env:\n")
    print(f"TMDB_SESSION_ID={session_id}")
    print(f"TMDB_ACCOUNT_ID={account_id}")