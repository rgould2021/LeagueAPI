import requests
import os
import json
from urllib.parse import quote
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("API_KEY")

base_url = "https://americas.api.riotgames.com"

def calculateChamp():
    gameName = quote(input("Enter Game Name: ").strip())
    tagLine = quote(input("Enter the Tagline #: ").strip())
    
    # Construct the URL
    url = f"{base_url}/riot/account/v1/accounts/by-riot-id/{gameName}/{tagLine}?api_key={API_KEY}"
    
    # Make the request
    response = requests.get(url)
    
    if response.status_code == 200:
        print(response.json())  # Print the JSON response
    else:
        print(f"Error: {response.status_code}, {response.text}")

# Example input: MaC n NaP (gameName) and 9601 (tagLine)
calculateChamp()