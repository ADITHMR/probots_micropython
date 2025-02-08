import machine
import time
import drivers.tm1637 as tm1637
from machine import Pin,I2C


isOled=0

disp = tm1637.TM1637(clk=Pin(27), dio=Pin(26))

# Initialize I2C bus (SCL, SDA pins)
i2c = I2C(0, scl=Pin(22), sda=Pin(21))

TOUCH1=Pin(14,Pin.IN)
TOUCH2=Pin(15,Pin.IN)

LED_STRIP=Pin(5,Pin.OUT)

BUZZER=Pin(32,Pin.OUT)


IR_LDR1=Pin(39,Pin.IN,Pin.PULL_UP)
IR_LDR2=Pin(36,Pin.IN,Pin.PULL_UP)

servo1=Pin(33, Pin.OUT)

pin_ir = Pin(25, Pin.IN) # IR receiver

FIRE_SENSOR_PIN=35

oled=0

def set_pin_out(pin):
    pin=int(pin)
    print(pin)
    result=Pin(pin, Pin.OUT)
    return result

def set_pin_in(pin):
    pin=int(pin)
    return Pin(pin, Pin.IN)
def get_trig_state(state):
 
    if state=="Active Low":
        return 0
    elif state=="Active High":
        return 1
    else:
        return 0
    
