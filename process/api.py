_F='password'
_E='username'
_D='Error:'
_C=False
_B='token'
_A='schema.dat'
import urequests,json
from local_host.connect_wifi import connect_wifi
from utils import get_jsonvalue_from_file,put_jsonvalue_to_file,write_file,read_file
class Api:
	user_login_url='http://roboninjaz.com:8010/api/user/login';get_projects_url='http://roboninjaz.com:8010/api/projects/getAllacquired-projects';get_projectfile_url='http://roboninjaz.com:8010/api/projects/download/';username=get_jsonvalue_from_file(_A,_E);password=get_jsonvalue_from_file(_A,_F);auth_header='0'
	def __init__(A):pass
	def user_login(B):
		H='user';G='application/json';F='Content-Type';I={'email':B.username,_F:B.password}
		try:
			A=urequests.post(B.user_login_url,data=json.dumps(I),headers={F:G})
			if A.status_code==200:print('Login successful');D=A.json();C=D[_B];E=D[H][_E];put_jsonvalue_to_file(_A,_B,C);put_jsonvalue_to_file(_A,H,E);B.auth_header={'Authorization':f"Bearer {C}",F:G};print('Token:',C);print('User :',E)
			else:print('Login failed with status code:',A.status_code);print('Response:',A.text);return _C
			A.close();return True
		except Exception as J:print(_D,J);return _C
	def get_projects(A):
		C=get_jsonvalue_from_file(_A,_B)
		if C!='0':
			try:
				B=urequests.get(A.get_projects_url,headers=A.auth_header)
				if B.status_code==200:D=B.json();E=D['projects'];A.save_projects(E)
			except Exception as F:print(_D,F);return _C
	def save_projects(P,projects):
		O='PROJECT';N='config.txt';M='project/projectList.py';E=[];F={};B=['activity1','activity2','activity3','activity4','activity5'];A=0
		for G in projects:
			Q=G['files'];R=G['description'];put_jsonvalue_to_file('project/project_description.dat',B[A],R)
			for H in Q:
				C=f"{B[A]}/{H['filename'].split('-')[1]}";I=H['id'];J=P.get_project_file(I)
				if J!='0':
					with open(C,'w')as D:D.write(J);print(f"{I} written to {C}")
			C=f"{B[A]}/config.txt";K=get_jsonvalue_from_file(C,'project_name');E.append(K);F[K]=B[A];A+=1
		write_file(M,f"project_topic_list ={E}")
		with open('project/project_routing.json','w')as D:json.dump(F,D)
		L=read_file(M);S=get_jsonvalue_from_file(N,O)
		if S in L:pass
		else:put_jsonvalue_to_file(N,O,L[1])
	def get_project_file(A,id):
		try:
			C=f"{A.get_projectfile_url}{id}";B=urequests.get(C,headers=A.auth_header)
			if B.status_code==200:return B.text
		except Exception as D:print(_D,D);return'0'