# import required libraries
from helpers import gpio_helpers
from helpers import lcd_helpers as lcd
import Adafruit_DHT
from time import sleep

# Setup Pins
gpio_helpers.setupPins()

# Run test lcd
lcd.setup_lcd()
