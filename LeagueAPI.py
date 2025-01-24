#I want the program to take my last 5 matches into account and recommmend a player based off win rate or stats prior.
import requests
API_KEY = "RGAPI-b61d3bf1-a2f7-44af-8b62-4366bd2ff63b"
headers = {
    "X-Riot-Token": API_KEY
}
def calculateChamp():
    gameName=input("Enter game name: ")
    tagLine=input("Enter the tagline #: ")
    url = "https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{gameName}/{tagLine}"
    response = requests.get(url, headers=headers)
    print(response)
    #MaCnNaP#9601
calculateChamp()