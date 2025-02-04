import time


from pin_mapping import TOUCH1,TOUCH2
from local_host.connect_wifi import  connect_wifi
# from machine_id import get_update_flag


if TOUCH1.value()==True and TOUCH2.value()==True:
    from local_host.esp_as_AP import enable_AP
    enable_AP()
elif  TOUCH1.value()==True and TOUCH2.value()==False:
    from local_host.webServer import runWebServer
    from drivers.oled import oled_log
    oled_log("Web server ")
    oled_log("Mode ")
    runWebServer()

connect_wifi()
import json
with open('schema.dat', 'r') as f:
    data = json.load(f)
temp=str(data["update_flag"]) 
print(f"update_status={temp}")
if temp=="True":
    print("Starting Update")
    try:
        from drivers.oled import oled_log
        oled_two_data(1,3,"Starting","Update")
    except Exception as e:
        print("OLED Error:", e)
    from ota_update import run_update
    run_update()
    
    
time.sleep(1)

from process.save_html import save_html
from process.fetch_projects import fetch_projects






fetch_projects()
save_html()