#!/usr/bin/env python
from SunFounder_PiPlus import *

global RGB

RGB = RGB_LED(port='B')

RGB.rgb(0, 255, 0)
