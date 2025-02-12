import neopixel
import machine

class CustomNeoPixel:
    def __init__(self, pin, num_pixels, enabled=True):
        """Initializes the NeoPixel strip."""
        self.is_enabled = enabled
        if self.is_enabled:
            self.np = neopixel.NeoPixel(machine.Pin(pin,machine.Pin.OUT), num_pixels)

    def set_color(self, index, r, g, b):
        """Sets the color of a specific NeoPixel."""
        if self.is_enabled:
            if 0 <= index < len(self.np):
                self.np[index] = (r, g, b)
                self.np.write()

    def clear(self):
        """Turns off all the NeoPixels."""
        if self.is_enabled:
            self.np.fill((0, 0, 0))  # More efficient to fill all pixels at once
            self.np.write()

