# import required libraries
from helpers import gpio_helpers
from helpers import lcd_helpers as lcd
import Adafruit_DHT
from time import sleep

print("Start Program")
# Setup Pins
L1, L2, L3, L4, C1, C2, C3, C4, LCD_RS, LCD_E, LCD_D4, LCD_D5, LCD_D6, LCD_D7 = \
   gpio_helpers.setupPins()

print("Start Program")
print(L1, L2, L3, L4, C1, C2, C3, C4, LCD_RS, LCD_E, LCD_D4, LCD_D5, LCD_D6, LCD_D7 )
# Run test lcd
lcd.setup_lcd(L1, L2, L3, L4, C1, C2, C3, C4, LCD_RS, LCD_E, LCD_D4, LCD_D5, LCD_D6, LCD_D7 )
