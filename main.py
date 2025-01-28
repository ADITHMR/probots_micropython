# Author: Adith Pillai
# Language: MicroPython
# Project Name: Probots

import machine
import time
from local_host.esp_as_AP import *
from pin_mapping import *
from local_host.webServer import *
from display import *
from ir_decode import *
from ir_rx.nec import NEC_8
from ir_rx.print_error import print_error
from runProject import *
import _thread


if TOUCH1.value()==True and TOUCH2.value()==True:
    enable_AP()
elif  TOUCH1.value()==True and TOUCH2.value()==False:
   runWebServer()
    




ir = NEC_8(pin_ir, callback) # Instantiate the NEC_8 receiver
# # Show debug information
# ir.error_function(print_error)


    

    
proj=str(get_parameter("PROJECT"))  #Get selected project name from file
print(f"project_name-->{proj}")






try:

    _thread.start_new_thread(runProject, (proj,))

    
    
except KeyboardInterrupt:
    ir.close()
