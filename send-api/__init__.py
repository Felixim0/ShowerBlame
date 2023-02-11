#!/usr/bin/env python
# encoding: utf-8
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def setGPIO(gpio_number, status):
  nbr = int(gpio_number)

  if str(status) == '1':
    stat = GPIO.HIGH
  else:
    stat = GPIO.LOW

  GPIO.setup(nbr  ,GPIO.OUT)

  GPIO.output(nbr ,stat)

  print(f'Changing {nbr} to {stat}')

def acknowladgeByFlashing():
  for i in range(0,10):
    setGPIO(4, 1)
    time.sleep(0.3)
    setGPIO(4, 0)
    time.sleep(0.3)



