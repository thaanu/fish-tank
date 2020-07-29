# THIS FILE CAN BE CALLED WITH ARGUMENTS TO TURN ON A DEVICE
# EXAMPLE: python3 switch.py light on

import sys
from config import *
from tank import *
import time

device = str(sys.argv[1])
status = str(sys.argv[2])

if status == 'on':
    status_write(device, 'manual_on')
    print(device, status)
else:
    print("Invalid command")