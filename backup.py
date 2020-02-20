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

s1.mode('RGB-RAW')
s2.mode('RGB-RAW')

while True:
    if (btn.any()):
        print('Fui pressinado!', file=stderr)
        sleep(0.1)
        # Apertar para cima
        if (btn.buttons_pressed[0] == 'up'):
            print('Para cima.', file=stderr)
            #Segue linha
            while True:
                print('.', file=stderr)
                # Verificar se apertou algo
                if (btn.any()):
                    # Apertar enter = parar
                    if (btn.buttons_pressed[0] == 'enter'):
                        print('Pausei!', file=stderr)
                        # Aguardar apertar para baixo, para continuar
                        btn.wait_for_pressed('down')
                        print('Fdppp!', file=stderr)

        elif (btn.buttons_pressed[0] == 'down'):
            print('Para BAIXO!', file-strderr)
        elif (btn.buttons_pressed[0] == 'left'):
            print('Para ESQUERDA!!', file-strderr)
        elif (btn.buttons_pressed[0] == 'right'):
            print('Para DIREITA!!', file-strderr)