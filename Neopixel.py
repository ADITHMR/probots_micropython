# from machine import Pin
# from pin_mapping import *
# import neopixel
# #NeoPixel NP(led,3)
# NP= neopixel.NeoPixel(led,3)
# NP[1]= {255,0,0}
# NP.write()
import machine
import neopixel
import time
import random
#import colourwheel
#import colour
num_pixels=10
Red=0
Green=0
Blue=0
i=0
k=0
intensity=255
switch_val=0
pin = machine.Pin(2)
np = neopixel.NeoPixel(pin,num_pixels)
print(1)
a=1
b=c=0
def clear():
<<<<<<< Updated upstream
    for i in range(num_pixels):
=======
    for i in range(length):
>>>>>>> Stashed changes
        np[i]=(0,0,0,0)
    np.write()
def F_ON(Red,Green,Blue):
    for i in range(num_pixels):
        np[i]=(Red,Green,Blue)
    np.write()
def mode0():
    color=0xFF00
    color =color&0xFFFFFF00
    k=0
    while k<(num_pixels):
        for i in range(num_pixels):    
            np[i]=((color&0xFF000000)>>24,(color&0x00FF0000)>>16,(color&0x0000FF00)>>8)
            np.write()
            #print(color)
            #print(i)
            color=color*256
            time.sleep(0.1)
            if color > 0x100000000:
                color = 0xff00
            k=k+1
def mode1():
    for i in range(255):
        if((i%3)==0):
            a=1
            b=0
            c=0
        elif((i+1)%3==0):
            b=1
            a=0
            c=0
        elif((i+2)%3==0):
            b=0
            a=0
            c=1 
        np[0]=(i*a,i*b,i*c)
        np[1]=(i*b,i*c,i*a)
        np[2]=(i*c,i*a,i*b)
        np[3]=(i*a,i*b,i*c)
        np[4]=(i*b,i*c,i*a)
        np[5]=(i*c,i*a,i*b)
        np[6]=(i*a,i*b,i*c)   
        np.write()
        time.sleep(0.05)
        #print(i)
        #print("ok")
        #time.sleep(1)
def mode2():
    for i in range(255):
        if((i%3)==0):
            a=1
            b=0
            c=0
        elif((i+1)%3==0):
            b=1
            a=0
            c=0
        elif((i+2)%3==0):
            b=0
            a=0
            c=1   
        np[0]=(i*a,i*b,i*c)
        np[1]=(i*b,i*c,i*a)
        np[2]=(i*c,i*a,i*b)
        np[3]=(i*a,i*b,i*c)
        np[4]=(i*b,i*c,i*a)
        np[5]=(i*c,i*a,i*b)
        np[6]=(i*a,i*b,i*c)   
        np.write()
        time.sleep(.01)
        #print(i)
        time.sleep(1)
def ON(Led,Red,Green,Blue):
    np[Led]=(Blue,Red,Green)
    np.write()
def mode3():
    color=255,0,0,0,255,0,0,0,255,255,255,0,0,255,255,255,255,255
    print (len(color))
    for i in range(len(color)-3):        
        Red=color[i]
        Green=color[i+1]
        Blue=color[i+2]
        i=i+3
        for k in range(num_pixels):
           ON(k,Red,Green,Blue)
           time.sleep(.1)
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
<<<<<<< Updated upstream
        for k in range(num_pixels):
            clear()
            ON(k,Red,Green,Blue)
            time.sleep(.1)
        for k in range(num_pixels):
            clear()
            ON(num_pixels-k-1,Red,Green,Blue)
=======
        for k in range(length):
            clear()
            ON(k,Red,Green,Blue)
            time.sleep(.1)
        for k in range(length):
            clear()
            ON(length-k-1,Red,Green,Blue)
>>>>>>> Stashed changes
            time.sleep(.1)
def mode5():
    color=255,0,0,0,255,0,0,0,255,255,255,0,0,255,255,255,255,255
    print (len(color))
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
        for k in range(num_pixels):
            F_ON(Red,Green,Blue)
            ON(num_pixels-k-1,0,0,0)
#             if(k>0):
#                 ON(k-1,0,0,0)
            time.sleep(.1)
def mode6():
    color=255,0,0,0,255,0,0,0,255,255,255,0,0,255,255,255,255,255
    for i in range(len(color)-3):        
        Red=color[i]
        Green=color[i+1]
        Blue=color[i+2]
        i=i+3
<<<<<<< Updated upstream
        for k in range(num_pixels):
