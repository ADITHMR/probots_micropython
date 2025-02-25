import picoweb
import network
import time
import json
import urequests
import machine



from local_host.get_project_html import get_project_html

from utils import url_decode

from local_host.project_config_update import update_project_config

from local_host.web_page import web_page, successProjectPage,message_page,errorPage



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
        

        with open("local_host/index_page.html", 'r') as f:
            response= f.read()
        yield from picoweb.start_response(resp)
        yield from resp.awrite(response)
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
        

@app.route("/checkUpdate")
def check_update(req, resp):
    try:
        with open('version.dat', 'r') as f:
            html_content= json.load(f)
            
        version_now=(html_content["version"])
        html_path=html_content["version_path"]
        data=urequests.get(html_path).text
        data=json.loads(data)
        latest_version=data["version"]
        
        if latest_version==version_now:
            response=message_page("<h2> You are up to date!</h2>")
        else:
            response=message_page('''
            <h1>Update available.</h1>
            <h2> Do you want to update device?.</h2>
            <a href="/updatenow"  class="btn btn-warning" >Update Now </a>
            ''')
        yield from picoweb.start_response(resp)
        yield from resp.awrite(response)
    except Exception as e:
        print(f"Error at check_update() route : {e}")
        response=errorPage
    
    
    

@app.route("/updatenow")
def update_now(req, resp):
    with open('schema.dat', 'r') as f:
        schema= json.load(f)

    schema["update_flag"]="True"
    with open('schema.dat', 'w') as f:
            json.dump(schema, f)
    response=message_page('''
    <h2>Update Initiated...</h2>
    <h1 class="text-danger">Press the reset button to proceed with the update...</h1>
    
    <h2 class="text-danger">Do not interrupt the update process.</h2>''')
    yield from picoweb.start_response(resp)
    yield from resp.awrite(response)
    
    
@app.route("/restart")
def restart(req, resp):
    response=message_page(f'''
    <h2 class="text-danger">Device restarted successfully</h2>
    ''')
    
    yield from picoweb.start_response(resp)
    yield from resp.awrite(response)
    time.sleep(.1)
    machine.reset()
    

@app.route("/project", methods=["POST"])
def submit(req, resp):
    yield from req.read_form_data()
    data = req.form
    data_str=str(data).replace("'",'"')
    json_data=json.loads(data_str)
    update_project_config(json_data)
    response=message_page(f'''
    <h3>You have selected</h3>
    <h2 class="text-success">{data['project']}</h2>
    <a href="/restart">Click here to restart the system</a>
    ''')


    yield from picoweb.start_response(resp)
    yield from resp.awrite(response)

# Start web server


def runWebServer():
    try:
   
        app.run(debug=True, host="0.0.0.0", port=80)
    except Exception as e:
        print("Error runWebServer() :",e, e.args)



