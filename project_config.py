
import socket
import network
import machine
from web_page import *
import time
from file_mgr import *
import json
from esp_as_AP import *
from pin_mapping import *
from display import *

def enable_project_selector():
        
    led.off()
    WIFI_SSID=""
    WIFI_PASSWORD=""
    ##################################################
    ### OPEN FILE AND GET SSID AND PASSWORD
    WIFI_SSID=str(get_parameter("SSID"))
    WIFI_PASSWORD=str(get_parameter("PASSWORD"))
    
    ############################################

    sta = network.WLAN(network.STA_IF)
    if not sta.isconnected():
        print(f"Connecting to the network....with ssid={WIFI_SSID}")
        sta.active(True)
        sta.connect(WIFI_SSID, WIFI_PASSWORD)
        disp_scroll_str("CONNecting")
        while not sta.isconnected():
            pass
        print('Network config:', sta.ifconfig())
        disp_seq_str(["DONE"],2)
       
        disp_scroll_str('IP Address '+sta.ifconfig()[0].replace('.','-'))
       
        

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 80))  # Specify the port number (80 for HTTP)
    s.listen(50)




    def handle_callback(timer):
        led.value(not led.value())




    while True:
        # Socket accept()
        try:
            conn, addr = s.accept()
            print("Got connection from %s" % str(addr))

            # Socket receive()
            request = conn.recv(1024)
            print("")
            print("")
            

            # Socket send()
            request = str(request)
            params = {}
            if "?" in request:
                query_string = request.split("GET /")[1].split(" HTTP")[0]
                
                if "?" in query_string:
                    query_string = query_string.split("?")[1]
                    pairs = query_string.split("&")
                    for pair in pairs:
                        key, value = pair.split("=")
                        params[key] = value
                
                print("a")
                if "selectedItem" in params:
                    print("b")
                    data=params["selectedItem"]
                    print("c")
                    data=data.replace("+", " ")
                    print('Content- '+ data )
                    set_parameter("PROJECT",data)
            #         print("Content %s" % request[8:20])
    #                 if request[8:20]=="selectedItem":
    #                     text=data[21:23]
    #                     set_parameter("PROJECT",text)
    #             #         .split(" ", 1)
    #                     print(text)
                    led.value(1)
                    time.sleep(1)
                    led.value(0)
                    print("Success")
                    response=successPage(data)
                    conn.send(response)
                    conn.close()
            
            else:
                try:
                    response = web_page()
                    conn.send('HTTP/1.1 200 OK\n')
                    conn.send('Content-Type: text/html\n')
#             conn.send('Connection: close\n\n')
                    conn.send(response)
                    conn.close()
                except Exception as e:
                  print(f"An error occurred: {e}")
        #           conn.close()
        except Exception as e:
          print(f"An error occurred: {e}")
#           conn.close()
          
        
        
#             

        



