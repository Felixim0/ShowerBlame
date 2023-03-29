# import required libraries
from helpers import gpio_helpers
from helpers import lcd_helpers as lcd
from helpers import num_pad_helpers as num_pad
import Adafruit_DHT
from time import sleep

print("Start Program")
# Setup Pins
L1, L2, L3, L4, C1, C2, C3, C4, LCD_RS, LCD_E, LCD_D4, LCD_D5, LCD_D6, LCD_D7 = \
   gpio_helpers.setupPins()

gpioValues = {
    "L1": L1, "L2": L2, "L3": L3, "L4": L4,
    "C1": C1, "C2": C2, "C3": C3, "C4": C4,
    "LCD_RS": LCD_RS, "LCD_E" : LCD_E,
    "LCD_D4": LCD_D4, "LCD_D5": LCD_D5,
    "LCD_D6": LCD_D6, "LCD_D7": LCD_D7
}

print("Start Program")
print(gpioValues)
# Run test lcd
lcd.setup_lcd(gpioValues)

# Set screen to default start values
lcd.lcd_text("Welcome Human!", 1, gpioValues)
#lcd.lcd_text("", 2, gpioValues)

def setShowerMessage(time):
    lcd.lcd_text("Time: " + str(time) + " mins", 2, gpioValues)

setTime = 0
l1result = l2result = l3result = l4result = None
# Numpad
while True:
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
    elif (l2result != None):
        if l2result != "B":
            setTime = str(setTime) + str(l2result)
    elif (l3result != None):
        if l3result != "C":
            setTime = str(setTime) + str(l3result)
    elif (l4result != None):
        if (l4result != "D") and (l4result != "*") and (l4result != "#"):
            setTime = str(setTime) + str(l4result)

    # Remove the first 0 if that's there
    setTime = setTime[1:] if str(setTime).startswith("0") else setTime
    setShowerMessage(setTime)

    l1result = l2result = l3result = l4result = None
    sleep(0.2)
