


from imports import *





def run_activity():
    project_configs=get_project_config_data("02 Sensor-controlled street light")  
    sensor=set_pin_in(project_configs["sensor_pin"])
    sensor_trig=get_trig_state(project_configs["sensor_active_state"])
    print(f"{project_configs}")
    
    del project_configs
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
     


