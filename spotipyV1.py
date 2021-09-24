import time

import scrollphathd
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Uncomment the below if your display is upside down
#   (e.g. if you're using it in a Pimoroni Scroll Bot)
scrollphathd.rotate(180)

# Dial down the brightness
scrollphathd.set_brightness(0.1)

# If rewind is True the scroll effect will rapidly rewind after the last line
rewind = False

# Delay is the time (in seconds) between each pixel scrolled
delay = 0.02

cid="292aaab47e4041e5937fb8ae6f5ebc30"
secret="bd548194ccfe4f43a575dcc994709def"
username = "pdzpdz@protonmail.com"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cid,client_secret=secret,redirect_uri='http://localhost/callback/',scope="user-read-currently-playing"))


result = sp.current_user_playing_track()

if result == None:
       out1 = "No Tracks"
       out2 = "Playing"
else:
       artiest=(result['item']['album']['artists'][0]['name'])
       nummer=(result['item']['name'])
       out1 = artiest
       out2 = nummer
 
lines = [out1, " ",out2] 
line_height = scrollphathd.DISPLAY_HEIGHT + 2
offset_left = 0
lengths = [0] * len(lines)

for line, text in enumerate(lines):
    lengths[line] = scrollphathd.write_string(text, x=offset_left, y=line_height * line)
    offset_left += lengths[line]


scrollphathd.set_pixel(offset_left - 1, (len(lines) * line_height) - 1, 0)

while True:  
       scrollphathd.scroll_to(0, 0)
       scrollphathd.show()
     
       pos_x = 0
       pos_y = 0

       for current_line, line_length in enumerate(lengths):    
              # Delay a slightly longer time at the start of each line
              time.sleep(delay * 10)            
              # Scroll to the end of the current line
              for y in range(line_length):
                     scrollphathd.scroll(1, 0)
                     pos_x += 1
                     time.sleep(delay)
                     scrollphathd.show()
                     
                     # If we're currently on the very last line and rewind is True
                     # We should rapidly scroll back to the first line.
              if current_line == len(lines) - 1 and rewind:
                     for y in range(pos_y):
                            scrollphathd.scroll(-int(pos_x / pos_y), -1)
                            scrollphathd.show()
                            time.sleep(delay)
                            
                            # Otherwise, progress to the next line by scrolling upwards
              else:
                     for x in range(line_height):
                            scrollphathd.scroll(0, 1)
                            pos_y += 1
                            scrollphathd.show()
                            time.sleep(delay)
