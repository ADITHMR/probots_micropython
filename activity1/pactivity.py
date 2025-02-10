
# *************Luminous Play: LED light magic**********************

from machine import Pin
from pin_mapping import *
import machine
import neopixel
import time
import random
from imports import *
from drivers.ir_decode import get_IR_data
import os
from utils import get_activity_params
from ir_rx.nec import NEC_8
ir = NEC_8(pin_ir, callback) # Instantiate the NEC_8 receiver

num_pixels=5
Red=0
Green=0
Blue=0
i=0
k=0
interrupted=0
count=0
intensity=255
switch_val=0



a=1
b=c=0
def clear():
    for i in range(num_pixels):
        np[i]=(0,0,0,0)
    Write()
def F_ON(Red,Green,Blue):
    for i in range(num_pixels):
        np[i]=(Red,Green,Blue)
    Write()

def mode2():
    clear()
    colorset={(255,0,0),(0,255,0),(0,0,255),(0,255,255),(255,255,0),(255,255,255)}
    for color in colorset:
        for i in range(num_pixels):  
            np[i]=color   
            Write()
            if get_IR_data()!=2:
                return
            time.sleep(.2)
        time.sleep(0.5)
    

def ON(Led,Red,Green,Blue):
    np[Led]=(Blue,Red,Green)
    Write()
def Write():
    np.write()
    if(interrupted):
        return
def OFF(Led,Red,Green,Blue):
    np[Led]=(0,0,0)
    Write()    
def mode3():
    color=255,0,0,0,255,0,0,0,255,255,255,0,0,255,255,255,255,255
    for i in range(len(color)-3):        
        Red=color[i]
        Green=color[i+1]
        Blue=color[i+2]
        i=i+3
        for k in range(num_pixels):
            ON(k,Red,Green,Blue)
            time.sleep(.1)
            if get_IR_data()!=3:
                return
        for k in range(num_pixels):
            ON(num_pixels-k-1,0,0,0)
            time.sleep(.1)
            
def mode4():
    color=255,0,0,0,255,0,0,0,255,255,255,0,0,255,255,255,255,255
    for i in range(len(color)-3):        
        Red=color[i]
        Green=color[i+1]
        Blue=color[i+2]
        i=i+3
        for k in range(num_pixels):
            clear()
            ON(k,Red,Green,Blue)
            time.sleep(.1)
            if get_IR_data()!=4:
                return
        for k in range(num_pixels):
            clear()
            ON(num_pixels-k-1,Red,Green,Blue)
            time.sleep(.1)
def mode5():
    color=255,0,0,0,255,0,0,0,255,255,255,0,0,255,255,255,255,255
    for i in range(len(color)-3):        
        Red=color[i]
        Green=color[i+1]
        Blue=color[i+2]
        i=i+3
        for k in range(num_pixels):
            F_ON(Red,Green,Blue)
            ON(k,0,0,0)
            #if(k+1<num_pixels):
                #ON(k+1,Red,Green,Blue)
            time.sleep(.1)
            if get_IR_data()!=5:
                return
        for k in range(num_pixels):
            F_ON(Red,Green,Blue)
            ON(num_pixels-k-1,0,0,0)
#             if(k>0):
#                 ON(k-1,0,0,0)
            time.sleep(.1)
            if get_IR_data()!=5:
                return
def mode6():
    color=255,0,0,0,255,0,0,0,255,255,255,0,0,255,255,255,255,255
    for i in range(len(color)-3):        
        Red=color[i]
        Green=color[i+1]
        Blue=color[i+2]
        i=i+3
        for k in range(num_pixels):
            clear()
            ON(k,Red,Green,Blue)
            if(k+1<num_pixels):
                ON(k+1,Red,Green,Blue)   
            time.sleep(.2)
            if get_IR_data()!=6:
                return
            
        for k in range(num_pixels):
            clear()
            ON(num_pixels-k-1,Red,Green,Blue)
            if(k>0):
                ON(k-1,Red,Green,Blue) 
            time.sleep(.2)
            if get_IR_data()!=6:
                return
def mode7():
    l=0
    color=255,0,0,0,255,0,0,0,255,0,255,255,255,255,0,255,255,255
    colorset={(255,0,0),(0,255,0),(0,0,255),(0,255,255),(255,255,0),(255,255,255)}
    clear()
#     for i in range(len(color)-3):
#         Red=color[i]
#         Green=color[i+1]
#         Blue=color[i+2]            
#         i=i+3
    for color in colorset:
        for z in range(10):
            for k in range(num_pixels):
                clear()
                #ON(k,Red,Green,Blue)
                np[k]=color
                Write()
                time.sleep(.1)
                if get_IR_data()!=7:
                    return
            clear()
            time.sleep(.05)
def mode8(): #random
    wait=0.1
#    print(num_pixels)
    for i in range(num_pixels):        
        if random.randint(0, 10) > 8:  # 20% chance of twinkling
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            np[i] = color
            if get_IR_data()!=8:
                return
        else:
            np[i] = (0, 0, 0)  # Turn off some LEDs
    Write()
    time.sleep(wait)
def mode9():  #wave
    wait=0.05
    for j in range(num_pixels * 2):
        for i in range(num_pixels):
            if (i + j) % num_pixels == 0:
                np[i] = (255, 0, 0)  # green color
                if get_IR_data()!=9:
                    return
            else:
                np[i] = (0, 0, 0)  # Turn off the LED
        Write()
        time.sleep(wait)
