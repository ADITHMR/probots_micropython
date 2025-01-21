
from imports import *

num_pixels = 5
np = neopixel.NeoPixel(LED_STRIP, num_pixels)
def all_set_color(r, g, b):
    for i in range(num_pixels):
        np[i] = (r, g, b)  # Set the color (Red, Green, Blue)
    np.write()  # Write the data to the strip

def set_color_for(num,r, g, b):
    for i in range(num):
        np[i] = (r, g, b)  # Set the color (Red, Green, Blue)
    np.write()  # Write the data to the strip