import json
#        01 Fun with LED Lights
def get_project_html(project_name):
    
    with open('projects/project_routing.json', 'r') as f:
        activity = json.load(f)
    if project_name in activity:
        path=f"html/{activity[project_name]}.html"
        
        with open(path, 'r') as f:
            page = f.read()
    return page
       
           
        
