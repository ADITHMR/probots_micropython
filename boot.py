# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()


from esp_as_AP import *
from pin_mapping import *
from  projectList import  *

# if boot_sw1.value()==False and boot_sw2.value()==False:
#     enable_AP()
# elif  boot_sw1.value()==False and boot_sw2.value()==True:
#     enable_project_selector()
    