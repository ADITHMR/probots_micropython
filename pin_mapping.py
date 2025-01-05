from machine import Pin
import tm1637

disp = tm1637.TM1637(clk=Pin(27), dio=Pin(26))
boot_sw1=Pin(15,Pin.IN,Pin.PULL_UP)
boot_sw2=Pin(4,Pin.IN,Pin.PULL_UP)
led=Pin(13,Pin.OUT)