import requests

def get_owned_games(api_key, steam_id):
    url = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/"
    params = {
        'key': api_key,
        'steamid': steam_id,
        'include_appinfo': True,  # Set to True to get game names
        'include_played_free_games': True,  # Include free games in the results
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if 'response' in data and 'games' in data['response']:
            games = data['response']['games']
            if games:
                print(f"List of games owned by the player with Steam ID {steam_id}:")
                for game in games:
                    game_name = game.get('name', 'Unknown Game')
                    hours_played = game.get('playtime_forever', 0) / 60  # Convert minutes to hours
                    print(f"{game_name} - Hours Played: {hours_played:.2f}")
            else:
                print("No games found or no hours played.")
        else:
            print("No games found or unable to retrieve game data.")
    else:
        print(f"Failed to retrieve data: {response.status_code}")

# Use your API key directly
api_key = '66b663ed3c2e70c8fa0417a3'

# Prompt user for Steam ID (not hardcoded)
steam_id = input("Please enter the Steam ID for which you want to retrieve the games: ")

get_owned_games(api_key, steam_id)
