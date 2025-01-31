
# ******************SentiLume: Intelligent street illumination************************

from imports import *
from utils import get_activity_params





def run_activity(activity):
    params=get_activity_params(activity)
     
    sensor=set_pin_in(params["sensor_pin"])
    sensor_trig=get_trig_state(params["sensor_active_state"])
    
    print("starting 'SentiLume: Intelligent street illumination ' activity")
    
    

    last=0
    while True: 
        if sensor.value() ==sensor_trig:
            if last==0:
                all_set_color(255,255,255)
                disp_seq_str(["MOON"],0)
#                 oled_log("Street Light ON")
                oled_three_data(2,2,2,"Street","Light","ON")
                last=1
                one_beep()
        else:
            if last==1:
                all_set_color(0,0,0)
                disp_seq_str(["SUN"],0)
#                 oled_log("Street Light OFF")
                oled_three_data(2,2,2,"Street","Light","OFF")
                last=0
                one_beep()
        time.sleep(.5)
     


