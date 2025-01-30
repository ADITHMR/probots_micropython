import machine
import time
from imports import *



# Function to measure distance
def measure_distance():
    
   
    
    pulse_start=0
    pulse_end=0
    pulse_duration=0
    
    # Send a 10us pulse to the Trigger pin to start the measurement
    trigger_pin.on()
    time.sleep_us(10)  # Delay for 10 microseconds
    trigger_pin.off()

    # Wait for the Echo pin to go high (start of the pulse)
    while echo_pin.value() == 0:
        pulse_start = time.ticks_us()
    
    # Wait for the Echo pin to go low (end of the pulse)
    while echo_pin.value() == 1:
        pulse_end = time.ticks_us()

    # Calculate the pulse duration in microseconds
    pulse_duration = time.ticks_diff(pulse_end, pulse_start)
    
    # Speed of sound is approximately 34300 cm per second at 20°C
    # The time it takes for the sound to travel to the object and back is divided by 2
    distance = (pulse_duration * 0.0343) / 2  # Distance in cm
    return distance

# Main loop
def dig_dist_measurement_fun():
    
    project_configs=get_project_config_data("07 Digital distance measurement")
    global trigger_pin,echo_pin
    trigger_pin=set_pin_out(project_configs["trig_pin"])
    echo_pin=set_pin_in(project_configs["echo_pin"])
    
    while True:
        dist = int(measure_distance())  # Measure the distance
        if dist>100:
            print(f"Distance: {dist} cm")  # Print the distance in cm
            oled_three_data(2,2,2,"Distance",">100","cm")
            disp_seq_str(["High"],0)

        else:
            print(f"Distance: {dist} cm")  # Print the distance in cm
            oled_three_data(2,2,2,"Distance",str(dist),"cm")
            disp_seq_str([str(dist)],0)
#         time.sleep(.5)  # Delay between measurements

# Run the main loop

