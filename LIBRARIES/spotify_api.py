# Description     : Code that will impress u ;)
# Author          : G.M. Yongco
# SPOTIPY IMPORTS ---------------------------------------------------------------------------------
import spotipy
from spotipy.oauth2 import SpotifyOAuth

ID = open("./REFERENCES/client_ID.txt", "r").read()
SECRET = open("./REFERENCES/client_secret.txt", "r").read()
REDIRECT_URI = open("./REFERENCES/redirect_uri.txt", "r").read()

# FUNCTIONS ---------------------------------------------------------------------------------------

custom_scope = "user-read-currently-playing"
current_playing_client = spotipy.Spotify(
	auth_manager = SpotifyOAuth(
			client_id       = ID, 
			client_secret   = SECRET, 
			scope           = custom_scope, 
			redirect_uri    = REDIRECT_URI
		)
	)

# meant to return a boolean
def current_playing_is_ad():
	result = current_playing_client.currently_playing()
	return_val = False

	if(str(result) == 'None'):
		print("result is none")
	elif(result['currently_playing_type'] == 'ad'):
		return_val = True
		
	return return_val

def current_playing_song():

	result = current_playing_client.currently_playing()
	return_val = "currently_playing_type is an ad"

	if(str(result) == 'None'):
		return_val = "result_is_none"
	elif(result['currently_playing_type'] == 'ad'):
		return_val = "currently_playing_type is an ad"
	else:
		return_val = str(result['item']['name'])

	return return_val

# reminder, this func returns a string
def is_playing():
	result = current_playing_client.currently_playing()
	return_val = "currently_playing_type is an ad"

	if(str(result) == 'None'):
		return_val = "result_is_none"
	elif(result['currently_playing_type'] == 'ad'):
		return_val = "currently_playing_type is an ad"
	else:
		return_val = str(result['is_playing'])
	
	return return_val
	

def get_device_id():
	custom_scope = "user-read-playback-state"

	client = spotipy.Spotify(
	auth_manager = SpotifyOAuth(
			client_id       = ID, 	
			client_secret   = SECRET, 
			scope           = custom_scope, 
			redirect_uri    = REDIRECT_URI
		)
	)

	return client.devices()