def mode0():
    wait=0.1
    for i in range(num_pixels):
        np[i] = (255, 255, 255)  # White light
        Write()
        time.sleep(wait)
        np[i] = (0, 0, 0)  # Turn off the light
        if get_IR_data()!=10:
                return

    for i in range(num_pixels - 1, -1, -1):
        np[i] = (255, 255, 255)
        Write()
        time.sleep(wait)
        np[i] = (0, 0, 0)
        if get_IR_data()!=10:
                return
import random

def mode11():#fire_effect
    wait=0.05
    for i in range(num_pixels):
        red = random.randint(0, 255)
        green = random.randint(0, red)  # Green is always less than or equal to red
        blue = random.randint(0, green)  # Blue is always less than or equal to green
        np[i] = (blue,red,green)  # Simulate fire color
        if get_IR_data()!=11:
                return
    Write()
    time.sleep(wait)
def mode12(): # increase & decrease colorset brightness
    wait=0.01
    colorset={(1,0,0),(0,1,0),(0,0,1),(0,1,1),(1,1,0),(1,1,1)}
    for color in colorset:
        for brightness in range(0, 255, 5):  # Increasing brightness
            for i in range(num_pixels):
                np[i] =((brightness*color[0]),(brightness*color[1]),(brightness*color[2]))
                if get_IR_data()!=12:
                    return
            Write()
            time.sleep(wait)
        for brightness in range(255, 0, -5):  # Decreasing brightness
            for i in range(num_pixels):
                np[i] =((brightness*color[0]),(brightness*color[1]),(brightness*color[2]))
                if get_IR_data()!=12:
                    return
            Write()
            time.sleep(wait)
def mode13(): #rainbow_chase
    wait=0.1
    for j in range(256):  # Number of color shifts (one full rainbow)
        for i in range(num_pixels):
            color = wheel((i + j) & 255)  # Shift color based on position
            np[i] = color
            if get_IR_data()!=13:
                return
        Write()
        time.sleep(wait)
def mode14():#full_color_fade
#     print("Fade in colors")
    wait=0.2
    for j in range(256):
        for i in range(num_pixels):
            np[i] = (j, 0, 0)  # Red fades in
            if get_IR_data()!=14:
                return
        Write()
        time.sleep(wait)        
        for i in range(num_pixels):
            np[i] = (0, j, 0)  # Green fades in
            if get_IR_data()!=14:
                return
        Write()
        time.sleep(wait)
        
        for i in range(num_pixels):
            np[i] = (0, 0, j)  # Blue fades in
            if get_IR_data()!=14:
                return
        Write()
        time.sleep(wait)
      
#     print("colors")
    for j in range(255, -1, -1):
        for i in range(num_pixels):
            np[i] = (j, 0, 0)  # Red fades out
            if get_IR_data()!=14:
                return
        Write()
        time.sleep(wait)
        
        for i in range(num_pixels):
            np[i] = (0, j, 0)  # Green fades out
            if get_IR_data()!=14:
                return
        Write()
        time.sleep(wait)
        
        for i in range(num_pixels):
            np[i] = (0, 0, j)  # Blue fades out
            if get_IR_data()!=14:
                return
        Write()
        time.sleep(wait)
def wheel(pos):
    """
    Generate color from a position on the color wheel.
    :param pos: Integer position from 0 to 255 (representing 360 degrees on the color wheel)
    :return: (r, g, b) tuple for the RGB color
    """
    if pos < 85:
        return (pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return (255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return (0, pos * 3, 255 - pos * 3)
def mode1():
    clear()
    colorset={(255,0,0),(0,255,0),(0,0,255),(0,255,255),(255,255,0),(255,255,255)}
    for color in colorset:
        for i in range(num_pixels):
            if(i):
                OFF(i-1,color[0],color[1],color[2])
            ON(i,color[0],color[1],color[2])
            if get_IR_data()!=1:
                return
            time.sleep(1)
        for i in range(num_pixels):        
            OFF(num_pixels-i-1,0,0,0)
            if((num_pixels-i-2)>=0):
                ON(num_pixels-2-i,color[0],color[1],color[2])
            if get_IR_data()!=1:
                return
            time.sleep(1)
def LED(mode):
    #print(mode)
    if(mode==0):
        mode0()
    elif(mode==1):
        mode1()
    elif(mode==2):
        mode2()
    elif(mode==3):
        mode3()
    elif(mode==4):
        mode4()
    elif(mode==5):
        mode5()
    elif(mode==6):
        mode6()
    elif(mode==7):
        mode7()
    elif(mode==8):
        mode8()
    elif(mode==9):
        mode9()
    elif(mode==10):
        mode10()
    elif(mode==11):
        mode11()
    elif(mode==12):
        mode12()
    elif(mode==13):
        mode13()
    elif(mode==14):
        mode14()
num_leds=5
def fire_effect():
    # Create a random flickering effect that simulates fire colors
      # Simulate a lightning strike (all LEDs flash brightly)
    for i in range(num_leds):
        # Create a gradient effect, moving from blue to green to red
        r = int(255 * (i / num_leds))  # Smooth red transition
        g = int(255 * ((num_leds - i) / num_leds))  # Smooth green transition
        b = 255 - r - g  # Blue is the remaining part
        np[i] = (r, g, b)
    
    Write()
def run_activity(activity):
    
    params=get_activity_params(activity)
    
    global led_pin,num_pixels,np
    led_pin=set_pin_out(params["strip_led_pin"])
    num_pixels=int(params["led_num"])
    
    np = neopixel.NeoPixel(led_pin,num_pixels)
    print("starting 'Luminous Play: LED light magic' activity")
    while True:
        irdata=get_IR_data()
        LED(irdata)
       



