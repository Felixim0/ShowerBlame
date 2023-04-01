import re
import time
import argparse

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT


def write(msg):
    # Create device
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=1, block_orientation=0,
                     rotate=1, blocks_arranged_in_reverse_order=False)

    # Set device slightly dimmer
    device.contrast(16)

    # Calculate the time it takes to scroll the text
    scroll_delay = 0.15
    total_characters = len(msg) + device.width
    total_time = scroll_delay * total_characters

    # Log message
    print(f'Writing "{msg}" to screen')

    # Show Message to device
    show_message(device,
     msg,
     fill="white",
     font=proportional(CP437_FONT),
     scroll_delay=scroll_delay)

    # Wait the time it takes to scroll
    time.sleep(total_time)
    return False
