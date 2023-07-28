from subprocess import Popen
import os

# SPOTIFY LOCATION
path = ""

if os.path.exists(os.environ['appdata'] + "\\Spotify\\Spotify.exe"):
	path += os.environ['appdata'] + "\\Spotify\\Spotify.exe"
elif os.path.exists(os.environ['localappdata'] + "\\Microsoft\\WindowsApps\\Spotify.exe"):
	path += os.environ['localappdata'] + "\\Microsoft\\WindowsApps\\Spotify.exe"
else:
	raise ImportError("Spotify not Found.") # we can ask for install location from user


def spotify_open():
	Popen([path], shell=True)

def spotify_close():
	os.system("taskkill /f /im spotify.exe") # it might print output to console


# FOR TEST THE MODULE
if __name__ == '__main__':
	input("Start Spotify?")
	spotify_open()
	os.system("cls")
	input("Close Spotify?")
	spotify_close()
	os.system("cls")
	input("Press any key to close")