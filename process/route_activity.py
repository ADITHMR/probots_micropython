import json
def route_activity(activity_name):
	with open('project/project_routing.json','r')as A:B=json.load(A)
	return B[activity_name]
