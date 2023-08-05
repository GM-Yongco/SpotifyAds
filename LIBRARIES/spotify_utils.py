# Description     : Spaghetti code to f#*k you up :D
# Author          : J.Z. Reyes

# BUILT-IN MODULES
from subprocess import run, Popen
from time import time
import os

# DEPENDENCIES (pywin32)
from win32 import win32gui
from win32.lib.win32con import *

# from LIBRARIES.spotify_utils import *
__all__ = ["spotify_open", "spotify_close", "spotify_play", "spotify_pause"] 

# INITIALIZE SPOTIFY LOCATION ---------------------------------------------------------------------
path = ""

if os.path.exists(os.environ['appdata'] + "\\Spotify\\Spotify.exe"):
	path += os.environ['appdata'] + "\\Spotify\\Spotify.exe"
elif os.path.exists(os.environ['localappdata'] + "\\Microsoft\\WindowsApps\\Spotify.exe"):
	path += os.environ['localappdata'] + "\\Microsoft\\WindowsApps\\Spotify.exe"
else:
	raise ImportError("Spotify not Found.")

# CLIENT UTILITY FUNCTIONS ------------------------------------------------------------------------
def spotify_open():
	# run([path])
	Popen([path])
	sTime = time()
	while (time() - sTime) <= 5:
		try:
			win32gui.EnumWindows(open_Hloop, None)
		except EndIteration:
			break

def spotify_close():
	os.system("taskkill /f /im spotify.exe")

# has song name parameter cuz the window changes name 
# when downloaded form the microsoft store
def spotify_pause_play(songName = False):
	try:
		win32gui.EnumWindows(play_Hloop, [VK_SPACE, songName])
	except EndIteration:
		return
	raise RuntimeError("Failed to pause")



# EnumWindows FUNCTIONS ---------------------------------------------------------------------------
def open_Hloop(hwnd, arg):
	if win32gui.GetWindowText(hwnd).startswith("Spotify") and win32gui.GetClassName(hwnd) == "Chrome_WidgetWin_0":
		win32gui.PostMessage(hwnd, WM_SYSCOMMAND, SC_NEXTWINDOW, 0)
		raise EndIteration

def play_Hloop(hwnd, args):
	if args[1]:
		if (win32gui.GetWindowText(hwnd).startswith("Spotify") or win32gui.GetWindowText(hwnd).endswith(args[1])) and win32gui.GetClassName(hwnd) == "Chrome_WidgetWin_0":
			client_Interact(hwnd, args[0])
			raise EndIteration
	else:
		if win32gui.GetWindowText(hwnd).startswith("Spotify") and win32gui.GetClassName(hwnd) == "Chrome_WidgetWin_0":
			client_Interact(hwnd, args[0])
			raise EndIteration

def client_Interact(hwnd, key):
	if win32gui.IsIconic(hwnd):
		wMin = True
	else:
		wMin = False

	win32gui.PostMessage(hwnd, WM_ACTIVATE, WA_CLICKACTIVE, 0)
	win32gui.PostMessage(hwnd, WM_KEYDOWN, key, 0)
	win32gui.PostMessage(hwnd, WM_KEYUP, key, 0)
	win32gui.PostMessage(hwnd, WM_ACTIVATE, WA_INACTIVE, 0)

	if wMin:
		win32gui.PostMessage(hwnd, WM_SYSCOMMAND, SC_MINIMIZE, 0)

# CUSTOM EXCEPTION
class EndIteration(Exception):
	pass


# DEBUGGER
if __name__ == '__main__':
	input("Start Spotify?")
	spotify_open()
	os.system("cls")
	input("Play/Pause?")
	spotify_pause_play()
	os.system("cls")
	input("Play/Pause?")
	spotify_pause_play()
	os.system("cls")
	input("Close Spotify?")
	spotify_close()
	os.system("cls")
	input("Press any key to end program. . .")