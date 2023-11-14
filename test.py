import pandas as pd
import json 
# HEROS IDs for json file
# https://liquipedia.net/dota2/MediaWiki:Dota2webapi-heroes.json

def data_analysis():
    data = pd.read_csv("2018/picks_bans.csv/picks_bans.csv")
    print(data.head(10))

def hero_name_id():
    with open("heros.json","r") as file:
        heros = json.load(file)
        #heros["result"]['heroes'][0]["name"]
        for hero_info in heros["result"]['heroes'][:]:
            print(hero_info)
            #pass 

if __name__=="__main__":
    #hero_name_id()
    data_analysis()
    #pass