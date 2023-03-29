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

def reduceTimeByASecond(setTime):
    # Split the input string by ':'
    time_parts = setTime.split(':')

    # Check if there is only one part (i.e., just minutes)
    if len(time_parts) == 1:
        # Convert the minutes to seconds and subtract 1
        total_seconds = int(time_parts[0]) * 60 - 1
    else:
        # If there are both minutes and seconds, convert them to seconds and subtract 1
        total_seconds = int(time_parts[0]) * 60 + int(time_parts[1]) - 1

    # Calculate the new minutes and seconds after reducing one second
    new_minutes = total_seconds // 60
    new_seconds = total_seconds % 60

    # Return the new time as a formatted string
    return f"{new_minutes}:{new_seconds:02d}"
