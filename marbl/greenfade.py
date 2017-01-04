#!/usr/bin/env python
from SunFounder_PiPlus import *
import RPi.GPIO as GPIO
import time
from marbl.plus_slide_potentiometers import sliders

def marbl():

	anything = sliders()

	global RGB, RE

	RGB = RGB_LED(port='B')

	while True:
		print(sliders.getdata())
		RGB.breath(0, 255, 0)

def destroy():
	RGB.destroy()
	GPIO.cleanup()

if __name__ == "__main__":
	try:marbl()
	except KeyboardInterrupt:
		destroy()