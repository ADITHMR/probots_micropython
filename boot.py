
from local_host.esp_as_AP import enable_AP
from pin_mapping import TOUCH1,TOUCH2
from local_host.webServer import runWebServer

if TOUCH1.value()==True and TOUCH2.value()==True:
    enable_AP()
elif  TOUCH1.value()==True and TOUCH2.value()==False:
    runWebServer()
    
from process.save_html import save_html
from process.fetch_projects import fetch_projects






fetch_projects()
save_html()