from imports import *

fire_sensor=Pin(FIRE_SENSOR_PIN,Pin.IN,Pin.PULL_DOWN)

def gas_leak_detection_fun():
    
    project_configs=get_project_config_data("08 Automatic gas leak detecion")  
    gas_sensor=set_pin_in(project_configs["sensor_pin"])
    gas_sensor_trig=get_trig_state(project_configs["sensor_active_state"])
    motor_pin_A=set_pin_out(project_configs["fan_pin_A"])
    motor_pin_B=set_pin_out(project_configs["fan_pin_B"])
    
    while True:
        motor_pin_A.value(0)
        motor_pin_B.value(0)
        while(gas_sensor.value()==gas_sensor_trig):
            oled_three_data(2,2,2,"CAUTION","Gas Leak","Detected")
            disp_seq_str(["FIRE"],0)
            motor_pin_B.value(1)
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
    
    
    