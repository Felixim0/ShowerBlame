import requests

def startShower(**setTime):
  setTime = setTime.get('setTime')
  print('Sending START')
  print(setTime)
  try:
    # Send message to motion sensor and display and buzzer
    response = requests.get('http://192.168.1.174:5000/startshower/' + str(setTime))
    # Send message to countdown timer
    response = requests.get('http://192.168.1.193:5000/startTimer/' + str(setTime) + '/01')
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
