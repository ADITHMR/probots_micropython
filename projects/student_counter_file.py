from pin_mapping import *
from imports import *

counter=0	#counter
TIMEOUT = 1  # Timeout in seconds

def student_counter_fun():
    global counter

    # Read the IR values
    sensor1 = IR_LDR1.value()
    sensor2 = TOUCH1.value()
    
    if sensor1 ==False:
        print("LDR1 detected object!")
        time.sleep(0.1)  # Debounce delay to prevent multiple counts
        
        start_time = time.time()  # Record the current time
        while time.time() - start_time < TIMEOUT:
            
            # Wait for the second LDR to detect the object
            sensor2 = TOUCH1.value()
            if sensor2  ==True:
                print("LDR2 detected object!")
                counter += 1
                two_beep()
                print(f"Head Count: {counter}")
                oled_two_data(2,3,"Count",str(counter))
                disp_seq_str([str(counter)],0)
                while sensor2  ==True:
                    pass
                return
        print("Timeout: Second LDR did not detect object in time.")
    if sensor2 ==True:
        
        print("LDR1 detected object!")
        time.sleep(0.1)  # Debounce delay to prevent multiple counts
        
        start_time = time.time()  # Record the current time
        while time.time() - start_time < TIMEOUT:
            
            # Wait for the second LDR to detect the object
            sensor1 = IR_LDR1.value()
            if sensor1  ==False:
                print("LDR2 detected object!")
                if counter>0:
                    counter -= 1
                    one_beep()
                print(f"Head Count: {counter}")
                oled_two_data(2,3,"Count",str(counter))
                disp_seq_str([str(counter)],0)
                while sensor1  ==False:
                    pass
                return
        print("Timeout: Second LDR did not detect object in time.")
   
