from config import *
from tank import *
import time

turn_water_pump_on()
status_write('water_pump', 'auto_on')
time.sleep(auto_water_pump_timeout)
turn_water_pump_off()
status_write('water_pump', 'auto_off')