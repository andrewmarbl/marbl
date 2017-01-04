#!/usr/bin/env python
from SunFounder_PiPlus import *
import RPi.GPIO as GPIO

def marbl():

    global RGB

    RGB = RGB_LED(port='B')

    while True:

        RGB.breath(0, 255, 0)

def destroy():
	RGB.destroy()
	GPIO.cleanup()

if __name__ == "__main__":
	try:marbl()
	except KeyboardInterrupt:
		destroy()