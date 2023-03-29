import RPi.GPIO as GPIO

def readLine(line, characters, gpioValues):
    GPIO.output(line, GPIO.HIGH)
    if(GPIO.input(gpioValues.get("C1")) == 1):
        return characters[0]
    if(GPIO.input(gpioValues.get("C2")) == 1):
        return characters[1]
    if(GPIO.input(gpioValues.get("C3")) == 1):
        return characters[2]
    if(GPIO.input(gpioValues.get("C4")) == 1):
        return characters[3]
    GPIO.output(line, GPIO.LOW)
    return None
