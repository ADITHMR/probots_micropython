from pin_mapping import *
import time

def runPproject(project_name):
    
    if(project_name==1):
        led.on();
        time.sleep(1)
        led.off()
        time.sleep(1)
    elif(project_name==2):
        led.on();
        time.sleep(.1)
        led.off()
        time.sleep(.1)