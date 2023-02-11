#!/usr/bin/env python
# encoding: utf-8
import json,time
from flask import Flask
import RPi.GPIO as GPIO

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

@app.route('/live/set/<device_id>/<device_status>')
def setDevice(device_id, device_status):
  setGPIO(device_id, device_status)
  return f'{device_status}, {device_id}'

app.run(host='0.0.0.0')
