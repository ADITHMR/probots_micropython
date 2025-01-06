from machine import Pin
import time

boot_sw1=Pin(4,Pin.IN,Pin.PULL_UP)

while True :
    time.sleep(1)
    print(boot_sw1.value())