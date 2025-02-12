import time
import random
import neopixel
from machine import Pin
from pin_mapping import *
from drivers.ir_decode import get_IR_data, callback,set_IR_data
from ir_rx.nec import NEC_8
from utils import get_activity_params

class NeoPixelEffects:
    def __init__(self, pin, num_pixels, increment_pin, decrement_pin):
        # Initialize NeoPixel setup
        self.pin = Pin(pin, Pin.OUT)
        self.num_pixels = num_pixels
        self.np = neopixel.NeoPixel(self.pin, self.num_pixels)
        self.old_ir_code = -1
        self.ir_code = 0
        self.loopExit = False

        # Colors for rainbow effect
        self.rainbow_colors = [
            (255, 0, 0),    # Red
            (255, 127, 0),  # Orange
            (255, 255, 0),  # Yellow
            (0, 255, 0),    # Green
            (0, 0, 255),    # Blue
            (75, 0, 130),   # Indigo
            (148, 0, 211)   # Violet
        ]

        # Setup the IR receiver
        self.ir = NEC_8(pin_ir, callback)

        # Pins for increment and decrement switches
        self.increment_pin = Pin(increment_pin, Pin.IN, Pin.PULL_UP)
        self.decrement_pin = Pin(decrement_pin, Pin.IN, Pin.PULL_UP)

        # Attach interrupts to handle switch presses
        self.increment_pin.irq(trigger=Pin.IRQ_FALLING, handler=self.increment_ir_code)
        self.decrement_pin.irq(trigger=Pin.IRQ_FALLING, handler=self.decrement_ir_code)
        
    def increment_ir_code(self, pin):
        """Increment the IR code when the increment button is pressed."""
        set_IR_data(get_IR_data()+1)
        print(f"Incremented IR Code: {self.ir_code}")

    def decrement_ir_code(self, pin):
        """Decrement the IR code when the decrement button is pressed."""
        set_IR_data(get_IR_data()-1)
        print(f"Decremented IR Code: {self.ir_code}")

    def get_random_color(self):
        """Generates a random color with RGB values."""
        return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        
    def circular_chase(self):
        """Creates a circular chase effect with random colors."""
        while not self.loopExit:
            r, g, b = self.get_random_color()

            for i in range(self.num_pixels):
                self.np.fill((0, 0, 0))  # Turn off all pixels
                self.np[i] = (r, g, b)   # Set current pixel to the random color
                self.np.write()
                time.sleep(0.05)

                if self.check_for_exit():
                    return

    def rainbow_effect(self):
        """Displays a rainbow effect cycling through the colors."""
        while not self.loopExit:
            for color in self.rainbow_colors:
                for i in range(self.num_pixels):
                    self.np[i] = color
                self.np.write()
                time.sleep(0.5)

                if self.check_for_exit():
                    return

    def filling_effect(self):
        """Creates a filling effect where colors fill in both directions."""
        while not self.loopExit:
            for i in range(len(self.rainbow_colors)):
                color = self.rainbow_colors[(i - 1) % len(self.rainbow_colors)]
                next_color = self.rainbow_colors[(i + 1) % len(self.rainbow_colors)]

                for j in range(self.num_pixels):
                    self.np[j] = color
                    self.np.write()
                    time.sleep(0.1)

                    if self.check_for_exit():
                        return

                color = next_color

                for j in range(self.num_pixels - 1, -1, -1):
                    self.np[j] = color
                    self.np.write()
                    time.sleep(0.1)

                    if self.check_for_exit():
                        return

    def check_for_exit(self):
        """Checks if IR signal is received and exits the effect."""
        ir_code = get_IR_data()
        if ir_code != self.old_ir_code:
            self.old_ir_code = ir_code
            self.loopExit = True  # Exit the current effect
            
            print(f"IR Code: {ir_code}")

            # Check for specific IR codes and switch effects
            if ir_code == 0:  # IR code for Circular Chase
                print("Switching to Circular Chase")
                self.loopExit = False
                self.circular_chase()

            elif ir_code == 1:  # IR code for Rainbow Effect
                print("Switching to Rainbow Effect")
                self.loopExit = False
                self.rainbow_effect()

            elif ir_code == 2:  # IR code for Filling Effect
                print("Switching to Filling Effect")
                self.loopExit = False
                self.filling_effect()

            return True
        
        return False

    def run(self):
        """Main loop to control the effect switching based on IR input."""
        while True:
            self.check_for_exit()


def run_activity(activity):
    """Starts the LED effects based on the given activity parameters."""
    params = get_activity_params(activity)

    # Assuming the activity params include pin and LED count
    led_pin = set_pin_out(params["strip_led_pin"])  # Ensure this function returns a valid Pin object
    num_pixels = int(params["led_num"])
    
    # Specify the pins for increment and decrement switches
    increment_pin = 14  # Pin 14 for increment
    decrement_pin = 15  # Pin 15 for decrement
    
    neo_effects = NeoPixelEffects(pin=led_pin, num_pixels=num_pixels, increment_pin=increment_pin, decrement_pin=decrement_pin)
    print("Starting 'Luminous Play: LED light magic' activity")
    neo_effects.run()
run_activity("activity1")