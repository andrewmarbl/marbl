#!/usr/bin/env python
from SunFounder_PiPlus import *
import RPi.GPIO as GPIO
import time

def marbl():

	global RGB, RE

	RE = Rotary_Encoder(port='A')
	RGB = RGB_LED(port='B')

	while True:

        RGB.breath(0, 255, 0)
		count = RE.rotary_deal(count, step=2)
		print(count)
		time.sleep(.5)
def destroy():
	RGB.destroy()
	GPIO.cleanup()
	RE.destroy()
	GPIO.cleanup()

if __name__ == "__main__":
	try:marbl()
	except KeyboardInterrupt:
		destroy()