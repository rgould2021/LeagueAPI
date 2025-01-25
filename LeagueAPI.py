#I want the program to take my last 5 matches into account and recommmend a player based off win rate or stats prior.
import requests
import os
from dotenv import load_dotenv, dotenv_values 
load_dotenv()
API_KEY = os.getenv("API_KEY")

params = {
    "X-Riot-Token": API_KEY
}
def calculateChamp():
    gameName=input("Enter Game Name: ")
    tagLine=input("Enter the Tagline #: ")
    url = "https://americas.api.riotgames.com/riot/?api_key={API_KEY}"
    response = requests.get(url, params=params)
    print(response)
    #MaCnNaP#9601
calculateChamp()