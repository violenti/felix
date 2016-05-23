#!/usr/bin/env python3
 # -*- encoding: utf-8 -*-

import RPi.GPIO as GPIO
import time

def water(sensor):

     GPIO.setwarnings(False)
     GPIO.setmode(GPIO.BCM)

     if sensor == 0:

        GPIO.setup(17,GPIO.OUT)
        GPIO.setup(27,GPIO.IN)
        GPIO.output(17, GPIO.LOW)
        time.sleep(1.0)
        GPIO.output(17, True)
        time.sleep(0.00001)
        GPIO.output(17, False)

        while GPIO.input(27) == 0:
          signaloff = time.time()

        while GPIO.input(27) == 1:
          signalon = time.time()

        timepassed = signalon - signaloff
        distance = timepassed * 17000
        consumido = distance * 35
        volumen = 100 - ((consumido * 100) / 15000)
        value = str (volumen)
        redondeo = value [:4]
        print redondeo
        #agregar query sqlite

     else:
        print "Incorrect usonic() function varible."

