import time


from pin_mapping import TOUCH1,TOUCH2
from local_host.connect_wifi import  connect_wifi


if TOUCH1.value()==True and TOUCH2.value()==True:
    from local_host.esp_as_AP import enable_AP
    enable_AP()
elif  TOUCH1.value()==True and TOUCH2.value()==False:
    from local_host.webServer import runWebServer
    from drivers.oled import oled_log
    oled_log("Web server ")
    oled_log("Mode ")
    runWebServer()
time.sleep(1)
connect_wifi()
from process.save_html import save_html
from process.fetch_projects import fetch_projects






fetch_projects()
save_html()