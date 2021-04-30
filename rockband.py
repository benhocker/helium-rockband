#!/usr/bin/python

from helium import *

song = 'One Headlight'
artist = 'The Wallflowers'

start_chrome('www.harmonixmusic.com/games/rock-band/request')
write(song, into='Song Title')
write(artist, into='Artist')
click('Submit')
kill_browser()