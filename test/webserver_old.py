

import socket
import network
from drivers.oled import *
from local_host.project_config_update import *
from process.file_mgr import *
from local_host.web_page import *
import ure
import traceback
from drivers.display import *
import sys
import gc
from utils import url_decode
from test.get_project_page_ import *
from local_host.project_config_update import *
from utils import url_decode
# from ota_update import *

# Global variable for WiFi connection status
wifi_connected = False
wifi_connection_timeout = 5  # Timeout after 10 seconds
wifi_conn_start_time = time.time()

restart = 0

# Connect to WiFi
def connect_wifi():
    global wifi_connected  # Ensure we're using the global variable
    WIFI_SSID = str(get_parameter("SSID"))
    WIFI_PASSWORD = str(get_parameter("PASSWORD"))
    
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASSWORD)
    
    print('Connecting to WiFi...')
    oled_log("Conn to WiFi...")
    disp_scroll_str("CONNecting")
    
    while not wlan.isconnected():
        oled_two_data(1, 2, "Conn to WiFi", str(wifi_connection_timeout - (time.time() - wifi_conn_start_time)))
        if (time.time() - wifi_conn_start_time) > wifi_connection_timeout:
            print("Connection timed out")
            wifi_connected = False
            return
        time.sleep(1)
    
    wifi_connected = True
    print('WiFi connected')
    oled_log("WiFi connected")
    disp_seq_str(["DONE"], 1)
    print('IP Address:', wlan.ifconfig()[0])
    oled_log("IP->")
    oled_log(wlan.ifconfig()[0])
    
    ip_last_byte = wlan.ifconfig()[0].split('.')[3]
    disp_seq_str([str(ip_last_byte)], 1)


# Handle HTTP requests
def handle_request(client):
    restart = False
    client.settimeout(10)
   
    gc.collect()
    free_mem = gc.mem_free()
    used_mem = gc.mem_alloc()
    print(f"Used memory: {used_mem} bytes")
    print(f"Free memory: {free_mem} bytes")
    
    try:
#         client.settimeout(3)  # Timeout in seconds
        data = client.recv(1024)  # Blocking call here but done synchronously
        
        if not data:
            print("Client closed the connection")
            return
        
        request_str = str(data)
        print(request_str)
        
        # Handle different routes
        response = handle_route(request_str, client)
        
        if response:
            client.send(response)
            if html_content is not None:  # Check if html_content exists before deletion
                del html_content
            del response
            gc.collect()
            
                    
            print("response sent")
            
    
    except OSError as e:
        if e.errno == 113:  # ECONNABORTED
            print("Error: Connection aborted by client (ECONNABORTED)")
        else:
            print("OSError:", e)
            traceback.print_exc()
    except Exception as e:
        print("General Error:", e)
        traceback.print_exc()
    finally:
        try:
            client.close()
            print("client close")
            
        except Exception as e:
            print("Error closing client connection:", e)
            traceback.print_exc()


def handle_route(request_str, client):
    if '/hello' in request_str:
        return "HTTP/1.1 200 OK\n\nStatus: Hello There!"
    elif '/reset' in request_str:
        return restartSuccessPage()
    elif 'GET /?project' in request_str:
        datas = get_params(request_str)
#         print(datas)
        update_project_config(datas)
        
        
        return successProjectPage(url_decode(datas['project']))
    elif 'selectedItem=' in request_str and 'POST' in request_str:
        return handle_post_selected_item(request_str)
    elif 'POST /update HTTP' in request_str:
        return handle_firmware_update()
    elif 'GET / HTTP' in request_str:
        return handle_homepage_request()
    elif '/reset' in request_str:
            # Redirect to /newpage
            response = restartSuccessPage()
            client.send(response)
            machine.reset()
            return response
    else:
        return errorPage()
def handle_firmware_update():
    response=None
    with open('local_host/update_firmware.html', 'r') as f:
                response = f.read()
    return response
    

def handle_post_selected_item(request_str):
    match = ure.search(r'selectedItem=([^&]+)', request_str)
    if match:
        selected_option = match.group(1).replace("'", "").replace("+", " ")
        selected_option=url_decode(selected_option)
        response=get_project_html(selected_option)
        return response
    else:
        return errorPage()
    


def handle_homepage_request():
    response = web_page()
    return response


# Start the web server
def start_server():
    wlan = network.WLAN(network.STA_IF)
    ip_address = wlan.ifconfig()[0]
    
    # If the IP is still unknown, print an error and return
    if ip_address == '0.0.0.0':
        print("Error: Unable to get IP address.")
        return
    
    addr = socket.getaddrinfo(ip_address, 80)[0][-1]
    s = socket.socket()
    
    try:
        s.bind(addr)
        s.listen(1)
        print('Listening on', addr)

        while True:
            try:
                client, addr = s.accept()
                print('Client connected from', addr)
                handle_request(client)
                time.sleep(.1)
            
            except Exception as e:
                print("Error accepting connection:", e)
                

    except OSError as e:
        print("Error binding socket:", e)
        print("Trying with a different port...")
        addr = (ip_address, 8080)  # Try binding to port 8080 if port 80 is in use
        s.bind(addr)
        s.listen(1)
        print('Listening on', addr)
        while True:
            client, addr = s.accept()
            print('Client connected from', addr)
            handle_request(client)


# Main function to connect to WiFi and start the server
def runWebServer():
    connect_wifi()  # Connect to WiFi
    start_server()  # Start the server
# data={'project': 'Luminous+Play%3A+LED+light+magic', 'led_num': '5', 'strip_led_pin': '7'}
# update_project_config(data)
# runWebServer()
