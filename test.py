from file_mgr import *
from local_host.web_page import *
from display import *
import ure  # MicroPython version of regular expressions
import socket
import network
import time
import machine
from oled import *

wifi_connection_timeout = 10  # Timeout after 10 seconds
wifi_conn_start_time = time.time()
wifi_connected=0
# Connect to WiFi
def connect_wifi():
    ##################################################
    ### OPEN FILE AND GET SSID AND PASSWORD
    WIFI_SSID=str(get_parameter("SSID"))
    WIFI_PASSWORD=str(get_parameter("PASSWORD"))
    
    ############################################
    
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASSWORD)
    print('Connecting to WiFi...')
    oled_log("Conn to WiFi...")
    disp_scroll_str("CONNecting")
    
    while not wlan.isconnected():
        oled_two_data(1,2,"Conn to WiFi",str(wifi_connection_timeout-(time.time() - wifi_conn_start_time)))
        # Check if the connection is taking too long
        if (time.time() - wifi_conn_start_time) > wifi_connection_timeout:
            print("Connection timed out")
            
            wifi_connected=0
            return
            break
        time.sleep(1)
    wifi_connected=1
    print('WiFi connected')
    oled_log("WiFi connected")
    disp_seq_str(["DONE"],1)
    print('IP Address:', wlan.ifconfig()[0])
    oled_log("IP->")
    oled_log(wlan.ifconfig()[0])
    
    
    disp_scroll_str('IP Address '+wlan.ifconfig()[0].replace('.','-'))
    
    ip_last_byte=wlan.ifconfig()[0].split('.')[3]
    disp_seq_str([str(ip_last_byte)],1)

# Handle HTTP requests
def handle_request(client):
    restart=0
    try:

        # Set the socket timeout
        client.settimeout(3)  # Timeout in seconds

        # Receive the request (non-blocking)
#         request = await asyncio.sleep(0)  # Mimic a non-blocking call
        data = client.recv(1024)  # Blocking call here but done synchronously
        
        request_str = str(data)

        if not data:
            print("Client closed the connection")
            return

#         print('Request:', request_str)

        # Handle different routes
        if '/hello' in request_str:
            response = "HTTP/1.1 200 OK\n\nStatus: Hello There!"
#             client.send(response)
        elif '/reset' in request_str:
            # Redirect to /newpage
            response = restartSuccessPage()
            restart=1
        elif 'GET /?project_name' in request_str:
            datas=get_params(request_str)
            print(datas)
            
        elif 'selectedItem=' and 'POST' in request_str:
            # Simple regex to find the selectedOption value
            match=0
            selected_option=0
            print("level-1")
            match = ure.search(r'selectedItem=([^&]+)', request_str)
            
            print(f"match={match.group(1)}")
            if match!=None:
                selected_option = match.group(1).replace("'","")
                selected_option = selected_option.replace("+"," ")
#                 
                with open('projects/project_configurations.txt', 'r') as f:
                    data= json.load(f)
                    print(data)
                    if selected_option in data:
                        print("**************got data*****************")
                        with open('local_host/project_page.html', 'r') as f:
                            html_content = f.read()
                        html_content = html_content.replace('{*config_list*}', json.dumps(data[selected_option]))
                        html_content=html_content.replace('{*heading*}',selected_option)
                        response=html_content
#                         print(response)
                    else:
                        response=errorPage()
                
                
#             result=save_data(selected_option,"POST")
#             if result!= 0:
#                 response = successProjectPage(result)
#             else:
#                 response=errorPage()

                
            
#     // FOR GET REQUEST        
#         elif 'selectedItem=' in request_str:
#             result=save_data(request_str,"GET")
#             if result!= 0:
#                 response = successProjectPage(result)
#             else:
#                 response=errorPage()
# #             client.send(response)
        elif'GET / HTTP' in request_str:
            response = web_page()
            try:
                with open("project.html", 'w') as f:  # Open the file in write mode ('w')
                    f.write(response)  # Write content to the file
                    print(f"Content successfully written to file")
            except Exception as e:
                print(f"Error writing to file: {e}")
#             client.send(response)
     
        # Send the response (non-blocking)
        client.send(response)
       
        

    except OSError as e:
        if e.errno == 113:  # ECONNABORTED
            print("Error: Connection aborted by client (ECONNABORTED)")
        else:
            print("OSError:", e)
    except Exception as e:
        print("General Error:", e)
    finally:
        try:
            # Ensure that the client connection is closed
            print("Closing client connection")
            client.close()
            if  restart == 1:
                time.sleep(1)
                machine.reset()
            
                
        except Exception as e:
            print("Error closing client connection:", e)
    

# Start the web server
def start_server():
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(1)
    print('Listening on', addr)

    while True:
        try:
            # Accept client connections synchronously (without asyncio.to_thread)
            client, addr = s.accept()
            print('Client connected from', addr)

            # Handle the request asynchronously
            handle_request(client)

        except Exception as e:
            print("Error accepting connection:", e)

# Main function to connect to WiFi and start the server
def runWebServer():
    
    start_server()  # Start the server

def save_data(str_data,req_type):
    params={}
    if req_type=="GET":
        try:
            query_string = str_data.split("GET /")[1].split(" HTTP")[0]
            if "?" in query_string:
                query_string = query_string.split("?")[1]
                pairs = query_string.split("&")
                for pair in pairs:
                    key, value = pair.split("=")
                    params[key] = value
            if "selectedItem" in params:
                data=params["selectedItem"]
                data=data.replace("+", " ")
                print('Content- '+ data )
                set_parameter("PROJECT",data)
                print("Success")
                return data
        except Exception as e:
            print(f"An error occurred: {e}")
            return 0
    elif req_type=="POST":
        try:
            data=str_data
            data=data.replace("+", " ")
            
            print('Content- '+ data )
            set_parameter("PROJECT",data)
            print("Success")
            return data
        except Exception as e:
            print(f"An error occurred: {e}")
            return 0
                            

def get_params(str_data):
    params={}
    try:
        query_string = str_data.split("GET /")[1].split(" HTTP")[0]
        if "?" in query_string:
            query_string = query_string.split("?")[1]
            pairs = query_string.split("&")
            for pair in pairs:
                key, value = pair.split("=")
                params[key] = value
            return params
    except Exception as e:
            print(f"An error occurred: {e}")
            return 0


connect_wifi()
runWebServer()