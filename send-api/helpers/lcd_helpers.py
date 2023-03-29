import RPi.GPIO as GPIO
from time import sleep

# Device constants
LCD_CHR = True    # Character mode
LCD_CMD = False   # Command mode
LCD_CHARS = 16    # Characters per line (16 max)

def setup_lcd(gpioValues):
# Initialize display
  lcd_init(gpioValues)

# Initialize and clear display
def lcd_init(gpioValues):
  lcd_write(0x33,LCD_CMD, gpioValues) # Initialize
  lcd_write(0x32,LCD_CMD, gpioValues) # Set to 4-bit mode
  lcd_write(0x06,LCD_CMD, gpioValues) # Cursor move direction
  lcd_write(0x0C,LCD_CMD, gpioValues) # Turn cursor off
  lcd_write(0x28,LCD_CMD, gpioValues) # 2 line display
  lcd_write(0x01,LCD_CMD, gpioValues) # Clear display
  sleep(0.0005)     # Delay to allow commands to process

def lcd_write(bits, mode, gpioValues):
# High bits
  GPIO.output(gpioValues.get("LCD_RS"), mode) # RS

  GPIO.output(gpioValues.get("LCD_D4"), False)
  GPIO.output(gpioValues.get("LCD_D5"), False)
  GPIO.output(gpioValues.get("LCD_D6"), False)
  GPIO.output(gpioValues.get("LCD_D7"), False)
  if bits&0x10==0x10:
    GPIO.output(gpioValues.get("LCD_D4"), True)
  if bits&0x20==0x20:
    GPIO.output(gpioValues.get("LCD_D5"), True)
  if bits&0x40==0x40:
    GPIO.output(gpioValues.get("LCD_D6"), True)
  if bits&0x80==0x80:
    GPIO.output(gpioValues.get("LCD_D7"), True)

# Toggle 'Enable' pin
  lcd_toggle_enable(gpioValues)

# Low bits
  GPIO.output(gpioValues.get("LCD_D4"), False)
  GPIO.output(gpioValues.get("LCD_D5"), False)
  GPIO.output(gpioValues.get("LCD_D6"), False)
  GPIO.output(gpioValues.get("LCD_D7"), False)
  if bits&0x01==0x01:
    GPIO.output(gpioValues.get("LCD_D4"), True)
  if bits&0x02==0x02:
    GPIO.output(gpioValues.get("LCD_D5"), True)
  if bits&0x04==0x04:
    GPIO.output(gpioValues.get("LCD_D6"), True)
  if bits&0x08==0x08:
    GPIO.output(gpioValues.get("LCD_D7"), True)

# Toggle 'Enable' pin
  lcd_toggle_enable(gpioValues)

def lcd_toggle_enable(gpioValues):
  sleep(0.0005)
  GPIO.output(gpioValues.get("LCD_E"), True)
  sleep(0.0005)
  GPIO.output(gpioValues.get("LCD_E"), False)
  sleep(0.0005)

def lcd_text(message, line, gpioValues):
  # Send text to display
  message = message.ljust(LCD_CHARS," ")

  lcd_write(line, LCD_CMD, gpioValues)

  for i in range(LCD_CHARS):
    lcd_write(ord(message[i]),LCD_CHR, gpioValues)
