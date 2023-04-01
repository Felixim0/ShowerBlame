#!/usr/bin/env python
from flask import Flask
import serial
import time

app = Flask(__name__)

# Deffine Arduino Communication to start a timer
def send_start_time(minutes, seconds):
    ser.write(f"{minutes},{seconds}".encode())

# Deffine Arduino Communication to cancel an ongoing timer
def reset_timer():
    ser.write(b"reset")

# Setup USB serial connection
ser = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(2)

# Initially set the timer to blank
reset_timer()

# Setup 'Start Timer' route given minutes and seconds
@app.route('/startTimer/<int:minutes>/<int:seconds>')
def startTimer(minutes, seconds):
    send_start_time(minutes, seconds)
    return('Timer Started')

# Setup route to cancel ongoing timer
@app.route('/resetTimer')
def resetTimer():
    reset_timer()
    return('Timer Reset')

# Start the API webapp
try:
    app.run(host='0.0.0.0', threaded=True)
finally:
    print("Programme ended")
