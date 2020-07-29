# THIS FILE CAN BE SET AS A CRON JOB TO RUN ON A GIVEN TIME
# THE SCRIPT WILL SLEEP FOR DEFINED TIMEOUT AND STOP THE ACTION
# CHECK CONFIG.PHP / CONFIG-SAMPLE.PHP FOR CONFIGUTATION

from config import *
from tank import *
import time

turn_light_on()
status_write('light', 'auto_on')
time.sleep(auto_light_timeout)
turn_light_off()
status_write('light', 'auto_off')