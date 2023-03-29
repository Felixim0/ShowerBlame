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

def matrixNormalMessage():
    global timer
    print('Matrix thread START')
    while timer > 0:
        matrix.write('TEST MESSAGE')
    print('Matrix thread over')

@app.route('/startshower/<int:minutes>')
def showerStarted(minutes):
  global timer

  if timer > 0:
      # Shower already running, so stop here!
      return 'Shower already running'

  print(f'Start Shower for: {minutes} mins')

  # Received "Blast alarm to acknowladge start message received"
#  ackThread =  threading.Thread(target=allarmBlast, args=())
#  ackThread.start()

  # Start Matric Thread
  matrixThread =  threading.Thread(target=matrixNormalMessage, args=())
  matrixThread.start()

  timer = minutes * 60
  while timer > 0:
      # Start flashing light thread
      gpio.turnStatusLightOn(gpioValues)
      sleep(1)
      gpio.turnStatusLightOff(gpioValues)
      sleep(1)
      print(timer)
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
