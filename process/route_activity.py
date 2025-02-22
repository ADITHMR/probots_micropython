import json

def route_activity(activity_name):
    with open('project/project_routing.json', 'r') as f:
        data = json.load(f)
    return (data[activity_name])
                    
