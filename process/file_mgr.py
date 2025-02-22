import json
def set_parameter(parameter,value):
	D=value;A=parameter
	with open('config.txt','r')as B:
		C=json.load(B)
		if A in C:
			try:C[A]=str(D)
			except:return'Data format error'
			with open('config.txt','w')as B:json.dump(C,B);print('Data storedf in config.txt')
			E=get_parameter(A)
			if E==str(D):return'OK'
			else:return'Error Saving Data'
		else:return f"Error 404: No parameter named {A}"
def get_parameter(parameter):
	A=parameter
	with open('config.txt','r')as C:
		B=json.load(C)
		if A in B:D=B[A].replace("'",'');return D
		else:return'Error 404: No Such Parameter Found'
def get_project_config_data(project_name):
	A=project_name
	try:
		with open('projects/project_configurations.txt','r')as C:B=json.load(C)
	except FileNotFoundError:print('The configuration file does not exist.')
	except json.JSONDecodeError:print('Error decoding the JSON configuration file.')
	except Exception as D:print(f"An error occurred: {D}")
	if A in B:return B[A]
