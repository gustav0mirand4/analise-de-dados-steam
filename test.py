import pandas as pd
import json 

# HEROS IDs for json file
# https://liquipedia.net/dota2/MediaWiki:Dota2webapi-heroes.json

data = pd.read_csv("2018/picks_bans.csv/picks_bans.csv")
print(data.head())

with open("heros.json","r") as file:
    heros = json.load(file)
    #heros["result"]['heroes'][0]["name"]
    print(heros)

