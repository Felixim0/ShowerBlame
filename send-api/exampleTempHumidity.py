import Adafruit_DHT
from time import sleep

# Set sensor type and BCM GPIO number
sensor = Adafruit_DHT.DHT11
gpio = 26

while True:
    sleep(1)

    # Attempt to get a reading from the sensor
    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)

    # Check if reading was successful
    if humidity is not None and temperature is not None:
        print('Temperature: {0:0.1f}°C'.format(temperature))
        print('Humidity: {0:0.1f}%'.format(humidity))
    else:
        print('Failed to get reading. Try again!')
