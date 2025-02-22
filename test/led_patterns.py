import time
import random
import neopixel
from machine import Pin
from pin_mapping import *
from drivers.ir_decode import get_IR_data,callback
from ir_rx.nec import NEC_8
ir = NEC_8(pin_ir, callback)

# NeoPixel setup
pin = Pin(5, Pin.OUT)  # Set the GPIO pin where the NeoPixel strip is connected
num_pixels = 12  # Number of NeoPixels in the strip
np = neopixel.NeoPixel(pin, num_pixels)

old_ir_code=-1
ir_code=0
loopExit=0
# Colors for rainbow effect
rainbow_colors = [
    (255, 0, 0),    # Red
    (255, 127, 0),  # Orange
    (255, 255, 0),  # Yellow
    (0, 255, 0),    # Green
    (0, 0, 255),    # Blue
    (75, 0, 130),   # Indigo
    (148, 0, 211)   # Violet
]

# Effect Functions
def get_random_color():
    """Generates a random color with RGB values."""
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

def circular_chase():
    global loopExit
    """Creates a circular chase effect with random colors."""
    while not loopExit:
        r, g, b = get_random_color()

        for i in range(num_pixels):
            np.fill((0, 0, 0))  # Turn off all pixels
            np[i] = (r, g, b)   # Set current pixel to the random color
            np.write()
            time.sleep(0.05)

            check_for_exit()
            if loopExit:
                break
def rainbow_effect():
    global loopExit
    """Displays a rainbow effect cycling through the colors."""
    while not loopExit:
        for color in rainbow_colors:
            for i in range(num_pixels):
                np[i] = color
            np.write()
            time.sleep(0.5)
        
            check_for_exit()
            if loopExit:
                break

def filling_effect():
    """Creates a filling effect where colors fill in both directions."""
    global loopExit
    while not loopExit:
        for i in range(len(rainbow_colors)):
            color = rainbow_colors[(i - 1) % len(rainbow_colors)]
            next_color = rainbow_colors[(i + 1) % len(rainbow_colors)]

            for j in range(num_pixels):
                np[j] = color
                np.write()
                time.sleep(0.1)

                check_for_exit()
                if loopExit:
                    break

            color = next_color

            for j in range(num_pixels - 1, -1, -1):
                np[j] = color
                np.write()
                time.sleep(0.1)

                check_for_exit()
                if loopExit:
                    break
            check_for_exit()
            if loopExit:
                break

# Function to check for IR signal and exit the current effect if needed
def check_for_exit():
    global old_ir_code,ir_code
    ir_code = get_IR_data()
    global loopExit
    if ir_code !=old_ir_code:
        loopExit=1
        print(f"IR Code: {ir_code}")
        old_ir_code=ir_code
        # Check for specific IR codes and switch effects
        if ir_code == 0:  # Example IR code for "1" button
            print("Switching to Circular Chase")
            return True
        elif ir_code == 1:  # Example IR code for "2" button
            print("Switching to Rainbow Effect")
            return True
        elif ir_code == 2:  # Example IR code for "3" button
            print("Switching to Filling Effect")
            return True

        return False

def main():
    """Main loop to control the effect switching based on IR input."""
    current_effect = None
    global old_ir_code,ir_code, loopExit
    while True:
        if ir_code ==0:
#             old_ir_code=ir_code
            print('circular_chase')
            loopExit=0
            circular_chase()

        elif ir_code ==1:
#             old_ir_code=ir_code
            print('rainbow')
            loopExit=0
            rainbow_effect()

        elif ir_code ==2:
#             old_ir_code=ir_code
            print( 'filling')
            loopExit=0
            filling_effect()

if __name__ == "__main__":
    main()
