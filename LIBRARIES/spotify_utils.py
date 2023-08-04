# Description     : Spaghetti code to f#*k you up :D
# Author          : J.Z. Reyes

# BUILT-IN MODULES
from subprocess import run
import os

# DEPENDENCIES (pywin32)
# Not sure but it might raise a missing DLL error
from win32 import win32gui
from win32.lib.win32con import *
from spotify_api import current_playing_song

# use this instead:
#
# from spotify_utils import *
#
# to leave other variables undefined in the main and well, for convenience
# it might need to use this one if it raises ImportError(Location Unknown):
#
# from LIBRARIES.spotify_utils import *
__all__ = ["spotify_open", "spotify_close", "spotify_play"] 

# INITIALIZE SPOTIFY LOCATION
path = ""

if os.path.exists(os.environ['appdata'] + "\\Spotify\\Spotify.exe"):
	path += os.environ['appdata'] + "\\Spotify\\Spotify.exe"
elif os.path.exists(os.environ['localappdata'] + "\\Microsoft\\WindowsApps\\Spotify.exe"):
	path += os.environ['localappdata'] + "\\Microsoft\\WindowsApps\\Spotify.exe"
else:
	raise ImportError("Spotify not Found.") # we can ask for install location from user and make a REFERENCES txt file for it



# CLIENT UTILITY FUNCTIONS
def spotify_open():
	run([path])
	while True:
		try:
			win32gui.EnumWindows(open_Hloop, None)
		except:
			break


def spotify_close():
	os.system("taskkill /f /im spotify.exe") # it might print output to console. tell me if u want it removed :D

def spotify_play():
	try:
		win32gui.EnumWindows(play_Hloop, [VK_SPACE, current_playing_song()])
		raise RuntimeError("Failed to play/pause")
	except:
		pass



def open_Hloop(hwnd, arg):
	if win32gui.GetWindowText(hwnd).startswith("Spotify") and win32gui.GetClassName(hwnd) == "Chrome_WidgetWin_0":
		win32gui.ShowWindow(hwnd, SW_NORMAL)
		win32gui.ShowWindow(hwnd, SW_HIDE)
		return False

def play_Hloop(hwnd, args):
	if (win32gui.GetWindowText(hwnd).startswith("Spotify") or win32gui.GetWindowText(hwnd).endswith(args[1])) and win32gui.GetClassName(hwnd) == "Chrome_WidgetWin_0":

		if win32gui.IsIconic(hwnd):
			wMin = True
		else:
			wMin = False

		win32gui.PostMessage(hwnd, WM_ACTIVATE, WA_CLICKACTIVE, 0)
		win32gui.PostMessage(hwnd, WM_KEYDOWN, args[0], 0)
		win32gui.PostMessage(hwnd, WM_KEYUP, args[0], 0)
		win32gui.PostMessage(hwnd, WM_ACTIVATE, WA_INACTIVE, 0)

		if wMin:
			win32gui.ShowWindow(hwnd, SW_HIDE)

		return False


# TO TEST THE MODULE (feel free to just run the script for testing)
if __name__ == '__main__':
	input("Start Spotify?")
	spotify_open()
	os.system("cls")
	input("Play/Pause?")
	spotify_play()
	os.system("cls")
	input("Play/Pause? (2nd)")
	spotify_play()
	os.system("cls")
	input("Close Spotify?")
	spotify_close()
	os.system("cls")
	input("Press any key to close. . .")