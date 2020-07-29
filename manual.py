from config import *
from tank import *
import os
import time
import threading
import json

# Local status
ls_light_on = False
ls_filter_on = False
ls_water_pump_on = False

# Continue listening
print("Listening...")
while True:

    # Check if light was auto turned off
    if status_read('light') == 'auto_off':
        ls_light_on = False
    if status_read('filter') == 'auto_off':
        ls_filter_on = False
    if status_read('water_pump') == 'auto_off':
        ls_water_pump_on = False


    # Manually Turn light on
    if status_read('light') == 'manual_on' and ls_light_on == False:
        turn_light_on()
        ls_light_on = True

    # Manually Turn light off
    if status_read('light') == 'manual_off' and ls_light_on == True:
        turn_light_off()
        ls_light_on = False

    # Manually Turn filter on
    if status_read('filter') == 'manual_on' and ls_filter_on == False:
        turn_filter_on()
        ls_filter_on = True

    # Manually Turn filter off
    if status_read('filter') == 'manual_off' and ls_filter_on == True:
        turn_filter_off()
        ls_filter_on = False

    # Manually Turn water pump on
    if status_read('water_pump') == 'manual_on' and ls_water_pump_on == False:
        turn_water_pump_on()
        ls_water_pump_on = True

    # Manually Turn water pump off
    if status_read('water_pump') == 'manual_off' and ls_water_pump_on == True:
        turn_water_pump_off()
        ls_water_pump_on = False


    # Sleep for 1 second
    time.sleep(1)


