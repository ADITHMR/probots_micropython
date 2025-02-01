import picoweb
import network
import time
import json

from local_host.connect_wifi import  connect_wifi
from local_host.web_page import web_page, successProjectPage
from local_host.get_project_html import get_project_html

from utils import url_decode

from local_host.project_config_update import update_project_config


connect_wifi()

# Create Picoweb app
app = picoweb.WebApp(__name__)

# # HTML template
# def web_page():
#     return """<!DOCTYPE html>
# <html>
# <head><title>ESP32 Web Server</title></head>
# <body>
#     <h1>ESP32 Picoweb Server</h1>
#     <p>Welcome to the microcontroller web server!</p>
#     <form action="/submit" method="POST">
#         <input type="text" name="message" placeholder="Enter message">
#         <button type="submit">Send</button>
#     </form>
#     <p>Try these links:</p>
#     <ul>
#         <li><a href="/hello">Hello Page</a></li>
#         <li><a href="/greet/John">Greet John</a></li>
#     </ul>
# </body>
# </html>
# """

# Route handlers
@app.route("/")
def index(req, resp):
    if req.method=="GET":
        yield from picoweb.start_response(resp)
        yield from resp.awrite(web_page())
    else:
        yield from req.read_form_data()
        data = req.form
        print(data)
        if "selectedItem" in data:
            project=data["selectedItem"]
        else:
            project="no data"
        response=get_project_html(project)

        yield from picoweb.start_response(resp)
        yield from resp.awrite(response)
        

@app.route("/hello")
def hello(req, resp):
    yield from picoweb.start_response(resp)
    yield from resp.awrite("Hello from ESP32!")

@app.route("/greet/<name>")
def greet(req, resp, name):
    yield from picoweb.start_response(resp)
    yield from resp.awrite(f"Hello, {name}!")

@app.route("/project", methods=["POST"])
def submit(req, resp):
    yield from req.read_form_data()
    data = req.form
    data_str=str(data).replace("'",'"')
    json_data=json.loads(data_str)
    update_project_config(json_data)


    yield from picoweb.start_response(resp)
    yield from resp.awrite(successProjectPage(url_decode(data['project'])))

# Start web server
app.run(debug=True, host="0.0.0.0", port=80)
