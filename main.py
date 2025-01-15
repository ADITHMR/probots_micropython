# Author: Adith Pillai
# Language: MicroPython
# Project Name: Probots

import machine
import time
from esp_as_AP import *
from pin_mapping import *
from project_config import *
from display import *
from ir_decode import *
from ir_rx.nec import NEC_8
from ir_rx.print_error import print_error
from runProject import *

<<<<<<< Updated upstream
=======
# Run the web server
# runWebServer()
>>>>>>> Stashed changes

if boot_sw1.value()==False and boot_sw2.value()==False:
    enable_AP()
elif  boot_sw1.value()==False and boot_sw2.value()==True:
    enable_project_selector()
    



pin_ir = Pin(14, Pin.IN) # IR receiver
ir = NEC_8(pin_ir, callback) # Instantiate the NEC_8 receiver
# Show debug information
ir.error_function(print_error)


    

    
proj=get_parameter("PROJECT")  #Get selected project name from file

print(proj)
disp_scroll_str(str(proj))

while True:
    try:
#         print ("level 0")
        runProject(proj)
    except KeyboardInterrupt:
        ir.close()
