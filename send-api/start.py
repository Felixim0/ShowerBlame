# import required libraries
from helpers import gpio_helpers
from helpers import lcd_helpers as lcd
import Adafruit_DHT
from time import sleep

print("Start Program")
# Setup Pins
L1, L2, L3, L4, C1, C2, C3, C4, LCD_RS, LCD_E, LCD_D4, LCD_D5, LCD_D6, LCD_D7 = \
   gpio_helpers.setupPins()

gpioValues = {
    "L1": L1,
    "L2": L2,
    "L3": L3,
    "L4": L4,
    "C1": C1,
    "C2": C2,
    "C3": C3,
    "C4": C4,
    "LCD_RS": LCD_RS,
    "LCD_E": LCD_E,
    "LCD_D4": LCD_D4,
    "LCD_D5": LCD_D5,
    "LCD_D6": LCD_D6,
    "LCD_D7": LCD_D7
}

print("Start Program")
print(gpioValues)
# Run test lcd
lcd.setup_lcd(gpioValues)

# Loop - send text and sleep 3 seconds between texts
# Change text to anything you wish, but must be 16 characters or less
  while True:
    lcd.lcd_text("Hello World!",LCD_LINE_1, gpioValues)
    lcd.lcd_text("",LCD_LINE_2, gpioValues)

    lcd.lcd_text("Rasbperry Pi",LCD_LINE_1, gpioValues)
    lcd.lcd_text("16x2 LCD Display",LCD_LINE_2, gpioValues)
    sleep(3) # 3 second delay

    lcd.lcd_text("ABCDEFGHIJKLMNOP",LCD_LINE_1, gpioValues)
    lcd.lcd_text("1234567890123456",LCD_LINE_2, gpioValues)
    sleep(3) # 3 second delay

    lcd.lcd_text("I love my",LCD_LINE_1, gpioValues)
    lcd.lcd_text("Raspberry Pi!",LCD_LINE_2, gpioValues)
    sleep(3)

    lcd.lcd_text("MBTechWorks.com",LCD_LINE_1, gpioValues)
    lcd.lcd_text("For more R Pi",LCD_LINE_2, gpioValues)
    sleep(3)

# End of main program code
