from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.led_matrix.device import max7219
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT

# Initialize the SPI interface
serial = spi(port=0, device=0, gpio=None)

# Initialize the max7219 device with the serial interface
device = max7219(serial, cascaded=3, block_orientation=-90)

# Display the message
show_message(device, "Hello world!", fill="white", font=proportional(CP437_FONT))

