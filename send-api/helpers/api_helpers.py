import requests
import threading


def startTimer(**setTime):
  print()
  print('TIMER start')
  print('Set time value is:', str(setTime))
  time = setTime.get('setTime')
  # Send message to countdown timer
  try:
      response = requests.get('http://192.168.1.193:5000/startTimer/' + str(setTime) + '/01')
      print('URL: ')
      print('http://192.168.1.193:5000/startTimer/' + str(setTime) + '/01')
      print()
  except:
      print("Error starting the timer")

def startShower(**setTime):
  time = setTime.get('setTime')
  print()
  print('Start Shower (will now start timer thread and send disaply unit message)')
  print('Set setTime value is:', str(setTime))
  print('Set time value is:', str(time))
  print()
  try:
    # Start new thread to start the countdown timer
    startTimerThread = threading.Thread(target=startTimer, kwargs={'setTime': setTime})
    startTimerThread.start()

    # Send message to motion sensor and display and buzzer
    response = requests.get('http://192.168.1.174:5000/startshower/' + str(time))
  except:
    print('There was an error')

def stopShower():
  print('Sending STOP')
  try:
    # Send cancel message to sensor display and buzzer
    response = requests.get('http://192.168.1.174:5000/stopshower')
    # Send cancel message to Countdown timer
    response = requests.get('http://192.168.1.193:5000/resetTimer/')
  except:
    print('There was an error')
