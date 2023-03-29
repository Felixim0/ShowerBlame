#!/usr/bin/env python
# encoding: utf-8
from time import sleep
from flask import Flask
from helpers import led_screen_8_8 as matrix
from helpers import gpio_helpers as gpio
import threading

app = Flask(__name__)

timer = 0
gpioValues = gpio.setupPins()

def matrixMessage():
    global timer
    while timer > 0:
        matrix.write('TEST MESSAGE')

def statusLed():
    global timer
    while timer > 0:
        gpio.turnStatusLightOn(gpioValues)
        sleep(0.5)
        gpio.turnStatusLightOff(gpioValues)
        sleep(0.5)

@app.route('/startshower/<int:minutes>')
def showerStarted(minutes):
  global timer

  if timer > 0:
      # Shower already running, so stop here!
      return 'Shower already running'

  # Get number of seconds
  timer = minutes * 60

  # Log start
  print(f'Start Shower for: {timer} secs')

  # Start output threads
  ackThread =  threading.Thread(target=gpio.allarmBlast, kwargs=gpioValues)
  ackThread.start()

  # Start Matric Thread
  matrixThread =  threading.Thread(target=matrixMessage, args=())
  matrixThread.start()

  # Start Matric Thread
  statusLedThread =  threading.Thread(target=statusLed, args=())
  statusLedThread.start()

  # Main program timer (all threads work of this variable)
  while timer > 0:
      print(timer)
      sleep(1)
      timer = timer - 1

  # Timer finished  !
  return 'Shower Over'


@app.route('/stopshower')
def showerStopped():
  global timer
  if timer  <= 0:
    return 'Error: Shower not running'

  # Cancel the timer
  timer = 0

#  ackThread =  threading.Thread(target=allarmBlast, args=())
 # ackThread.start()
  return('Shower End Signal Sent!')


# Start the API webapp
try:
  app.run(host='0.0.0.0')
finally:
    gpio.cleanup()
