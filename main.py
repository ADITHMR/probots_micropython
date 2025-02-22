# Author: Adith Pillai
# Language: MicroPython
# Project Name: RoboNinjaz

import machine,time
from local_host.esp_as_AP import*
from local_host.webServer import*
from drivers.display import*
from drivers.ir_decode import*
from ir_rx.nec import NEC_8
from ir_rx.print_error import print_error
from process.run_activity import run
import _thread
proj=str(get_parameter('PROJECT'))
print(f"project_name-->{proj}")
try:run(proj)
except KeyboardInterrupt:ir.close()
