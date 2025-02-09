import time


from pin_mapping import TOUCH1,TOUCH2
from local_host.connect_wifi import  connect_wifi
from drivers.oled import *
oled_two_data(1,1,"System","Booting")
# from machine_id import get_update_flag
# time.sleep(.5)

if TOUCH1.value()==True and TOUCH2.value()==True:
    from local_host.esp_as_AP import enable_AP
    enable_AP()
elif  TOUCH1.value()==True and TOUCH2.value()==False:
    from local_host.webServer import runWebServer
    oled_two_data(1,1,"Web server","Mode")
    time.sleep(1)
    runWebServer()

connect_wifi()
import json
with open('schema.dat', 'r') as f:
    data = json.load(f)
temp=str(data["update_flag"]) 
print(f"update_status={temp}")
if temp=="True":
    print("Starting Update")
#     time.sleep(.5)
    try:
        from drivers.oled import oled_log
        oled_two_data(1,1,"Starting","Update")
    except Exception as e:
        print("OLED Error:", e)
    from ota_update import run_update
    run_update()

# time.sleep(.5)
from process.save_html import save_html
from process.fetch_projects import fetch_projects


oled_two_data(1,1,"Setting up","Activities")
# time.sleep(.5)
fetch_projects()
oled_two_data(1,1,"Updating","Files")
# time.sleep(.5)
save_html()
oled_two_data(1,1,"Starting","Activities")
# time.sleep(.5)