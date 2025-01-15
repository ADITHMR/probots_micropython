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
length=7
Red=0
Green=0
Blue=0
i=0
k=0
intensity=255
switch_val=0
pin = machine.Pin(2)
np = neopixel.NeoPixel(pin,length)
print(1)
a=1
b=c=0
def clear1():
    for i in range(length):
        np[i]=(0,0,0,0)
    np.write()
def F_ON(Red,Green,Blue):
    for i in range(length):
        np[i]=(Red,Green,Blue)
    np.write()
def mode1():
    print("LEVEL 3")
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
def mode0():
    color=0xFF00
    color =color&0xFFFFFF00
    k=0
    while k<(length):
        for i in range(length):    
            np[i]=((color&0xFF000000)>>24,(color&0x00FF0000)>>16,(color&0x0000FF00)>>8)
            np.write()
            #print(color)
            #print(i)
            color=color*256
            time.sleep(0.1)
            if color > 0x100000000:
                color = 0xff00
            k=k+1
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
        for k in range(length):
           ON(k,Red,Green,Blue)
           time.sleep(.1)
        for k in range(length):
           ON(length-k-1,0,0,0)
           time.sleep(.1)
def mode4():
    color=255,0,0,0,255,0,0,0,255,255,255,0,0,255,255,255,255,255
    for i in range(len(color)-3):        
        Red=color[i]
        Green=color[i+1]
        Blue=color[i+2]
        i=i+3
        for k in range(length):
            clear1()
            ON(k,Red,Green,Blue)
            time.sleep(.1)
        for k in range(length):
            clear1()
            ON(length-k-1,Red,Green,Blue)
            time.sleep(.1)
def mode5():
    color=255,0,0,0,255,0,0,0,255,255,255,0,0,255,255,255,255,255
    print (len(color))
    for i in range(len(color)-3):        
        Red=color[i]
        Green=color[i+1]
        Blue=color[i+2]
        i=i+3
        for k in range(length):
            F_ON(Red,Green,Blue)
            ON(k,0,0,0)
            #if(k+1<length):
                #ON(k+1,Red,Green,Blue)
            time.sleep(.1)
        for k in range(length):
            F_ON(Red,Green,Blue)
            ON(length-k-1,0,0,0)
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
        for k in range(length):
            clear1()
            ON(k,Red,Green,Blue)
            if(k+1<length):
                ON(k+1,Red,Green,Blue)   
            time.sleep(.2)
        for k in range(length):
            clear1()
            ON(length-k-1,Red,Green,Blue)
            if(k>0):
                ON(k-1,Red,Green,Blue) 
            time.sleep(.2)
def mode7():
    l=0
    color=255,0,0,0,255,0,0,0,255,0,255,255,255,255,0,255,255,255
    print (len(color))
    clear1()
    for i in range(len(color)-3):
        Red=color[i]
        Green=color[i+1]
        Blue=color[i+2]            
        i=i+3
        for z in range(10):
            for k in range(length):
                clear1()
                ON(k,Red,Green,Blue)
                time.sleep(.1)
            clear1()
            time.sleep(.05)
        
def LED(mode):
    if(mode==0):
        while True:
            mode0()
    elif(mode==1):
        while True:
            print("LEVEL 2")
            mode1()
    elif(mode==2):
        while True:
            mode2()
    elif(mode==3):
        while True:
            mode3()
    elif(mode==4):
        while True:
            mode4()
    elif(mode==5):
        while True:
            mode5()
    elif(mode==6):
        while True:
            mode6()
    elif(mode==7):
        while True:
            mode7()
    elif(mode==8):
        while True:
            mode8()
    elif(mode==9):
        while True:
            mode9()
# while True:
#     print("clear")
#     clear1()
#     #time.sleep(0.1) 
#     print("mode0")
#     LED(0)
#     #time.sleep(0.1)
#     #clear1()
    
