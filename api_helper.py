import requests
import os

client_id = os.environ['CLIENT_ID']
access_token = os.environ['ACCESS_TOKEN_2']
streamer_name = os.environ['CHANNEL']

headers = {
    'Client-ID': client_id,
    'Authorization': 'Bearer ' + access_token
}

def is_live():
    stream = requests.get('https://api.twitch.tv/helix/streams?user_login=' + streamer_name, headers=headers)

    stream_data = stream.json()

    if len(stream_data['data']) == 1:
        return True
    return False

if __name__ == "__main__":
    print(is_live())
