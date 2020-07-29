# THIS FILE HAS TO BE RUNNING IN THE BACKGROUND
# THE SCRIPT CHECKS FOR AN MANUAL DEVICE TURN ON AND TURN'S IT OFF WHEN IT REACHES THE TIMEOUT

from config import *
from tank import *
import time

timer = 1

while True:

    # Turn light off, if manuall on
    if status_read('light') == 'manual_on':
        while timer != config_timeout:
            timer += 1
            time.sleep(1)
        turn_light_off()
        status_write('light', 'auto_off')
        timer = 0

    # Turn light off, if manuall on
    if status_read('filter') == 'manual_on':
        while timer != config_timeout:
            timer += 1
            time.sleep(1)
        turn_filter_off()
        status_write('filter', 'auto_off')
        timer = 0

    # Turn light off, if manuall on
    if status_read('water_pump') == 'manual_on':
        while timer != config_timeout:
            timer += 1
            time.sleep(1)
        turn_water_pump_off()
        status_write('water_pump', 'auto_off')
        timer = 0

    # Sleep for 1 second and continue
    time.sleep(1)