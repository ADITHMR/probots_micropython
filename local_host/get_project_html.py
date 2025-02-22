import json
def get_project_html(project_name):
	B=project_name
	with open('project/project_routing.json','r')as A:C=json.load(A)
	if B in C:
		D=f"html/{C[B]}.html"
		with open(D,'r')as A:E=A.read()
		return E
