from config import *
from tank import *
import time

turn_filter_on()
status_write('filter', 'auto_on')
time.sleep(auto_filter_timeout)
turn_filter_off()
status_write('filter', 'auto_off')