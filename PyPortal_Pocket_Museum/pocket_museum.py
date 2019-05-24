import random
import time
import board
import math
from random import randint
from adafruit_pyportal import PyPortal



RANDOM_ART = str(randint(1, 470000))

# There's a few different places we look for data in the photo of the day
IMAGE_LOCATION = ["primaryImage"]
TITLE_LOCATION = ["title"]
ARTIST_LOCATION = ["artistDisplayName"]

INITIALDATASOURCE = "https://collectionapi.metmuseum.org/public/collection/v1/objects/6117"

# the current working directory (where this file is)
cwd = ("/"+__file__).rsplit('/', 1)[0]
pyportal = PyPortal(url = INITIALDATASOURCE,
                    #json_path=(IMAGE_LOCATION),
                    status_neopixel=board.NEOPIXEL,
                    default_bg=cwd+"/cute_background.bmp",
                    #text_font=cwd+"/fonts/Arial-12.bdf",
                    #text_position=((5, 220), (5, 200)),
                    #text_color=(0xFFFFFF, 0xFFFFFF),
                    #text_maxlen=(50, 50), # cut off characters
                    image_resize=(320, 240),
                    image_position=(0, 0),
                    debug = True)



print("loading...") # print to repl while waiting for font to load
pyportal.preload_font() # speed things up by preloading font


while True:

        print("Searching for new work!")

    # touch to display first / next art piece
    #if pyportal.touchscreen.touch_point:

        #random work is selected
        RANDOM_ART = str(randint(1, 470000))

        try:
            try:
                # set image json path to change pictures when screen touched
                pyportal._url=("https://collectionapi.metmuseum.org/public/collection/v1/objects/"+RANDOM_ART)
                pyportal._image_json_path = (IMAGE_LOCATION)


                value = pyportal.fetch()

                print(value[0])

                if value[0] == '':

                    continue
                    print("No image found")




                '''
                if (value[0] == '') or (value[1] == ''):

                    print("Value is null. Value 1 = ",value[0], "and value 2 = ", value[0])

                    if value[0] == '':
                        value[0] = 'UNKNOWN'

                    if value[1] == '':
                        value[1] = 'UNKNOWN'

                    value = pyportal.fetch()
                '''

            except KeyError:
                print('Key Error')
                continue
            print("Response is", value)
        except RuntimeError as e:
            print("Some error occured, retrying! -", e)





     #   if pyportal.touchscreen.touch_point:
      #      pyportal._json_path=(TITLE_LOCATION, ARTIST_LOCATION)

        stamp = time.monotonic()
        # wait 5 minutes before getting again
        while (time.monotonic() - stamp) < (5*60):
            # or, if they touch the screen, fetch immediately!
            if pyportal.touchscreen.touch_point:
                break


