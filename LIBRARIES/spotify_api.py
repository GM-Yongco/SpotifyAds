# Description     : Code that will impress u ;)
# Author          : G.M. Yongco
# IMPORTS -----------------------------------------------------------------------------------------
import base64
import requests #note to self: study this library

# SPOTIPY IMPORTS ---------------------------------------------------------------------------------
import spotipy
from spotipy.oauth2 import SpotifyOAuth

ID = open("./REFERENCES/client_ID.txt", "r").read()
SECRET = open("./REFERENCES/client_secret.txt", "r").read()
REDIRECT_URI = open("./REFERENCES/redirect_uri.txt", "r").read()


# MAIN --------------------------------------------------------------------------------------------
def exception_result_none(result):
	result = str(result)

	if(str(result) == 'none'):
		raise Exception("Result was none")

def current_playing_is_ad():
	custom_scope = "user-read-currently-playing"

	client = spotipy.Spotify(
	auth_manager = SpotifyOAuth(
			client_id       = ID, 
			client_secret   = SECRET, 
			scope           = custom_scope, 
			redirect_uri    = REDIRECT_URI
		)
	)

	result = client.currently_playing()
	exception_result_none(result)

	result_type = result['currently_playing_type']
	
	return_val = 0
	if(result_type == 'ad'):
		return_val = 1
	
	return return_val

def current_playing_song():
	custom_scope = "user-read-currently-playing"

	client = spotipy.Spotify(
	auth_manager = SpotifyOAuth(
			client_id       = ID, 
			client_secret   = SECRET, 
			scope           = custom_scope, 
			redirect_uri    = REDIRECT_URI
		)
	)
	result = client.currently_playing()
	exception_result_none(result)

	return_val = "currently_playing_type is an ad"
	if(result['currently_playing_type'] == 'ad'):
		return_val = "currently_playing_type is an ad"
	else:
		return_val = str(result['item']['name'])
		print(return_val)

	return return_val