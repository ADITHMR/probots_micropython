

from utils import url_decode
from time import sleep
# from drivers.display import disp_scroll_str
from machine_id import get_serial_no
from drivers.oled import *
from utils import put_jsonvalue_to_file,set_wifi_credentials

import json
try:
  import usocket as socket
except:
  import socket

import picoweb
import network
import time
import json
import urequests
import machine

from local_host.connect_wifi import  connect_wifi
app = picoweb.WebApp(__name__)
REPLACE_FOR_SPACE="@@!##"
def enable_AP():
    oled_log('Access point')
    oled_log('Please wait...')
#     disp_scroll_str('Access point')
    print('Access point')

    sleep(1)

    ssid = get_serial_no()
    password = '123456789'

    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid=ssid, password=password)
    ap.ifconfig(('192.168.10.1', '255.255.255.0', '192.168.1.1', '192.168.1.1'))
    
#     disp_scroll_str('IP Address -192-168-10-1')
    
    sleep(1)
    while ap.active() == False:
      pass
#     disp_scroll_str('Conn Success')
#     oled_log('Connect to "Prosol AP"')
    
    oled_log('IP->192.168.10.1')
    oled_log(f"SSID- '{ssid}'")
    print('Connection successful')
    print(ap.ifconfig())

@app.route("/")
def index(req, resp):
    if req.method=="GET":
        with open("local_host/credentials.html", 'r') as f:
            response= f.read()
        yield from picoweb.start_response(resp)
        yield from resp.awrite(response)
    
@app.route("/submit")
def submit(req, resp):
    if req.method == "POST":
        # Parse the form data from the POST request
        yield from req.read_form_data()
        data = req.form
        data_str=str(data).replace("'",'"')
        json_data=json.loads(data_str)
        print(json_data["ssid"])
        wifi_ssid=json_data["ssid"]
        wifi_password=json_data["wifi-password"]
        username=json_data["email"]
        userpassword=json_data["password"]
        
        set_wifi_credentials(wifi_ssid,wifi_password)
#         put_jsonvalue_to_file("config.txt","SSID",wifi_ssid)
#         put_jsonvalue_to_file("config.txt","PASSWORD",wifi_password)
        
        put_jsonvalue_to_file("schema.dat","username",username)
        put_jsonvalue_to_file("schema.dat","password",userpassword)
        
        
        success_response = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Submission Successful</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #121212;
                color: #ffffff;
                display: flex;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
            }}

            .form-container {{
                background-color: #1e1e1e;
                padding: 2rem;
                border-radius: 16px;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5);
                width: 100%;
                max-width: 400px;
                text-align: center;
            }}

            .main-heading {{
                font-size: 2.5rem;
                font-weight: bold;
                color: #00bcd4;
                margin-bottom: 1.5rem;
            }}

            h2 {{
                color: #ffffff;
                margin-bottom: 1.5rem;
            }}

            .section {{
                margin-bottom: 1.5rem;
            }}

            p {{
                font-size: 1.1rem;
                color: #bbbbbb;
            }}

            .back-button {{
                margin-top: 1rem;
                padding: 0.75rem;
                background-color: #00bcd4;
                color: white;
                border: none;
                border-radius: 8px;
                font-size: 1rem;
                cursor: pointer;
                transition: background-color 0.3s;
            }}

            .back-button:hover {{
                background-color: #008ba3;
            }}
        </style>
    </head>
    <body>
        <div class="form-container">
            <div class="main-heading">roboNinjaz</div>
            <h2>Form Submitted Successfully!</h2>
            <div class="section">
                <h3>WiFi Credentials</h3>
                <p><strong>WiFi SSID:</strong> {wifi_ssid}</p>
                <p><strong>WiFi Password:</strong> {wifi_password}</p>
            </div>

            <div class="section">
                <h3>User Login Credentials</h3>
                <p><strong>Email ID:</strong> {username}</p>
                <p><strong>Password:</strong> {userpassword}</p>
            </div>

            <h1>Restart the device!<h1>
        </div>
    </body>
    </html>
    """

        yield from picoweb.start_response(resp, content_type="text/html")
        yield from resp.awrite(success_response)
            
#         # Extract the username and password from the form data
#         ssid = form['ssid']
#         wifi_password = form['wifi-password']
#         print(ssid,wifi_password)
def runAP():
    enable_AP()   
    app.run(debug=True, host="0.0.0.0", port=80)    
