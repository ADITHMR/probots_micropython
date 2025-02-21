import  json
from local_host.web_page import web_page
from machine_id import get_serial_no
from utils import get_jsonvalue_from_file
def save_html():
    try:
        with open('local_host/project_page.html', 'r') as f:
                project_page = f.read()
        # -----------------------------------------------------------       
        with open('activity1/web_data.html', 'r') as f:
            data = json.load(f)
        with open('activity1/config.txt', 'r') as f:
            project_name = json.load(f)
        description=get_jsonvalue_from_file('project/project_description.dat','activity1')
        project_name=project_name["project_name"]
        optons=str(data["data"]).replace("'",'"').replace("True",'true')
        response = project_page.replace('{*config_list*}',str(optons))
        response = response.replace('{*heading*}', project_name)
        response=response.replace('{Project_description}',description)


        with open("html/activity1.html", "w") as f:
            f.write(response)
        # -----------------------------------------------------------
        with open('activity2/web_data.html', 'r') as f:
            data = json.load(f)
        
        with open('activity2/config.txt', 'r') as f:
            project_name = json.load(f)
        description=get_jsonvalue_from_file('project/project_description.dat','activity2')                   
        project_name=project_name["project_name"]
        optons=str(data["data"]).replace("'",'"').replace("True",'true')
        
        response = project_page.replace('{*config_list*}',str(optons))
        response = response.replace('{*heading*}', project_name)
        response=response.replace('{Project_description}',description)

        with open("html/activity2.html", "w") as f:
            f.write(response)
        # -----------------------------------------------------------
        with open('activity3/web_data.html', 'r') as f:
            data = json.load(f)
        with open('activity3/config.txt', 'r') as f:
            project_name = json.load(f)
        description=get_jsonvalue_from_file('project/project_description.dat','activity3')                    
        project_name=project_name["project_name"]
        optons=str(data["data"]).replace("'",'"').replace("True",'true')
        response = project_page.replace('{*config_list*}',str(optons))
        response = response.replace('{*heading*}', project_name)
        response=response.replace('{Project_description}',description)

        with open("html/activity3.html", "w") as f:
            f.write(response)
        # -----------------------------------------------------------
        with open('activity4/web_data.html', 'r') as f:
            data = json.load(f)
        with open('activity4/config.txt', 'r') as f:
            project_name = json.load(f)
        description=get_jsonvalue_from_file('project/project_description.dat','activity4')                    
        project_name=project_name["project_name"]
        optons=str(data["data"]).replace("'",'"').replace("True",'true')
        response = project_page.replace('{*config_list*}',str(optons))
        response = response.replace('{*heading*}', project_name)
        response=response.replace('{Project_description}',description)

        with open("html/activity4.html", "w") as f:
            f.write(response)
        # -----------------------------------------------------------
        with open('activity5/web_data.html', 'r') as f:
            data = json.load(f)
        with open('activity5/config.txt', 'r') as f:
            project_name = json.load(f)
        description=get_jsonvalue_from_file('project/project_description.dat','activity5')                    
        project_name=project_name["project_name"]
        optons=str(data["data"]).replace("'",'"').replace("True",'true')
        response = project_page.replace('{*config_list*}',str(optons))
        response = response.replace('{*heading*}', project_name)
        response=response.replace('{Project_description}',description)


        with open("html/activity5.html", "w") as f:
            f.write(response)
        # -----------------------------------------------------------
        indexPage=str(web_page()).replace("{machine_id}",f"S/N: {get_serial_no()}")
        with open("local_host/index_page.html", "w") as f:
            f.write(indexPage)
        print("Successfully saved HTML files...")
    except Exception as e:
        print("Error on 'save_html()':", e)
    
