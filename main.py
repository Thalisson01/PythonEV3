#!/usr/bin/env python3

"""
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
"""

from ev3dev2 import *

platform = get_current_platform()

if platform == 'ev3':
    from ev3dev2._platform.ev3 import INPUT_1, INPUT_2, INPUT_3, INPUT_4
    from ev3dev2._platform.ev3 import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
    from ev3dev2._platform.ev3 import LEDS, LED_GROUPS, LED_COLORS
else:
    raise Exception("Unsupported platform '%s'" % platform)

from ev3dev2.button import Button
from ev3dev2.console import *
from ev3dev2.display import *
from ev3dev2.fonts import *
from ev3dev2.led import Leds
from ev3dev2.motor import LargeMotor, SpeedPercent, MoveTank # OutPut
from ev3dev2.port import *
from ev3dev2.power import *
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.sound import *