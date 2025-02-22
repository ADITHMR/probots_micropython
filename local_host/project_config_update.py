import json,ujson
from process.route_activity import route_activity
from utils import url_decode
from process.file_mgr import set_parameter
def update_project_config(conf_list):
	D=conf_list
	try:
		E=url_decode(D['project']);F=route_activity(E);print(F);G=f"{F}/config.txt"
		with open(G,'r')as C:B=json.load(C)
		print(B)
		for(H,A)in D.items():
			if H=='project':A=url_decode(A);set_parameter('PROJECT',A)
			else:A=url_decode(A);B['params'][H]=A
		print(B)
		with open(G,'w')as C:json.dump(B,C)
		print(f"Configuration for project '{E}' has been updated successfully.")
	except Exception as I:print(f"An error occurred in 'update_project_config(conf_list)': {I}")
