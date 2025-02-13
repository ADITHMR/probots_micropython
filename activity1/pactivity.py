import time
import random
import neopixel
from machine import Pin
from pin_mapping import *
from drivers.ir_decode import get_IR_data, callback,set_IR_data
from ir_rx.nec import NEC_8
from utils import get_activity_params
from drivers.oled import oled_two_data

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
        
    def circular_chase(self,speed=0.1):
        """Creates a circular chase effect with random colors."""
        while not self.loopExit:
            for color in self.rainbow_colors:
                for i in range(self.num_pixels):
                    for j in range(self.num_pixels):
                        self.np[j] = color if j == i else (0, 0, 0)  # Light up one pixel at a time
                    self.np.write()
                    time.sleep(speed)
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
    def pulse_effect(self, speed=0.01, max_brightness=255):
        """Makes the LEDs pulse in and out with a smooth brightness transition."""
        while not self.loopExit:
            for color in self.rainbow_colors:
                for brightness in range(0, max_brightness + 1, 10):  # Increase brightness
                    for i in range(self.num_pixels):
                        self.np[i] = (int(color[0] * brightness / max_brightness), 
                                      int(color[1] * brightness / max_brightness), 
                                      int(color[2] * brightness / max_brightness))
                    self.np.write()
                    time.sleep(speed)
                    if self.check_for_exit():
                        return
                for brightness in range(max_brightness, -1, -5):  # Decrease brightness
                    for i in range(self.num_pixels):
                        self.np[i] = (int(color[0] * brightness / max_brightness), 
                                      int(color[1] * brightness / max_brightness), 
                                      int(color[2] * brightness / max_brightness))
                    self.np.write()
                    time.sleep(speed)
                    if self.check_for_exit():
                        return
