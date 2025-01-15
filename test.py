import machine
import neopixel
import time

pin = machine.Pin(2)

np = neopixel.NeoPixel(pin, 3)

np[1] = (100, 100, 100)
np.write()