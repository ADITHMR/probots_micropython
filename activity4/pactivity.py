# *********************CountMaster: Student headcount Tracker********

from pin_mapping import *
from imports import *
from utils import get_activity_params



# Constants
TIMEOUT = 3  # Timeout in seconds
counter = 0  # Initialize the student count

def run_activity(activity):
    params=get_activity_params(activity)
   
    
    # Initialize sensors 
    sensor1_pin = set_pin_in(params["sensor1_pin"])
    sensor2_pin = set_pin_in(params["sensor2_pin"])
    
    sensor_1_state = get_trig_state(params["sensor1_active_state"])
    sensor_2_state = get_trig_state(params["sensor2_active_state"])
    global counter
    print("Started 'CountMaster: Student headcount Tracker' activity")
    # Read the IR values continuously
    while True:
        sensor1 = sensor1_pin.value()  # Check the first IR sensor (LDR1)
        sensor2 = sensor2_pin.value()   # Check the second IR sensor (LDR2)
        
        if sensor1 == sensor_1_state:  # Object detected by LDR1
            print("LDR1 detected object!")
            time.sleep(0.1)  # Debounce delay to prevent multiple counts

            start_time = time.time()  # Record the current time
            while time.time() - start_time < TIMEOUT:
                # Wait for the second LDR to detect the object
                sensor2 = sensor2_pin.value()
                if sensor2 == sensor_2_state:  # Object detected by LDR2
                    print("LDR2 detected object!")
                    counter += 1  # Increase the count
                    two_beep()  # Beep twice (indicating count)
                    print(f"Head Count: {counter}")
                    oled_two_data(2, 3, "Count", str(counter))  # Update display
                    disp_seq_str([str(counter)], 0)  # Update sequence display
                    while sensor2 == sensor_2_state:
                        sensor2 = sensor2_pin.value()
                    time.sleep(.5)
                    break  # Break out of the timeout loop once count is updated
            else:
                print("Timeout: Second LDR did not detect object in time.")

        if sensor2 == sensor_2_state:  # Object detected by LDR2
            print("LDR2 detected object!")
            time.sleep(0.1)  # Debounce delay to prevent multiple counts

            start_time = time.time()  # Record the current time
            while time.time() - start_time < TIMEOUT:
                # Wait for the first LDR to detect the object
                sensor1 = sensor1_pin.value()
                if sensor1 == sensor_1_state:  # Object detected by LDR1
                    print("LDR1 detected object!")
                    if counter > 0:  # Ensure count doesn't go below 0
                        counter -= 1  # Decrease the count
                        one_beep()  # Beep once (indicating decrement)
                    print(f"Head Count: {counter}")
                    oled_two_data(2, 3, "Count", str(counter))  # Update display
                    disp_seq_str([str(counter)], 0)  # Update sequence display
                    while sensor1 == sensor_1_state:
                        sensor1 = sensor1_pin.value()
                        
                    time.sleep(.5)
                    break  # Break out of the timeout loop once count is updated
            else:
                print("Timeout: Second LDR did not detect object in time.")
            
        
        # Small delay to avoid constant polling (and high CPU usage)
        time.sleep(0.1)


