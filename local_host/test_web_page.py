import time
import machine
import json
import socket
import network
from oled import *
from local_host.project_config_update import *
import ure
import traceback
from imports import *
import sys

# Global variable for WiFi connection status
wifi_connected = False
wifi_connection_timeout = 10  # Timeout after 10 seconds
wifi_conn_start_time = time.time()

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
    try:
        client.settimeout(3)  # Timeout in seconds
        data = client.recv(1024)  # Blocking call here but done synchronously
        
        if not data:
            print("Client closed the connection")
            return
        
        request_str = str(data)
        
        # Handle different routes
        response = handle_route(request_str)
        
        if response:
            client.send(response)
    
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
            if restart:
                time.sleep(1)
                machine.reset()
        except Exception as e:
            print("Error closing client connection:", e)
            traceback.print_exc()

def handle_route(request_str):
    if '/hello' in request_str:
        return "HTTP/1.1 200 OK\n\nStatus: Hello There!"
    elif '/reset' in request_str:
        return restartSuccessPage()
    elif 'GET /?project' in request_str:
        datas = get_params(request_str)
        print(datas)
        update_project_config(datas)
        return "HTTP/1.1 200 OK\n\nProject updated."
    elif 'selectedItem=' in request_str and 'POST' in request_str:
        return handle_post_selected_item(request_str)
    elif 'GET / HTTP' in request_str:
        return handle_homepage_request()
    else:
        return errorPage()

def handle_post_selected_item(request_str):
    match = ure.search(r'selectedItem=([^&]+)', request_str)
    if match:
        selected_option = match.group(1).replace("'", "").replace("+", " ")
        with open('local_host/project_options_JSON.txt', 'r') as f:
            data = json.load(f)
        
        if selected_option in data:
            with open('local_host/project_page.html', 'r') as f:
                html_content = f.read()
            html_content = html_content.replace('{*config_list*}', json.dumps(data[selected_option]))
            html_content = html_content.replace('{*heading*}', selected_option)
            return html_content
        else:
            return errorPage()
    return None

def handle_homepage_request():
    response = web_page()
    try:
        with open("project.html", 'w') as f:
            f.write(response)
        print(f"Content successfully written to file")
    except Exception as e:
        print(f"Error writing to file: {e}")
    return response

# Start the web server
def start_server():
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(1)
    print('Listening on', addr)

    while True:
        try:
            client, addr = s.accept()
            print('Client connected from', addr)
            handle_request(client)
        except Exception as e:
            print("Error accepting connection:", e)

# Main function to connect to WiFi and start the server
def runWebServer():
    connect_wifi()  # Connect to WiFi
    start_server()  # Start the server

runWebServer()

