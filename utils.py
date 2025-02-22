import json
def get_jsonvalue_from_file(file_path,key):
	try:
		with open(file_path,'r')as A:B=json.load(A);return B[key]
	except Exception as C:print("Error on 'get_jsonvalue_from_file()':",C)
def put_jsonvalue_to_file(file_path,key,value):
	B=file_path
	try:
		with open(B,'r')as A:C=json.load(A)
		C[key]=value
		with open(B,'w')as A:json.dump(C,A)
	except Exception as D:print("Error on 'put_jsonvalue_to_file()':",D)
def read_file(file_path):
	try:
		with open(file_path,'r')as A:B=A.read()
		return B
	except Exception as C:print("Error on 'getData_from_file()':",C);return False
def write_file(file_path,data):
	try:
		with open(file_path,'w')as A:A.write(data)
		return True
	except Exception as B:print("Error on 'getData_from_file()':",B);return False
def get_activity_params(activity):
	A=f"{activity}/config.txt"
	with open(A,'r')as B:C=json.load(B)
	D=C['params'];return D
def get_params(str_data):
	B={}
	try:
		A=str_data.split('GET /')[1].split(' HTTP')[0]
		if'?'in A:
			A=A.split('?')[1];C=A.split('&')
			for D in C:E,F=D.split('=');B[E]=F
			return B
	except Exception as G:print(f"An error occurred: {G}");return 0
def url_decode(encoded_str):A=encoded_str.replace('+',' ');A=A.replace('%20',' ').replace('%21','!').replace('%22','"').replace('%23','#').replace('%24','$').replace('%25','%').replace('%26','&').replace('%27',"'").replace('%28','(').replace('%29',')').replace('%2A','*').replace('%2B','+').replace('%2C',',').replace('%2D','-').replace('%2E','.').replace('%2F','/').replace('%3A',':').replace('%3B',';').replace('%3C','<').replace('%3D','=').replace('%3E','>').replace('%3F','?').replace('%40','@').replace('%5B','[').replace('%5C','\\').replace('%5D',']').replace('%5E','^').replace('%5F','_').replace('%60','`').replace('%7B','{').replace('%7C','|').replace('%7D','}').replace('%7E','~');return A
