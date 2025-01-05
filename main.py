# Author: Adith Pillai
# Language: MicroPython
# Project Name: Probots

import machine
import time
from esp_as_AP import *
from pin_mapping import *
from project_config import *
from projects import *
from display import *


if boot_sw1.value()==False and boot_sw2.value()==False:
    enable_AP()
elif  boot_sw1.value()==False and boot_sw2.value()==True:
    enable_project_selector()
    
proj=get_parameter("PROJECT")
print(proj)
disp_seq_str(['p'+str(proj)],1)
while True:
    runPproject(proj)
    
    