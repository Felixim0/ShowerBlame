import requests
import threading


def startTimer(**setTime):
  time = setTime.get('setTime')
  # Send message to countdown timer
  try:
      response = requests.get('http://192.168.1.193:5000/startTimer/' + str(time) + '/01')
  except:
      print("Error starting the timer")

def startShower(**setTime):
  time = setTime.get('setTime')
  try:
    # Start new thread to start the countdown timer
    startTimerThread = threading.Thread(target=startTimer, kwargs=setTime)
    startTimerThread.start()

    # Send message to motion sensor and display and buzzer
    response = requests.get('http://192.168.1.174:5000/startshower/' + str(time))
  except:
    print('There was an error')

def stopShower():
  try:
    # Send cancel message to sensor display and buzzer
    response = requests.get('http://192.168.1.174:5000/stopshower')
    # Send cancel message to Countdown timer
    response = requests.get('http://192.168.1.193:5000/resetTimer/')
  except:
    print('There was an error')
