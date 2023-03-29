import RPi.GPIO as GPIO

# Device constants
LCD_CHR = True    # Character mode
LCD_CMD = False   # Command mode
LCD_CHARS = 16    # Characters per line (16 max)
LCD_LINE_1 = 0x80 # LCD memory location for 1st line
LCD_LINE_2 = 0xC0 # LCD memory location 2nd line

def setup_lcd(gpioValues):
# Initialize display
  lcd_init(gpioValues)
# Loop - send text and sleep 3 seconds between texts
# Change text to anything you wish, but must be 16 characters or less
  while True:
    lcd_text("Hello World!",LCD_LINE_1)
    lcd_text("",LCD_LINE_2)

    lcd_text("Rasbperry Pi",LCD_LINE_1)
    lcd_text("16x2 LCD Display",LCD_LINE_2)
    time.sleep(3) # 3 second delay

    lcd_text("ABCDEFGHIJKLMNOP",LCD_LINE_1)
    lcd_text("1234567890123456",LCD_LINE_2)
    time.sleep(3) # 3 second delay

    lcd_text("I love my",LCD_LINE_1)
    lcd_text("Raspberry Pi!",LCD_LINE_2)
    time.sleep(3)

    lcd_text("MBTechWorks.com",LCD_LINE_1)
    lcd_text("For more R Pi",LCD_LINE_2)
    time.sleep(3)

# End of main program code

# Initialize and clear display
def lcd_init(gpioValues):
  lcd_write(0x33,LCD_CMD, gpioValues) # Initialize
  lcd_write(0x32,LCD_CMD, gpioValues) # Set to 4-bit mode
  lcd_write(0x06,LCD_CMD, gpioValues) # Cursor move direction
  lcd_write(0x0C,LCD_CMD, gpioValues) # Turn cursor off
  lcd_write(0x28,LCD_CMD, gpioValues) # 2 line display
  lcd_write(0x01,LCD_CMD, gpioValues) # Clear display
  time.sleep(0.0005)     # Delay to allow commands to process

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
  lcd_toggle_enable()

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
  lcd_toggle_enable()

def lcd_toggle_enable():
  time.sleep(0.0005)
  GPIO.output(LCD_E, True)
  time.sleep(0.0005)
  GPIO.output(LCD_E, False)
  time.sleep(0.0005)

def lcd_text(message,line):
  # Send text to display
  message = message.ljust(LCD_CHARS," ")

  lcd_write(line, LCD_CMD)

  for i in range(LCD_CHARS):
    lcd_write(ord(message[i]),LCD_CHR)
