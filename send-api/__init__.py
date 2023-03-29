#!/usr/bin/env python
# encoding: utf-8
import time
import requests
import RPi.GPIO as GPIO
import threading
showerStarted = False

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(12, GPIO.IN,pull_up_down=GPIO.PUD_DOWN) # For the TinFoilSwitch

def setGPIO(gpio_number, status):
  nbr = int(gpio_number)

  if str(status) == '1':
    stat = GPIO.HIGH
  else:
    stat = GPIO.LOW

  GPIO.setup(nbr  ,GPIO.OUT)
  GPIO.output(nbr ,stat)
  #print(f'Changing {nbr} to {stat}')

def startShower():
  print('Sending START')
  try:
    response = requests.get('http://192.168.1.174:5000/startshower')
  except:
    print('There was an error')

def stopShower():
  print('Sending STOP')
  try:
    response = requests.get('http://192.168.1.174:5000/stopshower')
  except:
    print('There was an error')
  
def acknowladgeByFlashing():
  for i in range(0,10):
    setGPIO(16, 1)
    time.sleep(0.3)
    setGPIO(16, 0)
    time.sleep(0.3)

def cancelShowerTimer():
  global showerStarted
  time.sleep(900)
  # If not already cancelled
  if showerStarted == True:
    showerStarted = False

def buttonCheck():
  global showerStarted
  while True:
    if GPIO.input(17) == True:
      # Button Pressed
      if showerStarted == True:
        # Shower already running? Cancel the shower
        stopShowerThread = threading.Thread(target=stopShower, args=())
        stopShowerThread.start()
        showerStarted = False
        ackThread =  threading.Thread(target=acknowladgeByFlashing, args=())
        ackThread.start()
        # Don't accpet button input for another second to avoid infinate press
        time.sleep(1)
      else:
        # Shower isn't already running, start a shower! (and let all endpoints know)
        startShowerThread = threading.Thread(target=startShower, args=())
        startShowerThread.start()
        ackThread =  threading.Thread(target=acknowladgeByFlashing, args=())
        ackThread.start()
        showerStarted = True
        # Don't accpet button input for another second to avoid infinate press
        time.sleep(1)
    else:
      time.sleep(0.3)

try:
  buttonThread = threading.Thread(target=buttonCheck, args=())

  buttonThread.start()
  buttonThread.join()

finally:
    GPIO.cleanup()


    

