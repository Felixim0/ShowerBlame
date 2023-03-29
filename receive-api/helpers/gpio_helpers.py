import RPi.GPIO as GPIO

def setGPIO(gpio_number, status):
  stat = GPIO.HIGH if (str(status) == '1') else GPIO.LOW
  GPIO.output(int(gpio_number),stat)
  #print(f'Changing {nbr} to {stat}')

def setupPins():
    # Setup GPIO connectors for numberpad
    return False

    # Setup GPIO modes
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    # LED Status Pin
    statusLed= 4

    # Setup pin as an output
    GPIO.setup(statusLed, GPIO.OUT)

    return {'statusLed': statusLed}

def turnStatusLightOn(gpioValues):
    setGPIO(gpioValues.get('statusLed'), 1)

def turnStatusLightOff(gpioValues):
    setGPIO(gpioValues.get('statusLed'), 0)

def cleanup():
    GPIO.cleanup()

def allarmBlast():
  setGPIO(27, 1)
  time.sleep(1)
  setGPIO(27, 0)
