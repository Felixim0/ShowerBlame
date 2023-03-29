import RPi.GPIO as GPIO
from time import sleep

def acknowladgeByFlashing(**gpioValues):
  for i in range(0,10):
    setGPIO(gpioValues.get("ledGPIOnum"), 1)
    sleep(0.3)
    setGPIO(gpioValues.get("ledGPIOnum"), 0)
    sleep(0.3)

def setGPIO(gpio_number, status):
  stat = GPIO.HIGH if (str(status) == '1') else GPIO.LOW

  GPIO.output(int(gpio_number),stat)
  #print(f'Changing {nbr} to {stat}')

def cleanup():
    GPIO.cleanup()

def checkButtonGPIO(gpioValues):
    if GPIO.input(gpioValues.get("buttonGPIOnum")) == True:
        return True
    return False

def setupPins():
    # Setup GPIO connectors for numberpad
    L1 = 4
    L2 = 17
    L3 = 27
    L4 = 22

    C1 = 10
    C2 = 9
    C3 = 11
    C4 = 5

    # GPIO to LCD mapping
    LCD_RS = 7   # Pi pin 26
    LCD_E  = 8   # Pi pin 24
    LCD_D4 = 25  # Pi pin 22
    LCD_D5 = 24  # Pi pin 18
    LCD_D6 = 23  # Pi pin 16
    LCD_D7 = 18  # Pi pin 12

    # GPIO bcm For button
    buttonGPIOnum = 12
    # GPIO num for led
    ledGPIOnum = 16

    # Initialize the GPIO settings
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    # NumPad GPIO
    GPIO.setup(L1, GPIO.OUT)
    GPIO.setup(L2, GPIO.OUT)
    GPIO.setup(L3, GPIO.OUT)
    GPIO.setup(L4, GPIO.OUT)

    # Display GPIOs
    GPIO.setup(LCD_E, GPIO.OUT)
    GPIO.setup(LCD_RS, GPIO.OUT)
    GPIO.setup(LCD_D4, GPIO.OUT)
    GPIO.setup(LCD_D5, GPIO.OUT)
    GPIO.setup(LCD_D6, GPIO.OUT)
    GPIO.setup(LCD_D7, GPIO.OUT)

    # Tin Foil GPIO
    GPIO.setup(buttonGPIOnum, GPIO.IN,pull_up_down=GPIO.PUD_DOWN) # For the TinFoilSwitch
    GPIO.setup(ledGPIOnum ,GPIO.OUT)


    # Make sure to configure the input pins to use the internal pull-down resistors
    GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    # Pinout of the LCD:
    # 1 : GND
    # 2 : 5V power
    # 3 : Display contrast    - Connect to middle pin potentiometer
    # 4 : RS (Register Select)
    # 5 : R/W (Read Write)    - Ground this pin (important)
    # 6 : Enable or Strobe
    # 7 : Data Bit 0          - data pin 0, 1, 2, 3 are not used
    # 8 : Data Bit 1          -
    # 9 : Data Bit 2          -
    # 10: Data Bit 3          -
    # 11: Data Bit 4
    # 12: Data Bit 5
    # 13: Data Bit 6
    # 14: Data Bit 7
    # 15: LCD Backlight +5V
    # 16: LCD Backlight GND
    print("Finished setup of pins")
    return L1, L2, L3, L4, C1, C2, C3, C4, LCD_RS, LCD_E, LCD_D4, LCD_D5, LCD_D6, LCD_D7, buttonGPIOnum, ledGPIOnum
