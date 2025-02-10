from pin_mapping import *
import time
from projects.funWithLed_file import  led_strip_fun
from projects.auto_street_light_file import  * #Import all project files here
from projects.student_counter_file import  *
from projects.Temp_measurement_lm35_file import  *
from projects.automatic_door_file import  *
from projects.dig_dist_measurement_file import  *
from projects.automatic_fire_detection_file import *
from projects.gas_leak_detection_file import *
import _thread

from drivers.display import *
from drivers.oled import *
def runProject(project_name):
    
    proj=f"P{project_name[:2]}"
    oled_log('"'+project_name+'"')
    disp_seq_str([proj],1)
    
    if(project_name=="01 Fun with LED Lights"):
        led_strip_fun()
        
    elif(project_name=="02 Sensor-controlled street light"):
        auto_street_light_fun()
        
    elif(project_name=="03 Self-opening gate"):
        automatic_door_fun()
        
    elif(project_name=="04 Student headcount Tracker"):
        oled_two_data(2,3,"Count","0")
        disp_seq_str(["0"],0)
        while True:
            student_counter_fun() 
        
    elif(project_name=="05 Automatic fire detection system"):
        _thread.start_new_thread(automatic_fire_detection_fun, ())
        
    elif(project_name=="06 Temperature measurement device"):
        _thread.start_new_thread(Temp_measurement_lm35_fun, ())
        
    elif(project_name=="07 Digital distance measurement"):
        dig_dist_measurement_fun()
    elif(project_name=="08 Automatic gas leak detecion"):
        gas_leak_detection_fun()
        
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

                      
                      
                      
                      