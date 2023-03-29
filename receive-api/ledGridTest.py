from luma.led_matrix.device import max7219 as led

device = led.matrix(cascaded = 3)
device.show_message("Hello world!")
