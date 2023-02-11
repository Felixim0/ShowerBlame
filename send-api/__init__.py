#!/usr/bin/env python
# encoding: utf-8
import time
import requests
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17, GPIO.IN,pull_up_down=GPIO.PUD_DOWN) # For the TinFoilSwitch

def setGPIO(gpio_number, status):
  nbr = int(gpio_number)

  if str(status) == '1':
    stat = GPIO.HIGH
  else:
    stat = GPIO.LOW

  GPIO.setup(nbr  ,GPIO.OUT)

  GPIO.output(nbr ,stat)

  print(f'Changing {nbr} to {stat}')

def startShower():
  response = requests.get('http://192.168.1.174:5000/startshower')

def stopShower():
  response = requests.get('http://192.168.1.174:5000/stopshower')
  
def acknowladgeByFlashing():
  for i in range(0,10):
    setGPIO(4, 1)
    time.sleep(0.3)
    setGPIO(4, 0)
    time.sleep(0.3)


def cancelShowerTimer():
  global showerStarted
  time.sleep(10)
  # If not already cancelled
  if showerStarted == True:
    showerStarted = False

def buttonCheck():
  global showerStarted
  if GPIO.input(17) == True:
    acknowladgeByFlashing()
    if showerStarted == True:
      stopShower()
      showerStarted = False
    else:
      startShower()
      showerStarted = True
      cancellShowerThread = threading.Thread(target=cancelShowerTimer, args=())
  else:
    time.sleep(0.3)



buttonThread = threading.Thread(target=buttonCheck, args=())


buttonThread.start()
buttonThread.join()




    

