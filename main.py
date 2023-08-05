# Description     : Code that will impress u ;)
# Author          : G.M. Yongco && Yoshi Hirishima
# IMPORTS -----------------------------------------------------------------------------------------
import time

# CUSTOM IMPORTS ----------------------------------------------------------------------------------
from LIBRARIES import spotify_api as sa
from LIBRARIES import spotify_utils as su

# MAIN --------------------------------------------------------------------------------------------
su.spotify_open()

time_delta = 5
time_total = 0
while(True):
	print(f"time check: {time_total}")
	time_total += time_delta

	if (sa.current_playing_is_ad()):
		su.spotify_close()
		time.sleep(1)
		su.spotify_open()
		time.sleep(30)
		su.spotify_pause_play()

	time.sleep(time_delta)
