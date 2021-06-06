import requests
import base64
import pprint


def authenticate():
    client_id, client_secret = "fff680c653ea49ebaca3e84b632ba529", "ab9425b0698b4a5fb20148821d54de8c"
    client_keys = client_id+":"+client_secret
    client_keys_ascii = client_keys.encode("ascii")
    base = base64.b64encode(client_keys_ascii)
    response_token = requests.post('https://accounts.spotify.com/api/token', 
                                headers={
                                    'Authorization': "Basic " +  base.decode("ascii")
                                    }, data={'grant_type': 'client_credentials'})
    return response_token.json()['access_token']

HEADERS = {'Authorization': "Bearer " + authenticate()}

def search(parameters):
    response = requests.get('https://api.spotify.com/v1/search',params=parameters,headers=HEADERS)
    return response.json()
    

def get_album(album_id):
    response = requests.get('https://api.spotify.com/v1/albums/'+album_id, headers=HEADERS)
    return response.json()


def get_track(track_id):
    response = requests.get('https://api.spotify.com/v1/tracks/'+track_id, headers=HEADERS)
    return response.json()


def get_user_playlists_amount(user_id):
    response = requests.get('https://api.spotify.com/v1/users/'+user_id+'/playlists', headers=HEADERS)
    list = response.json()["items"]
    response_list = [[name] for name in list]
    return len(response_list)

def create_new_playlist(user_id, data):
    response = requests.post('https://api.spotify.com/v1/users/'+user_id+'/playlists', headers=HEADERS, data=data)
    return  response
    
if __name__ == '__main__':
    user_id = "12163032134"
    data_create = {
        "name": "New Playlist Name :D",
        "description": "New playlist description"
    }
    pprint.pprint(get_user_playlists_amount(user_id))
    pprint.pprint(create_new_playlist(user_id, data_create))
    pprint.pprint(get_user_playlists_amount(user_id))