from config import *
from tank import *
import time

turn_light_on()
status_write('light', 'auto_on')
time.sleep(auto_light_timeout)
turn_light_off()
status_write('light', 'auto_off')