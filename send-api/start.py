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
lcd.lcd_text("Hello World!", 1, gpioValues)
lcd.lcd_text("", 2, gpioValues)

# Numpad
while True:
    # call the readLine function for each row of the keypad
    num_pad.readLine(gpioValues.get("L1"), ["1","2","3","A"])
    num_pad.readLine(gpioValues.get("L2"), ["4","5","6","B"])
    num_pad.readLine(gpioValues.get("L3"), ["7","8","9","C"])
    num_pad.readLine(gpioValues.get("L4"), ["*","0","#","D"])
    time.sleep(0.1)
