#!/usr/bin/env python
from SunFounder_PiPlus import *


def setup():
    global RGB
    '''
    Initialize the RGB LED module with SunFounder_PiPlus.RGB_LED(port='A')
    Set the port to A or B, depending on which port you plug the module in.
    By default, port='A'.
    '''
    RGB = RGB_LED(port='B')


def main():
    while True:
        '''
        off() to turn off the RGB.
        '''
        RGB.off()


    RGB.breath(0, 255, 0)
    for i in range(360):
        RGB.hsb(i)
        time.sleep(0.1)

    for i in range(360):
        RGB.hsb(i, _b=0.7)
        time.sleep(0.1)


def destroy():
    RGB.destroy()
    GPIO.cleanup()


if __name__ == "__main__":
    try:
        setup()
        main()
    except KeyboardInterrupt:
        destroy()