=======
        for k in range(length):
>>>>>>> Stashed changes
            clear()
            ON(k,Red,Green,Blue)
            if(k+1<num_pixels):
                ON(k+1,Red,Green,Blue)   
            time.sleep(.2)
<<<<<<< Updated upstream
        for k in range(num_pixels):
            clear()
            ON(num_pixels-k-1,Red,Green,Blue)
=======
        for k in range(length):
            clear()
            ON(length-k-1,Red,Green,Blue)
>>>>>>> Stashed changes
            if(k>0):
                ON(k-1,Red,Green,Blue) 
            time.sleep(.2)
def mode7():
    l=0
    color=255,0,0,0,255,0,0,0,255,0,255,255,255,255,0,255,255,255
    print (len(color))
    clear()
    for i in range(len(color)-3):
        Red=color[i]
        Green=color[i+1]
        Blue=color[i+2]            
        i=i+3
        for z in range(10):
<<<<<<< Updated upstream
            for k in range(num_pixels):
=======
            for k in range(length):
>>>>>>> Stashed changes
                clear()
                ON(k,Red,Green,Blue)
                time.sleep(.1)
            clear()
            time.sleep(.05)
def mode8(): #random
    wait=0.1
    print(num_pixels)
    for i in range(num_pixels):        
        if random.randint(0, 10) > 8:  # 20% chance of twinkling
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            np[i] = color
        else:
            np[i] = (0, 0, 0)  # Turn off some LEDs
    np.write()
    time.sleep(wait)
def mode9():  #wave
    wait=0.05
    for j in range(num_pixels * 2):
        for i in range(num_pixels):
            if (i + j) % num_pixels == 0:
                np[i] = (255, 0, 0)  # green color
            else:
                np[i] = (0, 0, 0)  # Turn off the LED
        np.write()
        time.sleep(wait)
def mode10():
    wait=0.1
    for i in range(num_pixels):
        np[i] = (255, 255, 255)  # White light
        np.write()
        time.sleep(wait)
        np[i] = (0, 0, 0)  # Turn off the light

    for i in range(num_pixels - 1, -1, -1):
        np[i] = (255, 255, 255)
        np.write()
        time.sleep(wait)
        np[i] = (0, 0, 0)
import random

def mode11():#fire_effect
    wait=0.05
    for i in range(num_pixels):
        red = random.randint(0, 255)
        green = random.randint(0, red)  # Green is always less than or equal to red
        blue = random.randint(0, green)  # Blue is always less than or equal to green
        np[i] = (blue,red,green)  # Simulate fire color
    np.write()
    time.sleep(wait)
def mode12(): # pulse
    wait=0.01
    for brightness in range(0, 255, 5):  # Increasing brightness
        for i in range(num_pixels):
            np[i] = (brightness, 0, 0)  # Red color with variable brightness
        np.write()
        time.sleep(wait)
    for brightness in range(255, 0, -5):  # Decreasing brightness
        for i in range(num_pixels):
            np[i] = (brightness, 0, 0)  # Red color with variable brightness
        np.write()
        time.sleep(wait)
def mode13(): #rainbow_chase
    wait=0.1
    for j in range(256):  # Number of color shifts (one full rainbow)
        for i in range(num_pixels):
            color = wheel((i + j) & 255)  # Shift color based on position
            np[i] = color
        np.write()
        time.sleep(wait)
def mode14():#full_color_fade
    print("Fade in colors")
    wait=0.2
    for j in range(256):
        for i in range(num_pixels):
            np[i] = (j, 0, 0)  # Red fades in
        np.write()
        time.sleep(wait)
        
        for i in range(num_pixels):
            np[i] = (0, j, 0)  # Green fades in
        np.write()
        time.sleep(wait)
        
        for i in range(num_pixels):
            np[i] = (0, 0, j)  # Blue fades in
        np.write()
        time.sleep(wait)
      
    print("colors")
    for j in range(255, -1, -1):
        for i in range(num_pixels):
            np[i] = (j, 0, 0)  # Red fades out
        np.write()
        time.sleep(wait)
        
        for i in range(num_pixels):
            np[i] = (0, j, 0)  # Green fades out
        np.write()
        time.sleep(wait)
        
        for i in range(num_pixels):
            np[i] = (0, 0, j)  # Blue fades out
        np.write()
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

def LED(mode):
    print(mode)
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
while True:
    print("clear")
    clear()
    #time.sleep(0.1)
    LED(13)
    #time.sleep(0.1)
    #clear()
    
