from pin_mapping import *
import time

def fun_with_led():
    while True:
        led.on();
        time.sleep(1)
        led.off()
        time.sleep(1)