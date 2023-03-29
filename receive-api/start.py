#!/usr/bin/env python
# encoding: utf-8
from time import sleep
from flask import Flask
from helpers import led_screen_8_8 as matrix
from helpers import gpio_helpers as gpio
import threading


app = Flask(__name__)

showerRunning = False

def matrixNormalMessage():
    global timer
    print('Matrix thread START')
    while timer > 0:
        matrix.write('This is a test message')
    print('Matrix thread over')

@app.route('/startshower/<int:minutes>')
def showerStarted(minutes):
  global timer
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


      sleep(1)
      timer = timer - 1





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
    gpio.cleanup()
