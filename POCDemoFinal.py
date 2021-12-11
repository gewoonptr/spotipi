import time

import scrollphathd
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Uncomment the below if your display is upside down
#   (e.g. if you're using it in a Pimoroni Scroll Bot)
scrollphathd.rotate(180)

# Dial down the brightness
scrollphathd.set_brightness(0.2)

# If rewind is True the scroll effect will rapidly rewind after the last line
rewind = False

# Delay is the time (in seconds) between each pixel scrolled
delay = 0.01

cid="292aaab47e4041e5937fb8ae6f5ebc30"
secret="bd548194ccfe4f43a575dcc994709def"
username = "pdzpdz@protonmail.com"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cid,client_secret=secret,redirect_uri='http://localhost/callback/',scope="user-read-currently-playing",open_browser=False))

def getSpotifyInfo():
    result = sp.current_user_playing_track()

    if result == None:
        artiest = ""
        nummer = ""
    else:
        artiest=(result['item']['album']['artists'][0]['name'])
        nummer=(result['item']['name'])

    SpotifyInfo = artiest + " - " + nummer
    return SpotifyInfo

def scroll_message(message):
    scrollphathd.clear()                         # Clear the display and reset scrolling to (0, 0)
    length = scrollphathd.write_string(message)  # Write out your message
    scrollphathd.show()                          # Show the result
    time.sleep(0.5)                              # Initial delay before scrolling

    length -= scrollphathd.width

    # Now for the scrolling loop...
    while length > 0:
        scrollphathd.scroll(1)                   # Scroll the buffer one place to the left
        scrollphathd.show()                      # Show the result
        length -= 1
        time.sleep(0.02)                         # Delay for each scrolling step

    time.sleep(0.5)                              # Delay at the end of scrolling

while(True):
    scrolltext = getSpotifyInfo()
    scroll_message(scrolltext)
    time.sleep(1)
