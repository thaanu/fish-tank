from config import *
import json
import time

def turn_light_on():
    print("Light is on")

def turn_light_off():
    print("Light is off")

def turn_filter_on():
    print("Filter is on")

def turn_filter_off():
    print("Filter is off")

def turn_water_pump_on():
    print("Water pump is on")

def turn_water_pump_off():
    print("Water pump is off")



# Read status
def status_read(rData):
    c = open(config_file, 'r')
    j = json.loads(c.read())
    c.close()
    return j[rData]

# Write status file
def status_write(k, v):
    c = open(config_file, 'r')
    j = json.loads(c.read())
    c.close()
    j[k] = v
    with open(config_file, 'w') as outfile:
        json.dump(j, outfile)