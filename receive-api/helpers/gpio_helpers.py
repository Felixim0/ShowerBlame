import RPi.GPIO as GPIO
from time import sleep

def setGPIO(gpio_number, status):
  stat = GPIO.HIGH if (str(status) == '1') else GPIO.LOW
  GPIO.output(int(gpio_number),stat)
  #print(f'Changing {nbr} to {stat}')

def setupPins():
    # Setup GPIO modes
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    # LED Status Pin
    statusLed= 4

    # Allarm pin
    allarm = 27

    # Setup pin as an output
    GPIO.setup(statusLed, GPIO.OUT)
    setGPIO(statusLed, 0)

    GPIO.setup(allarm, GPIO.OUT)
    setGPIO(allarm, 0)

    return {'statusLed': statusLed, 'allarm': allarm}

def turnStatusLightOn(gpioValues):
    setGPIO(gpioValues.get('statusLed'), 1)

def turnStatusLightOff(gpioValues):
    setGPIO(gpioValues.get('statusLed'), 0)

def cleanup():
    GPIO.cleanup()

def allarmBlast(**gpioValues):
  setGPIO(gpioValues.get('allarm'), 1)
  sleep(1)
  setGPIO(gpioValues.get('allarm'), 0)
