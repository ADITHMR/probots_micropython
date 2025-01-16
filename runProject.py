from pin_mapping import *
import time
from projects.funWithLed import  * #Import all project files here
from projects.auto_street_light import  * #Import all project files here
from display import *
from oled import *

def runProject(project_name):
    
    proj=f"P{project_name[:2]}"
    oled_log('"'+project_name+'"')
    disp_seq_str([proj],1)
    
    if(project_name=="01 Fun with LED Lights"):
        fun_with_led()
        
    elif(project_name=="02 Sensor-controlled street light"):
        Sensor_controlled_streetlight()
        
    elif(project_name=="03 Self-opening gate"):
        led.on();
        time.sleep(.1)
        led.off()
        time.sleep(.1)
    elif(project_name=="04 Student headcount Tracker"):
        led.on();
        time.sleep(.1)
        led.off()
        time.sleep(.1)
    elif(project_name=="05 Automatic fire detection system"):
        led.on();
        time.sleep(.1)
        led.off()
        time.sleep(.1)
    elif(project_name=="06 Temperature measurement device"):
        led.on();
        time.sleep(.1)
        led.off()
        time.sleep(.1)
    elif(project_name=="07 Digital distance measurement"):
        led.on();
        time.sleep(.1)
        led.off()
        time.sleep(.1)
    elif(project_name=="08 Touchless dustbin"):
        led.on();
        time.sleep(.1)
        led.off()
        time.sleep(.1)
    elif(project_name=="09 Touch operated fan"):
        led.on();
        time.sleep(.1)
        led.off()
        time.sleep(.1)
    elif(project_name=="10 Smart fan"):
        led.on();
        time.sleep(.1)
        led.off()
        time.sleep(.1)
    elif(project_name=="11 Automated Solar tracking system"):
        led.on();
        time.sleep(.1)
        led.off()
        time.sleep(.1)
    elif(project_name=="12 Line follower robot"):
        led.on();
        time.sleep(.1)
        led.off()
        time.sleep(.1)

                      
                      
                      
                      