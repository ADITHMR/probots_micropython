# Author: Adith Pillai
# Language: MicroPython
# Project Name: Probots

import machine
import time
from esp_as_AP import *
from pin_mapping import *
from webServer import *
from display import *
from ir_decode import *
from ir_rx.nec import NEC_8
from ir_rx.print_error import print_error
from runProject import *

# Run the web server
runWebServer()
if boot_sw1.value()==False and boot_sw2.value()==False:
    enable_AP()
elif  boot_sw1.value()==False and boot_sw2.value()==True:
    runWebServer()
    



pin_ir = Pin(14, Pin.IN) # IR receiver
ir = NEC_8(pin_ir, callback) # Instantiate the NEC_8 receiver
# Show debug information
ir.error_function(print_error)


    

    
proj=get_parameter("PROJECT")  #Get selected project name from file
print(proj)
disp_scroll_str(str(proj))

while True:
    try:
        runProject(str(proj))
    except KeyboardInterrupt:
        ir.close()
