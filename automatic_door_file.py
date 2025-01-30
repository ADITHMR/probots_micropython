from machine import Pin, PWM
import time
from process.file_mgr import get_project_config_data
from pin_mapping import set_pin_in,get_trig_state
from drivers.display import disp_seq_str
from drivers.oled import oled_two_data
from drivers.led_strip import all_set_color




# servo_pin=None
# Function to initialize the PWM for the servo
def init_servo():
    global servo
    servo = PWM(servo_pin, freq=50)  # Create PWM object for controlling the servo
    print("PWM initialized for servo.")

# Function to open the gate (move servo to 90 degrees)
def open_gate():
    init_servo()
    Servo(0)  # Adjust the duty cycle to open the gate (angle ~90 degrees)
    print("Gate opened")
    oled_two_data(2,2,"Gate","OPEN")
    disp_seq_str(["OPEN"],0)
    all_set_color(0,255,0)
    stop_pwm()

# Function to close the gate (move servo to 0 degrees)
def close_gate():
    init_servo()
    Servo(180)  # Adjust the duty cycle to close the gate (angle ~0 degrees)
    print("Gate closed")
    disp_seq_str(["CLSE"],0)
    oled_two_data(2,2,"Gate","Closed")
    all_set_color(255,0,0)
    stop_pwm()
    
def Servo(angle):
    servo.duty(int(((angle)/180 *2 + 0.5) / 20 * 1023))
    
# Function to disable the PWM signal for the servo
def stop_pwm():
    servo.deinit()  # Disable PWM on the servo pin
    print("PWM signal disabled")

def automatic_door_fun():
    project_configs = get_project_config_data("03 Self-opening gate")
    
    # Initialize sensors and servo pin
    sensor_1_pin = set_pin_in(project_configs["sensor1_pin"])
    sensor_2_pin = set_pin_in(project_configs["sensor2_pin"])
    
    sensor_1_state = get_trig_state(project_configs["sensor1_active_state"])
    sensor_2_state = get_trig_state(project_configs["sensor2_active_state"])
    
    # Servo pin initialization
    global servo_pin  # Only if necessary, else handle it locally
    servo_pin = int(project_configs["servo_pin"])
    init_servo()  # Initialize servo motor

    TIMEOUT_DURATION = 15  # Timeout duration in seconds
    last_open_time = 0  # Track the time the gate was last opened
    gate_open = False  # Track the state of the gate (open or closed)
    open_direction=0
    # Initial gate closure
    close_gate()
   
    
    while True:
        # Check if either sensor detects an object to open the gate
        if (sensor_1_pin.value() == sensor_1_state or sensor_2_pin.value() == sensor_2_state) and not gate_open:
            if sensor_1_pin.value() == sensor_1_state:
                open_direction=1
            elif sensor_2_pin.value() == sensor_2_state:
                open_direction=2
                
            print("Entry detected! Opening the gate.")
            init_servo()  # Initialize the servo before moving it
            open_gate()   # Open the gate
            gate_open = True  # Mark the gate as open
            last_open_time = time.time()  # Store the current time when the gate opened
            time.sleep(1)  # Add a small delay to avoid multiple triggers

        # If the gate is open, check for timeout or exit
        if gate_open:
            current_time = time.time()
            timeout_display = str(TIMEOUT_DURATION - (current_time - last_open_time))
#             print(f"Time since last open: {current_time - last_open_time}s")
            
            # Update the OLED display with timeout
            oled_three_data(2, 2, 1, "Gate", "OPEN", f"t-out->{timeout_display}")
            disp_seq_str([timeout_display], 0)

            # Check for timeout condition
            if current_time - last_open_time >= TIMEOUT_DURATION:
#                 print(f"Timeout reached ({TIMEOUT_DURATION} seconds)! Closing the gate.")
                oled_two_data(2, 2, "Timeout", "______")
                disp_seq_str(["TOUT"], 0)
                time.sleep(1)
                close_gate()
                gate_open = False  # Mark the gate as closed
                time.sleep(1)  # Add a small delay to avoid multiple triggers

            # Check if the other sensor detects an object to close the gate
            elif (sensor_1_pin.value() == sensor_1_state and sensor_2_pin.value() != sensor_2_state)and open_direction==2:  # If Sensor 1 detects and Sensor 2 does not
                print("Exit detected! Closing the gate.")
                close_gate()
                gate_open = False  # Mark the gate as closed
                open_direction=0
                time.sleep(1)  # Add a small delay to avoid multiple triggers

            elif (sensor_2_pin.value() == sensor_2_state and sensor_1_pin.value() != sensor_1_state)and open_direction==1:  # If Sensor 2 detects and Sensor 1 does not
                print("Exit detected! Closing the gate.")
                close_gate()
                gate_open = False  # Mark the gate as closed
                open_direction=0
                time.sleep(1)  # Add a small delay to avoid multiple triggers
            elif sensor_1_pin.value() != sensor_1_state and sensor_2_pin.value() != sensor_2_state:
                pass
        time.sleep(0.1)  # Polling interval to reduce CPU load