#     def color_wave_effect(self):
#         """Creates a color wave effect moving along the LED strip."""
#         while not self.loopExit:
#             for i in range(self.num_pixels):
#                 # Determine which color to use at the given position
#                 color_index = (i + int(time.time() * 10)) % len(self.rainbow_colors)
#                 color = self.rainbow_colors[color_index]
#                 self.np[i] = color
#             self.np.write()
#             time.sleep(0.1)
    def sparkle_effect(self,  spark_chance=0.1, speed=0.05):
        """Creates a sparkling effect with random pixels lighting up in the given color."""
        while not self.loopExit:
            for color in self.rainbow_colors:
                for i in range(self.num_pixels):
                    if random.random() < spark_chance:
                        self.np[i] = color
                    else:
                        self.np[i] = (0, 0, 0)  # Turn off other pixels
                    if self.check_for_exit():
                        return
                self.np.write()
                time.sleep(speed)
    def colorful_fade_effect(self, fade_time=5):
        """Smoothly fades through a set of rainbow colors."""
        while not self.loopExit:
            for i in range(len(self.rainbow_colors)):
                color_start = self.rainbow_colors[i]
                color_end = self.rainbow_colors[(i + 1) % len(self.rainbow_colors)]
                
                # Fade from color_start to color_end
                for t in range(101):
                    r = int(color_start[0] * (1 - t / 100) + color_end[0] * (t / 100))
                    g = int(color_start[1] * (1 - t / 100) + color_end[1] * (t / 100))
                    b = int(color_start[2] * (1 - t / 100) + color_end[2] * (t / 100))
                    if self.check_for_exit():
                        return
                    for j in range(self.num_pixels):
                        self.np[j] = (r, g, b)
                        if self.check_for_exit():
                            return
                    self.np.write()
                    time.sleep(fade_time / 100)
   
    def alternating_stripes_effect(self,  stripe_size=1, speed=0.1):
        """Alternates blocks of colors across the LED strip."""
        while not self.loopExit:
            for i in range(len(self.rainbow_colors)):
                color1=self.rainbow_colors[i]
                color2=self.rainbow_colors[i-1]
                for i in range(0, self.num_pixels, stripe_size * 2):
                    # Set color for the first stripe
                    for j in range(i, min(i + stripe_size, self.num_pixels)):
                        self.np[j] = color1
                     
                    # Set color for the second stripe
                    for j in range(i + stripe_size, min(i + 2 * stripe_size, self.num_pixels)):
                        self.np[j] = color2
                        
                self.np.write()
                if self.check_for_exit():
                    return
                time.sleep(speed)
                for i in range(0, self.num_pixels, stripe_size * 2):
                    # Set color for the first stripe
                    for j in range(i, min(i + stripe_size, self.num_pixels)):
                        self.np[j] = color2
                    # Set color for the second stripe
                    for j in range(i + stripe_size, min(i + 2 * stripe_size, self.num_pixels)):
                        self.np[j] = color1
                self.np.write()
                if self.check_for_exit():
                    return
                time.sleep(speed)
    def ripple_effect(self, speed=0.1, ripple_size=5):
        """Creates a ripple effect moving across the LED strip."""
        while not self.loopExit:
            for color in self.rainbow_colors:
                for ripple_start in range(self.num_pixels):
                    # Create a ripple at the starting position
                    for i in range(ripple_size):
                        if ripple_start + i < self.num_pixels:
                            self.np[ripple_start + i] = color
                            
                    self.np.write()
                    if self.check_for_exit():
                        return
                    time.sleep(speed)
                    
                    # Clear the ripple after it moves
                    for i in range(self.num_pixels):
                        self.np[i] = (0, 0, 0)
    def zigzag_effect(self,  speed=0.1):
        """Creates a zigzag motion across the LED strip."""
        while not self.loopExit:
            for color in self.rainbow_colors:
                # Zigzag motion
                for i in range(self.num_pixels):
                    # Set the color for one side and reverse it on the other
                    if i % 2 == 0:
                        self.np[i] = color
                    else:
                        self.np[i] = (0, 0, 0)
                self.np.write()
                if self.check_for_exit():
                    return
                time.sleep(speed)
                
                # Reverse the effect
                for i in range(self.num_pixels):
                    if i % 2 == 0:
                        self.np[i] = (0, 0, 0)
                    else:
                        self.np[i] = color
                self.np.write()
                if self.check_for_exit():
                    return
                time.sleep(speed)
    def candlelight_flicker(self, speed=0.1, max_brightness=200):
        """Simulates candlelight by flickering the light randomly."""
        while not self.loopExit:
            for i in range(self.num_pixels):
                flicker_brightness = random.randint(0, max_brightness)
                self.np[i] = (flicker_brightness, flicker_brightness // 2, 0)  # Yellowish flicker
            self.np.write()
            if self.check_for_exit():
                return
            time.sleep(speed)
    
    def check_for_exit(self):
        """Checks if IR signal is received and exits the effect."""
        ir_code = get_IR_data()
        if ir_code > 9:
            ir_code=9
            set_IR_data(9)
        
        if ir_code != self.old_ir_code:
            self.old_ir_code = ir_code
            self.loopExit = True  # Exit the current effect
            
            print(f"IR Code: {ir_code}")

            # Check for specific IR codes and switch effects
            if ir_code == 0:  # IR code for Circular Chase
                print("Switching to Circular Chase")
                self.loopExit = False
                oled_two_data(2,2,"Circular","Chase")
                self.circular_chase()
                

            elif ir_code == 1:  # IR code for Rainbow Effect
                print("Switching to Rainbow Effect")
                self.loopExit = False
                oled_two_data(2,2,"Rainbow","Effect")
                self.rainbow_effect()

            elif ir_code == 2:  # IR code for Filling Effect
                print("Switching to Filling Effect")
                self.loopExit = False
                oled_two_data(2,2,"Filling","Effect")
                self.filling_effect()
            elif ir_code == 3:  # IR code for Circular Chase
                print("Switching to Pulse Effect")
                self.loopExit = False
                oled_two_data(2,2,"Pulse","Effect")
                self.pulse_effect()
            elif ir_code == 4:  # IR code for Circular Chase
                print("Switching to Sparkle Effect")
                self.loopExit = False
                oled_two_data(2,2,"Sparkle","Effect")
                self.sparkle_effect()
            elif ir_code == 5:  # IR code for Circular Chase
                print("Switching to Colorful fade  Effect")
                self.loopExit = False
                oled_two_data(2,2,"Fade","Effect")
                self.colorful_fade_effect()
            
            if ir_code == 6:  # IR code for Circular Chase
                print("Switching to Alternating stripes Chase")
                self.loopExit = False
                oled_two_data(2,2,"Stripes","Chase")
                self.alternating_stripes_effect()
            if ir_code == 7:  # IR code for Circular Chase
                print("Switching to riplle effect")
                self.loopExit = False
                oled_two_data(2,2,"Ripple","Effect")
                self.ripple_effect()
            if ir_code == 8:  # IR code for Circular Chase
                print("Switching to ZigZag effect")
                self.loopExit = False
                oled_two_data(2,2,"ZigZag","Effect")
                self.zigzag_effect()
            if ir_code == 9:  # IR code for Circular Chase
                print("Switching to candlelight flicker effect")
                self.loopExit = False
                oled_two_data(2,2,"Candle","Flicker")
                self.candlelight_flicker()
                
                
                
                

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
    