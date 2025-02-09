# ********************AutoGate: Self opening gate**********************
from machine import Pin
import time
from servo import Servo
from drivers.oled import oled_two_data
from neopixel import NeoPixel
from analog_buzzer import AnalogBuzzer
from utils import get_activity_params
from pin_mapping import get_trig_state




is_led_used=None
buzzer_pin=None
total_counts = None
timeout_duration = None
num_pixels=None
led_strip_pin=None
np=[]
buzzer=None
servo_mtr=None


    
def run_activity(activity):    
    oled_two_data(1,2,"Running","AutoGate")
    time.sleep(2)
    
    global np, is_led_used,buzzer_pin,total_counts,buzzer
    global timeout_duration ,num_pixels,led_strip_pin,servo_mtr
    # -----------------------------------
    # User Defined Datas
#     is_led_used=1
# # Initialize IR sensors and servo motor
#     sensor_in_pin=36
#     sensor_out_pin=39
#     servo_mtr_pin=33
#           # Servo motor control
#     buzzer_pin=32
#     timeout_duration = 5 
#     num_pixels=5
#     led_strip_pin=5
    params=get_activity_params(activity)
#     print(params)
    
    sensor_in_pin=int(params["sensor_in_pin"])
    sensor_out_pin=int(params["sensor_out_pin"])
    servo_mtr_pin=int(params["servo_mtr_pin"])
          # Servo motor control
    buzzer_pin=int(params["buzzer_pin"])
    timeout_duration = int(params["timeout_duration"])
    num_pixels=int(params["num_pixels"])
    led_strip_pin=int(params["led_strip_pin"])
    sensor_out_active_state=get_trig_state(params["sensor_out_active_state"])
    sensor_in_active_state=get_trig_state(params["sensor_in_active_state"])
    # -----------------------------------
    sensor_in = Pin(sensor_in_pin, Pin.IN)  # IR sensor for entry
    sensor_out = Pin(sensor_out_pin, Pin.IN) # IR sensor for exit
    servo_mtr = Servo(servo_mtr_pin)
    
    
    buzzer = AnalogBuzzer(pin_number=buzzer_pin)
    buzzer.play_tone(2000, 2)
    
    led_strip=Pin(led_strip_pin, Pin.IN)
    np = NeoPixel(led_strip,num_pixels)
    gate_close()
    total_counts = 0
#     red(num_pixels)
    is_entering = 0
    is_exiting = 0

    # Main loop
    while True:
        try:
            start_time = time.time()  

            if is_exiting == 0 and is_entering == 0:
                if sensor_in.value() == sensor_in_active_state:  
        #             time.sleep(0.1)  
                    print("Student Entering.")
                    oled_two_data(2,1,"Entering","-----")
                    gate_open()
                    is_entering = 1 

                elif sensor_out.value() == sensor_out_active_state:  
        #             time.sleep(0.1) 
                    print("Student Exiting.")
                    oled_two_data(2,1,"Exiting","-----")
                    gate_open()
                    is_exiting = 1  

            else:
              
                while time.time() - start_time < timeout_duration:
                    if is_exiting == 1:
                        if sensor_in.value() == sensor_in_active_state:
                            while sensor_in.value() == sensor_in_active_state:
                                pass
        #                     time.sleep(0.1)  
                            total_counts -= 1
                            print(f"Total count = {total_counts}")
                            oled_two_data(1,2,"Count",str(total_counts))
                            gate_close()  
                            is_exiting = 0  
                            
                            
#                             time.sleep(.2)  
                            break  
                    elif is_entering == 1:
                        if sensor_out.value() == sensor_out_active_state:
                            while sensor_out.value() == sensor_out_active_state:
                                pass
        #                     time.sleep(0.1) 
                            total_counts += 1
                            print(f"Total count = {total_counts}")
                            oled_two_data(1,2,"Count",str(total_counts))
                            gate_close() 
                            is_entering = 0  
                            
                            
#                             time.sleep(.2)  
                            break  
                
              
                if time.time() - start_time >= timeout_duration:
                    print("Timeout! Closing gate.")
                    gate_close()
                    oled_two_data(2,1,"Timeout","Gate Closed")
                    is_entering = 0
                    is_exiting = 0
                    time.sleep(1)  

            time.sleep(0.1)
        except Exception as e:
            print(f"Error in Autogate activity(): {e}")
def led_write():
    np.write()
    
def red(num_pixels):
    for i in range(num_pixels):
        np[i] = (255,0,0)
        led_write()
def green(num_pixels):
    for i in range(num_pixels):
        np[i] = (0,255,0)
        led_write()

def gate_open():
    global num_pixels
    servo_mtr.move(90)
    green(num_pixels)
    buzzer.play_tone(2500, .5)

def gate_close():
    global num_pixels
    servo_mtr.move(180)
    red(num_pixels)
    buzzer.play_tone(2500, .5)
    
# run_activity("activity3")
