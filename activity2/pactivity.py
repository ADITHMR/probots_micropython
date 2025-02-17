
# ******************SentiLume: Intelligent street illumination************************

from imports import *
from utils import get_activity_params
from analog_buzzer import AnalogBuzzer






def run_activity(activity):
    params=get_activity_params(activity)
     
    sensor=set_pin_in(params["sensor_pin"])
    sensor_trig=get_trig_state(params["sensor_active_state"])
    
    print("starting 'SentiLume: Intelligent street illumination ' activity")
    
    buzzer_enable=params["buzzer_enable"]
    buzzer_pin=int(params["buzzer_pin"])
    
    if buzzer_enable=="Enabled":
        buzzer_enable=True
    else:
        buzzer_enable=False
    buzzer = AnalogBuzzer(pin_number=buzzer_pin,enOrDi=buzzer_enable)
    buzzer.play_tone(2000, 1)
    last=0
    while True: 
        if sensor.value() ==sensor_trig:
            if last==0:
                all_set_color(255,255,255)
                disp_seq_str(["MOON"],0)
#                 oled_log("Street Light ON")
                oled_three_data(2,2,2,"Street","Light","ON")
                last=1
                buzzer.play_tone(2000, .2)
        else:
            if last==1:
                all_set_color(0,0,0)
                disp_seq_str(["SUN"],0)
#                 oled_log("Street Light OFF")
                oled_three_data(2,2,2,"Street","Light","OFF")
                last=0
                buzzer.play_tone(2000, .2)
        time.sleep(.1)
     
# run_activity("activity2")

