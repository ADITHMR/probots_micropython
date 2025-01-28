from imports import *

def fun_with_led_fun():
    
    project_configs=get_project_config_data("01 Fun with LED Lights")
    
    num=int(project_configs["led_num"])
    
    
    while True:
        set_color_for(num,200,150, 20)
#         print(f"data={get_IR_data()}")
#         LED(get_IR_data())

