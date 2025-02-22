import urequests,json
from local_host.connect_wifi import connect_wifi
from utils import get_jsonvalue_from_file,put_jsonvalue_to_file,write_file
class Api:
	user_login_url='http://roboninjaz.com:8010/api/user/login';get_projects_url='http://roboninjaz.com:8010/api/projects/getAllacquired-projects';get_projectfile_url='http://roboninjaz.com:8010/api/projects/download/';username=get_jsonvalue_from_file('schema.dat','username');password=get_jsonvalue_from_file('schema.dat','password');auth_header='0'
	def __init__(A):0
	def user_login(B):
		F={'email':B.username,'password':B.password}
		try:
			A=urequests.post(B.user_login_url,data=json.dumps(F),headers={'Content-Type':'application/json'})
			if A.status_code==200:print('Login successful');D=A.json();C=D['token'];E=D['user']['username'];put_jsonvalue_to_file('schema.dat','token',C);put_jsonvalue_to_file('schema.dat','user',E);B.auth_header={'Authorization':f"Bearer {C}",'Content-Type':'application/json'};print('Token:',C);print('User :',E)
			else:print('Login failed with status code:',A.status_code);print('Response:',A.text);return False
			A.close();return True
		except Exception as G:print('Error:',G);return False
	def get_projects(A):
		C=get_jsonvalue_from_file('schema.dat','token')
		if C!='0':
			try:
				B=urequests.get(A.get_projects_url,headers=A.auth_header)
				if B.status_code==200:D=B.json();E=D['projects'];A.save_projects(E)
			except Exception as F:print('Error:',F);return False
	def save_projects(L,projects):
		E=[];F={};B=['activity1','activity2','activity3','activity4','activity5'];A=0
		for G in projects:
			M=G['files'];N=G['description'];put_jsonvalue_to_file('project/project_description.dat',B[A],N)
			for H in M:
				C=f"{B[A]}/{H['filename'].split('-')[1]}";I=H['id'];J=L.get_project_file(I)
				if J!='0':
					with open(C,'w')as D:D.write(J);print(f"{I} written to {C}")
			C=f"{B[A]}/config.txt";K=get_jsonvalue_from_file(C,'project_name');E.append(K);F[K]=B[A];A+=1
		write_file('project/projectList.py',f"project_topic_list ={E}")
		with open('project/project_routing.json','w')as D:json.dump(F,D)
	def get_project_file(A,id):
		try:
			C=f"{A.get_projectfile_url}{id}";B=urequests.get(C,headers=A.auth_header)
			if B.status_code==200:return B.text
		except Exception as D:print('Error:',D);return'0'
