import json
import ujson
from imports import *
def update_project_config(conf_list):
    try:
        # Read the current configurations from the file
        with open('projects/project_configurations.txt', 'r') as f:
            data = json.load(f)
        
        # Ensure the project exists in the data
        project_name = conf_list['project'].replace("+", " ")
        if project_name not in data:
            print(f"Project '{project_name}' not found in the configuration file.")
            return
        
        # Get the project configuration
        project_data = data[project_name]
        
        # Update project configuration with new values
        for conf, value in conf_list.items():
            value = value.replace("+", " ")
            if conf == 'project':
                value = value.replace("+", " ")  # Ensure project name is correctly formatted
                set_parameter("PROJECT",value)
            value = value.replace("+", " ")
            project_data[conf] = value
            
        
        # Update the main data dictionary with the updated project data
        data[project_name] = project_data
        
        # Write the updated data back to the file
        with open('projects/project_configurations.txt', 'w') as f:
#             formatted_json =ujson.dumps(data, indent=4)
            json.dump(data, f)
        
        print(f"Configuration for project '{project_name}' has been updated successfully.")
    
    except FileNotFoundError:
        print("The configuration file does not exist.")
    except json.JSONDecodeError:
        print("Error decoding the JSON configuration file.")
    except Exception as e:
        print(f"An error occurred: {e}")

