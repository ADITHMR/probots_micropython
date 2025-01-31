from imports import *

fire_sensor=Pin(FIRE_SENSOR_PIN,Pin.IN,Pin.PULL_DOWN)

def automatic_fire_detection_fun():
    
    project_configs=get_project_config_data("05 Automatic fire detection system")  
    fire_sensor=set_pin_in(project_configs["sensor_pin"])
    fire_sensor_trig=get_trig_state(project_configs["sensor_active_state"])
    while True:
        while(fire_sensor.value()==fire_sensor_trig):
            oled_three_data(2,2,2,"CAUTION","Fire","Detected")
            disp_seq_str(["FIRE"],0)
            buzzer_on()
            set_color_for(3,255, 0, 0)
            time.sleep(.6)
            buzzer_off()
            set_color_for(3,0, 0, 0)
            time.sleep(.1)
        buzzer_off()
        set_color_for(3,0, 255, 0)
        oled_two_data(1,3,"ALL","SAFE")
        disp_seq_str(["SAFE"],0)
    
    
    