# import required libraries
from helpers import gpio_helpers
from helpers import lcd_helpers as lcd
from helpers import num_pad_helpers as num_pad
from helpers import api_helpers as api
import threading, Adafruit_DHT
from time import sleep

showerRunning = False

# Setup Pins
L1, L2, L3, L4, C1, C2, C3, C4, LCD_RS, LCD_E, LCD_D4, LCD_D5, LCD_D6, LCD_D7, buttonGPIOnum, ledGPIOnum = \
   gpio_helpers.setupPins()

# Store the GPIO values in a dict
gpioValues = {
    "L1": L1, "L2": L2, "L3": L3, "L4": L4,
    "C1": C1, "C2": C2, "C3": C3, "C4": C4,
    "LCD_RS": LCD_RS, "LCD_E" : LCD_E,
    "LCD_D4": LCD_D4, "LCD_D5": LCD_D5,
    "LCD_D6": LCD_D6, "LCD_D7": LCD_D7,
    "buttonGPIOnum": buttonGPIOnum, "ledGPIOnum": ledGPIOnum
}

# Run test lcd
lcd.setup_lcd(gpioValues)

# Set the non-countdown message
def setShowerMessage(time):
    lcd.lcd_text("Welcome Human!", 1, gpioValues)
    lcd.lcd_text("Time: " + str(time) + " mins", 2, gpioValues)

# Set the countdown message
def updateCountdownShowerMessage(time):
    lcd.lcd_text("Shower On!", 1, gpioValues)
    lcd.lcd_text("Time left: " + str(time) + " mins", 2, gpioValues)

def numPadCheck():
    global setTime, showerRunning
    setTime = 0
    l1result = l2result = l3result = l4result = None
    while True:
        if showerRunning == True:
            # The shower is running, manage countdown
            # Get the next time ("4:00" --> "3:59")
            setTime = num_pad.reduceTimeByASecond(str(setTime))
            # Update the new time to the display
            updateCountdownShowerMessage(setTime)
            # Wait 1 second so the timer is accurate
            sleep(1)
            # Check if the time is up!
            if setTime == "0:00":
                showerRunning = False
                setTime = 0
                setShowerMessage(setTime)
        else:
            # call the readLine function for each row of the keypad
            l1result = num_pad.readLine(gpioValues.get("L1"), ["1","2","3","A"], gpioValues)
            l2result = num_pad.readLine(gpioValues.get("L2"), ["4","5","6","B"], gpioValues)
            l3result = num_pad.readLine(gpioValues.get("L3"), ["7","8","9","C"], gpioValues)
            l4result = num_pad.readLine(gpioValues.get("L4"), ["*","0","#","D"], gpioValues)

            if (l1result != None):
                if l1result == "A":
                    # Back, delete the last character
                    setTime = setTime[:-1]
                else:
                    setTime = str(setTime) + str(l1result)
                    setTime = str(setTime)[1:] if str(setTime).startswith("0") else setTime
            elif (l2result != None):
                if l2result != "B":
                    setTime = str(setTime) + str(l2result)
                    setTime = str(setTime)[1:] if str(setTime).startswith("0") else setTime
            elif (l3result != None):
                if l3result != "C":
                    setTime = str(setTime) + str(l3result)
                    setTime = str(setTime)[1:] if str(setTime).startswith("0") else setTime
            elif (l4result != None):
                if (l4result != "D") and (l4result != "*") and (l4result != "#"):
                    setTime = str(setTime) + str(l4result)
                    setTime = str(setTime)[1:] if str(setTime).startswith("0") else setTime

            # Remove the first 0 if that's there
            setShowerMessage(setTime)

            l1result = l2result = l3result = l4result = None

            sleep(0.2)

def buttonCheck():
    global setTime, showerRunning
    while True:
        if gpio_helpers.checkButtonGPIO(gpioValues) == True:
            # Button pressed
            if showerRunning == False:
                # Start a shower, send message to receivers
                api.startShower(setTime)

                # Start AcknowladgeByFlashing thread
                ackThread =  threading.Thread(target=gpio_helpers.acknowladgeByFlashing, kwargs=gpioValues)
                ackThread.start()

                # Start the screen countdown!
                showerRunning = True
            elif showerRunning == True:
                # Shower already running, we now want to cancell the shower
                # Set the time to essentially nothing to allow other thread to handle it
                setTime = "0:02"

        sleep(0.2)

try:
  buttonThread = threading.Thread(target=buttonCheck, args=())
  numPadThread = threading.Thread(target=numPadCheck, args=())

  # Start thread for button detection and numpad detection
  numPadThread.start()
  buttonThread.start()

  buttonThread.join()
  numPadThread.join()

finally:
    gpio_helpers.cleanup()
