#!/usr/bin/env python3

import os
from dotenv import load_dotenv
import requests

load_dotenv()

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

def get_access_token():
    url = 'https://id.twitch.tv/oauth2/token'
    params = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'client_credentials'
    }
    response = requests.post(url, params=params)
    return response.json()['access_token']

def get_streams(usernames, access_token):
    headers = {
        'Client-ID': CLIENT_ID,
        'Authorization': f'Bearer {access_token}'
    }
    params = [('user_login', user) for user in usernames]
    url = 'https://api.twitch.tv/helix/streams'
    response = requests.get(url, headers=headers, params=params)
    return response.json()['data']

def print_streams(streams):
    for stream in streams:
        name = stream['user_name']
        game = stream['game_name']
        url = f"https://twitch.tv/{stream['user_login']}"
        print(f"{url}: {name} is playing {game}")

if __name__ == '__main__':
    
    # change streamers here
    usernames = ['ThePrimeagen', 'HandOfBlood']
    token = get_access_token()
    streams = get_streams(usernames, token)
    if streams:
        print_streams(streams)
    else:
        print("No one is live right now.")

