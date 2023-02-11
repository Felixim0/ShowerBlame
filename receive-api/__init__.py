#!/usr/bin/env python
# encoding: utf-8
import time
from flask import Flask
import RPi.GPIO as GPIO
overrideStopShower = False

app = Flask(__name__)

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


def allarmBlast():
  setGPIO(27, 1)
  time.sleep(2)
  setGPIO(27, 0)

@app.route('/startshower')
def showerStarted():
  global overrideStopShower
  timeLimit = 10 # seconds
  onTime = 0.5
  offTime = 0.1
  allarmBlast()
  while timeLimit > 0:
    setGPIO(4, 1)
    time.sleep(0.5)
    setGPIO(4, 0)
    time.sleep(0.1)
    timeLimit = timeLimit - (offTime + onTime)
    if overrideStopShower == True:
      timeLimit = -1
      overrideStopShower = False
  return('Succuess! Shower started')

@app.route('/stopshower')
def showerStopped():
  global overrideStopShower
  overrideStopShower = True
  allarmBlast()
  return('Shower End Signal Sent!')
  time.sleep(0.5)
  setGPIO(4, 0)
    
app.run(host='0.0.0.0')