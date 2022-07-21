from gpiozero import Button
from time import sleep
import datetime
import logging
from os.path import exists
from picamera import PiCamera

LOG_PATH = "camera.log"


if not exists(LOG_PATH):
    open(LOG_PATH, 'a').close()

# init the modules:
button = Button(2)
camera = PiCamera()
logging.basicConfig(filename=LOG_PATH, encoding='utf-8', level=logging.DEBUG)


# listen to button press and save captures
while True:

    # wait for press
    button.wait_for_press()

    # get current date and time to evoid override
    date_time = str(datetime.datetime.now())

    # replace spaces and symbols at the date and time string
    date_time = date_time.replace(" ", "_")
    date_time = date_time.replace(":", "-")
    date_time = date_time.replace(".", "_")

    try:
        # capture single frame
        camera.start_preview()
        camera.capture(f'images/{date_time}.jpg')
        camera.stop_preview()
        logging.info(f'capture image: images/{date_time}.jpg')

    except:
        logging.warning(f'Failed to capture image: images/{date_time}.jpg')

    # wait for 0.5 seconds
    sleep(0.5)