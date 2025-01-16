from pin_mapping import *
import machine

IR_LDR1=Pin(IR_LDR1_pin,Pin.IN,Pin.PULL_UP)
light=Pin(13,Pin.OUT)


def Sensor_controlled_streetlight():
    while True:
        if IR_LDR1.value() ==False:
            light.on()
        else:
            light.off()
        
