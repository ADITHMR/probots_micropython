import time
from machine import Pin




from local_host.connect_wifi import  connect_wifi
from drivers.oled import *
oled_two_data(1,1,"System","Booting")
# from machine_id import get_update_flag
# time.sleep(.5)
TOUCH1=Pin(14,Pin.IN)
TOUCH2=Pin(15,Pin.IN)
if TOUCH1.value()==True and TOUCH2.value()==True:
    from local_host.esp_as_AP import runAP
    runAP()
elif  TOUCH1.value()==True and TOUCH2.value()==False:
    oled_two_data(1,1,"Web server","Mode")
    wifi_connected=connect_wifi()
    if wifi_connected:
        oled_log("Web Server")
        from local_host.webServer import runWebServer
        
        time.sleep(1)
        runWebServer()

wifi_connected=connect_wifi()
import json
if wifi_connected:
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
if wifi_connected:
    import process.api as api
    api=api.Api()
    login=api.user_login()
    if login:
        oled_two_data(1,1,"User","Logged in")
        time.sleep(.5)
        oled_two_data(1,1,"Aquiring","Projects")
        api.get_projects()
        oled_two_data(1,1,"Aquire","Completed")
    else:
        oled_two_data(1,1,"Login","Failed")

# time.sleep(.5)
from process.save_html import save_html



oled_two_data(1,1,"Setting up","Activities")
# time.sleep(.5)
# fetch_projects()
oled_two_data(1,1,"Updating","Pages")
# time.sleep(.5)
save_html()
oled_two_data(1,1,"Starting","Activities")
# time.sleep(.5)