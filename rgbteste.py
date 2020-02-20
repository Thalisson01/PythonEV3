#!/usr/bin/env python3

from ev3dev2 import *
from sys import stderr

platform = get_current_platform()

if platform == 'ev3':
    from ev3dev2._platform.ev3 import INPUT_1, INPUT_2, INPUT_3, INPUT_4
    from ev3dev2._platform.ev3 import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
    from ev3dev2._platform.ev3 import LEDS, LED_GROUPS, LED_COLORS
else:
    raise Exception("Unsupported platform '%s'" % platform)

from ev3dev2.button import Button
from ev3dev2.led import Leds
from ev3dev2.motor import LargeMotor, SpeedPercent, MoveTank # OutPut
from ev3dev2.sensor.lego import TouchSensor, ColorSensor # Input
from time import sleep


btn = Button()
s1 = ColorSensor(INPUT_1)
s2 = ColorSensor(INPUT_4)

s1.mode = 'RGB-RAW'
s2.mode = 'RGB-RAW'

while True:
    RGB1 = [s1.value(0), s1.value(1), s1.value(2)]
    RGB2 = [s2.value(0), s2.value(1), s2.value(2)]
    print('1 - R', RGB1[0], 'G', RGB1[1], 'B', RGB1[2], file=stderr)
    print('2 - R', RGB2[0], 'G', RGB2[1], 'B', RGB2[2], file=stderr)
    sleep(1)