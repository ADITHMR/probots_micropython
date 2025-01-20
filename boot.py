# This file is executed on every boot (including wake-boot from deepsleep)
# import esp
# esp.osdebug(None)
#import webrepl
#webrepl.start()


#define MICROPY_REPL_INFO                 (0) // Disable REPL info
import machine

# Disable the REPL by controlling the serial port
machine.Pin(0, machine.Pin.OUT)  # This can disable the REPL serial interface
# sys.exit()  # Exit the REPL

# if boot_sw1.value()==False and boot_sw2.value()==False:
#     enable_AP()
# elif  boot_sw1.value()==False and boot_sw2.value()==True:
#     enable_project_selector()
    