#!/usr/bin/env python
# encoding: utf-8
import time
from flask import Flask
import RPi.GPIO as GPIO
import threading

overrideStopShower = False
showerRunning = False

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
  #print(f'Changing {nbr} to {stat}')

def allarmBlast():
  setGPIO(27, 1)
  time.sleep(1)
  setGPIO(27, 0)

@app.route('/startshower')
def showerStarted():
  global showerRunning
  if showerRunning:
    return 'Error: Shower already running'
  showerRunning = True

  print('START shower received')
  # Received "Shower Start Message"
  global overrideStopShower
  timeLimit = 900 # 5 Minutes = 300 Seconds
  onTime = 0.5
  offTime = 0.1
  ackThread =  threading.Thread(target=allarmBlast, args=())
  ackThread.start()
  while timeLimit > 0:
    print('Countdown Begun')
    setGPIO(4, 1)
    time.sleep(onTime)
    setGPIO(4, 0)
    time.sleep(offTime)
    timeLimit = timeLimit - (offTime + onTime)
    if overrideStopShower == True:
      timeLimit = -1
      overrideStopShower = False
      print('Override activated')
    print(timeLimit)
  showerRunning = False
  return('Succuess! Shower started')

@app.route('/stopshower')
def showerStopped():
  global showerRunning
  if not showerRunning:
    return 'Error: Shower not running'
  showerRunning = False

  print('STOP shower received')
  global overrideStopShower
  overrideStopShower = True
  ackThread =  threading.Thread(target=allarmBlast, args=())
  ackThread.start()
  time.sleep(0.5)
  setGPIO(4, 0)
  return('Shower End Signal Sent!')

try:

  app.run(host='0.0.0.0')
finally:
    GPIO.cleanup()
