from imports import *

def fun_with_led():
    
    while True:
        print(f"data={get_IR_data()}")
        LED(get_IR_data())
