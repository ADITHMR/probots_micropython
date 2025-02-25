
is_AP=False
is_Server=False
from drivers.oled import oled_log,oled_two_data
from machine import Pin
import time
TOUCH1=Pin(14,Pin.IN)
TOUCH2=Pin(15,Pin.IN)
from local_host.connect_wifi import  connect_wifi
try:
    
    
    if TOUCH1.value()==True and TOUCH2.value()==True:
#         pass
        is_AP=True
        oled_two_data(1,1,"Starting","Access Point")
        time.sleep(1)
    elif  TOUCH1.value()==True and TOUCH2.value()==False:
        is_Server=True
        
        oled_two_data(1,2,"Starting","Server")
#         time.sleep(1)
    oled_two_data(1,1,"System","Booting")
    

   
except Exception as e:
        print("Error boot() --import files error:",e, e.args)
import process.api as api
from local_host.esp_as_AP import runAP
from local_host.webServer import runWebServer
import json

from ota_update import run_update
from process.save_html import save_html
import gc
# from machine_id import get_update_flag
# time.sleep(.5)

if is_AP:
    try:
        runAP()
    except Exception as e:
        print("Error Boot() RunAP:",e, e.args)
wifi_connected=connect_wifi()
if  is_Server:
    oled_two_data(1,1,"Web server","Mode")
    
    if wifi_connected:
        oled_log("Web Server")
        
        
        time.sleep(1)
        runWebServer()


gc.collect()
if wifi_connected:
    with open('schema.dat', 'r') as f:
        data = json.load(f)
    temp=str(data["update_flag"]) 
    print(f"update_status={temp}")
    if temp=="True":
        print("Starting Update")
    #     time.sleep(.5)
        try:
            
            oled_two_data(1,1,"Starting","Update")
        except Exception as e:
            print("OLED Error:", e)
        
        run_update()
gc.collect()
if wifi_connected:
    
    api=api.Api()
    login=api.user_login()
    if login:
        oled_two_data(1,1,"User","Logged in")
        time.sleep(.5)
        oled_two_data(1,1,"Aquiring","Projects")
        api.get_projects()
        time.sleep(.5)
        oled_two_data(1,1,"Aquire","Completed")
    else:
        oled_two_data(1,1,"Login","Failed")
gc.collect()
# time.sleep(.5)




oled_two_data(1,1,"Setting up","Activities")
# time.sleep(.5)
# fetch_projects()
oled_two_data(1,1,"Updating","Pages")
# time.sleep(.5)
if wifi_connected:
    save_html()
gc.collect()
oled_two_data(1,1,"Starting","Activities")
# time.sleep(.5)