import  json

def fetch_projects():
    try:
        projectlist=[]
        project_routing_json={}

        with open('activity1/config.txt', 'r') as f:
                    data = json.load(f)
                    
        project_name=data["project_name"]
        if project_name in projectlist:
            pass
        else:
            projectlist.append(project_name)

        project_routing_json[project_name]="activity1"

        # ------------------------------------------------------------

        with open('activity2/config.txt', 'r') as f:
                    data = json.load(f)
                    
        project_name=data["project_name"]
        if project_name in projectlist:
            pass
        else:
            projectlist.append(project_name)

        project_routing_json[project_name]="activity2"
        # ------------------------------------------------------------

        with open('activity3/config.txt', 'r') as f:
                    data = json.load(f)
                    
        project_name=data["project_name"]
        if project_name in projectlist:
            pass
        else:
            projectlist.append(project_name)

        project_routing_json[project_name]="activity3"
        # ------------------------------------------------------------
        with open('activity4/config.txt', 'r') as f:
                    data = json.load(f)
                    
        project_name=data["project_name"]
        if project_name in projectlist:
            pass
        else:
            projectlist.append(project_name)

        project_routing_json[project_name]="activity4"
        # ------------------------------------------------------------
        with open('activity5/config.txt', 'r') as f:
                    data = json.load(f)
                    
        project_name=data["project_name"]
        if project_name in projectlist:
            pass
        else:
            projectlist.append(project_name)

        project_routing_json[project_name]="activity5"
        # ------------------------------------------------------------
        with open("projects/projectList.py", "w") as f:
            f.write(f"project_topic_list ={projectlist}")
        with open("projects/project_routing.json", "w") as f:
            json.dump(project_routing_json, f)
            
        print( f"project_topic_list ={projectlist}")
        print("Project fetching completed..")
    except Exception as e:
        # Code to handle the exception
        print(f"Error in 'fetch_projects()' : {e}")

