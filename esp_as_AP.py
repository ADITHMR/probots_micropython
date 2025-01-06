from web_page_AP import *
from file_mgr import *
from utils import *
from time import sleep
from display import *

import json
try:
  import usocket as socket
except:
  import socket

import network
import ustruct
import esp
esp.osdebug(None)
import ubinascii
import gc
gc.collect()


REPLACE_FOR_SPACE="@@!##"
def enable_AP():
    disp_scroll_str('Access point')
    sleep(1)
    
    
    
    ssid = 'Prosol AP'
    password = '12341234'

    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid=ssid, password=password)
    ap.ifconfig(('192.168.1.1', '255.255.255.0', '192.168.1.1', '192.168.1.1'))
    disp_scroll_str('IP Address -192-168-1-1')
    sleep(1)
    while ap.active() == False:
      pass
    disp_scroll_str('Conn Success')
    print('Connection successful')
    print(ap.ifconfig())

    

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 80))
    s.listen(5)

    while True:
        conn, addr = s.accept()
        print('Got a connection from %s' % str(addr))
        request = conn.recv(1024)
        #   print('Content = %s' % str(request))
        request_str=str(request)
#         print(request_str)
      # Check if it's a POST request
        if "POST" in request_str:
            # Extract SSID and Password from the request
            try:
                start_ssid = request_str.find("ssid=") + 5
                end_ssid = request_str.find("&", start_ssid)
                ssid = request_str[start_ssid:end_ssid] if end_ssid != -1 else request_str[start_ssid:]

                start_password = request_str.find("password=") + 9
                password = request_str[start_password:].split(" ")[0]
                password=password[:-1]

                ssid=url_decode(ssid)
                password=url_decode(password)
                
                REPLACE_FOR_SPACE
                if ssid.find(REPLACE_FOR_SPACE) != -1:
                    ssid=ssid.replace(REPLACE_FOR_SPACE," ")
                if password.find(REPLACE_FOR_SPACE) != -1:
                    password=password.replace(REPLACE_FOR_SPACE," ")
                # Print the received SSID and password
                print("Received SSID:", ssid)
                print("Received Password:", password)
                
                set_parameter("SSID",ssid)
                set_parameter("PASSWORD",password)
                
                # Respond with a success message
                conn.send('HTTP/1.1 200 OK\r\n')
                conn.send('Content-Type: text/html\r\n')
                conn.send('\r\n')
                conn.send("<html><body><h2>Data Received Successfully! Reset the module.</h2></body></html>")
                conn.close()

            except Exception as e:
                print("Error:", e)
                conn.send('HTTP/1.1 400 Bad Request\r\n')
                conn.send('Content-Type: text/html\r\n')
                conn.send('\r\n')
                conn.send("<html><body><h2>Error processing request!</h2></body></html>")
                
        else:
            response = web_page_AP()
            conn.send(response)
            conn.close()
#       if req_data[7:18]=="submit_wifi":
#           print("success")
#           data=req_data[24:].split(' ')
#           data=data[0]
#           ssid=url_decode(data.split('&')[0])
#           password=url_decode(data.split('&')[1].split('=')[1])
#           print("SSID="+str(ssid))
#           print("Pass="+str(password))
#           set_parameter("SSID",str(ssid))
#           set_parameter("PASSWORD",str(password))
          

   
