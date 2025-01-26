import requests
import os
import json
from urllib.parse import quote
from dotenv import load_dotenv
from champData import champions
# Load API key from .env
load_dotenv()
API_KEY = os.getenv("API_KEY")

base_url = "https://americas.api.riotgames.com"
champion_base_url = "https://na1.api.riotgames.com" 
params = {'count' : 5}

def getPUUID():
    gameName = quote(input("Enter Game Name: ").strip())
    tagLine = quote(input("Enter the Tagline #: ").strip())
    
    # Construct the URL
    url = f"{base_url}/riot/account/v1/accounts/by-riot-id/{gameName}/{tagLine}?api_key={API_KEY}"
    
    # Make the request
    response = requests.get(url)    
    
    if response.status_code == 200:
        data = response.json()
        puuid = data.get('puuid')
        print(f"PUUID: {puuid}")
        return puuid
    else:
        print(f"Error: {response.status_code}, {response.text}")

def masteryChamp():
    encryptedPUUID = getPUUID()
    params = {'count': 5, 'api_key': API_KEY}
    url2 = f"{champion_base_url}/lol/champion-mastery/v4/champion-masteries/by-puuid/{encryptedPUUID}/top"
    response = requests.get(url2, params=params)
    if response.status_code == 200:
        data = response.json()
        print(f"Based off of these mastery points I would suggest picking one of these champions since you played them the most and mastered them!")
        for champ in data:
            champ_id=champ.get("championId")
            champ_name=champions.get(champ_id, "Unknown Champion")
            mastery_points = champ.get('championPoints')
            print(f"Champion: {champ_name}, Mastery Points: {mastery_points}")
    else:
        print(f"Error: {response.status_code}, {response.text}")
masteryChamp()