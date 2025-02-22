import picoweb,network,time,json,urequests,machine
from local_host.connect_wifi import connect_wifi
from local_host.web_page import web_page,successProjectPage,message_page,errorPage
from local_host.get_project_html import get_project_html
from utils import url_decode
from local_host.project_config_update import update_project_config
app=picoweb.WebApp(__name__)
@app.route('/')
def index(req,resp):
	B=req;A=resp
	if B.method=='GET':
		with open('local_host/index_page.html','r')as F:C=F.read()
		yield from picoweb.start_response(A);yield from A.awrite(C)
	else:
		yield from B.read_form_data();D=B.form;print(D)
		if'selectedItem'in D:E=D['selectedItem']
		else:E='no data'
		C=get_project_html(E);yield from picoweb.start_response(A);yield from A.awrite(C)
@app.route('/checkUpdate')
def check_update(req,resp):
	try:
		with open('version.dat','r')as D:C=json.load(D)
		E=C['version'];F=C['version_path'];A=urequests.get(F).text;A=json.loads(A);G=A['version']
		if G==E:B=message_page('<h2> You are up to date!</h2>')
		else:B=message_page('\n            <h1>Update available.</h1>\n            <h2> Do you want to update device?.</h2>\n            <a href="/updatenow"  class="btn btn-warning" >Update Now </a>\n            ')
		yield from picoweb.start_response(resp);yield from resp.awrite(B)
	except Exception as H:print(f"Error at check_update() route : {H}");B=errorPage
@app.route('/updatenow')
def update_now(req,resp):
	with open('schema.dat','r')as A:B=json.load(A)
	B['update_flag']='True'
	with open('schema.dat','w')as A:json.dump(B,A)
	C=message_page('\n    <h2>Update Initiated...</h2>\n    <h1 class="text-danger">Press the reset button to proceed with the update...</h1>\n    \n    <h2 class="text-danger">Do not interrupt the update process.</h2>');yield from picoweb.start_response(resp);yield from resp.awrite(C)
@app.route('/restart')
def restart(req,resp):A=message_page(f'\n    <h2 class="text-danger">Device restarted successfully</h2>\n    ');yield from picoweb.start_response(resp);yield from resp.awrite(A);time.sleep(.1);machine.reset()
@app.route('/project',methods=['POST'])
def submit(req,resp):yield from req.read_form_data();A=req.form;B=str(A).replace("'",'"');C=json.loads(B);update_project_config(C);D=message_page(f'\n    <h3>You have selected</h3>\n    <h2 class="text-success">{A["project"]}</h2>\n    <a href="/restart">Click here to restart the system</a>\n    ');yield from picoweb.start_response(resp);yield from resp.awrite(D)
def runWebServer():app.run(debug=True,host='0.0.0.0',port=80)
