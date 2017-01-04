#!/usr/bin/env python
from SunFounder_PiPlus import *
class sliders(object):

	def setup(self):
		global SP
		'''
		Initialize the Slide Potentiometers module with SunFounder_PiPlus.Slide_Potentiometers()
		'''
		SP = Slide_Potentiometers()

	def main(self):
		while True:
			'''
			get_value(*sp)
			to get the specific potentiometer's value by argument *sp which ranges from 1 to 3.
			The argument should better be less than 3,
			when the number of the arguments MUST comply with the potentiometers involved.
			For example:
			sp1 = SP.get_value(1)
			sp1, sp2 = SP.get_value(1, 2)
			sp3 = SP.get_value(3)
			sp1, sp3 = SP.get_value(1, 3)
			sp1, sp2, sp3 = SP.get_value(1, 2, 3)

			'''
			self.sp1, self.sp2, self.sp3 = SP.get_value(1, 2, 3)
			#print 'RS1 = %d, RS2 = %d, RS3 = %d' % (sp1, sp2, sp3)
			time.sleep(0.1)

	def destroy(self):
		SP.destroy()
		GPIO.cleanup()

	def getdata(self):
		self.setup()
		self.main()
		return self.sp1, self.sp2, self.sp3