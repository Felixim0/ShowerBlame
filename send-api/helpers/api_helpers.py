import requests

def startShower(setTime):
  print('Sending START')
  print(setTime)
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
