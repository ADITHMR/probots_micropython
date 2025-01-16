from imports import *

def fun_with_led_fun():
    
    while True:
        print(f"data={get_IR_data()}")
        LED(get_IR_data())
