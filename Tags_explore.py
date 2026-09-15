#!/usr/bin/env python3
from Client.Tmdb_test import obtain_film_rating , Search_film, Genders,keywords
from Client.rawg_test   import obtain_genders_and_tags
from Client.steam_test import obtain_games_and_hours

films= obtain_film_rating()
for p in films[:5]:
    print(p["title"], "gender:", Genders(p["id"]), "keywords:", keywords(p["id"]))
print("------------------")

games=obtain_games_and_hours()
for j in games [:5]:
    info=obtain_genders_and_tags(j["name"])
    print(j["name"], info)