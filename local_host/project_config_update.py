import json
import ujson
# from imports import *
from  process.route_activity import route_activity
from utils import url_decode, put_jsonvalue_to_file
from process.file_mgr import set_parameter
def update_project_config(conf_list):
    try:
#         proj_name=url_decode(route_activity(conf_list["project"]))
        proj_name=url_decode(conf_list['project'])

        activity_name=route_activity(proj_name)
        print(activity_name)
        path=f"{activity_name}/config.txt"
        with open(path, 'r') as f:
            conf_data = json.load(f)
            
        print(conf_data)
        
        
    
        # Update project configuration with new values
        for conf, value in conf_list.items():
           
            if conf == 'project':
                value = url_decode(value)  # Ensure project name is correctly formatted
                set_parameter("PROJECT",value)
                put_jsonvalue_to_file("schema.dat","PROJECT",value)
                print("xxxxxxxxxxxxxxxxxxxx")
            else:
                value = url_decode(value)
                conf_data["params"][conf] = value
        print(conf_data)

        
        # Write the updated data back to the file
        with open(path, 'w') as f:
            json.dump(conf_data, f)
        
        print(f"Configuration for project '{proj_name}' has been updated successfully.")
    
    
    
    except Exception as e:
        print(f"An error occurred in 'update_project_config(conf_list)': {e}")

