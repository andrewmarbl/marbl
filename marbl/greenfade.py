#!/usr/bin/env python
from SunFounder_PiPlus import *
import RPi.GPIO as GPIO
import time
from marbl import plus_rotary_encoder

def marbl():

	global RGB, RE
	rot = plus_rotary_encoder.rot()


	RE = Rotary_Encoder(port='A')
	RGB = RGB_LED(port='B')

	while True:

		RGB.breath(0, 255, 0)
		print(rot.getdata())

def destroy():
	RGB.destroy()
	GPIO.cleanup()
	RE.destroy()
	GPIO.cleanup()

if __name__ == "__main__":
	try:marbl()
	except KeyboardInterrupt:
		destroy()