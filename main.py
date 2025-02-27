# Author: Adith Pillai
# Language: MicroPython
# Project Name: RoboNinjaz

import machine
import time
from local_host.esp_as_AP import *

from local_host.webServer import *
from drivers.display import *
from drivers.ir_decode import *
from ir_rx.nec import NEC_8
from ir_rx.print_error import print_error
from process.run_activity import run
import _thread
from utils import get_jsonvalue_from_file


# if TOUCH1.value()==True and TOUCH2.value()==True:
#     enable_AP()
# elif  TOUCH1.value()==True and TOUCH2.value()==False:
#     runWebServer()
    




# ir = NEC_8(pin_ir, callback) # Instantiate the NEC_8 receiver
# # Show debug information
# ir.error_function(print_error)


    

    
# proj=str(get_parameter("PROJECT"))  #Get selected project name from file
proj=get_jsonvalue_from_file("schema.dat","PROJECT")
print(f"project_name-->{proj}")






try:
    run(proj)
#     _thread.start_new_thread(run, (proj,))
    

    
    
except KeyboardInterrupt:
    pass
