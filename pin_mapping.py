import machine
import time
import tm1637
from machine import Pin,I2C


isOled=0

disp = tm1637.TM1637(clk=Pin(27), dio=Pin(26))

# Initialize I2C bus (SCL, SDA pins)
i2c = I2C(0, scl=Pin(22), sda=Pin(21))

TOUCH1=Pin(14,Pin.IN)
TOUCH2=Pin(15,Pin.IN)

LED_STRIP=Pin(5,Pin.OUT)

BUZZER=Pin(32,Pin.OUT)
BUZZER.on()

IR_LDR1=Pin(39,Pin.IN,Pin.PULL_UP)
IR_LDR2=Pin(36,Pin.IN,Pin.PULL_UP)



pin_ir = Pin(25, Pin.IN) # IR receiver

oled=0


