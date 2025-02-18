import urequests
import json
from local_host.connect_wifi import  connect_wifi
from utils import get_jsonvalue_from_file,put_jsonvalue_to_file

class Api:
    user_login_url="http://roboninjaz.com:8010/api/user/login"
    get_projects_url="http://roboninjaz.com:8010/api/projects/getAllacquired-projects"
    get_projectfile_url="http://roboninjaz.com:8010/api/projects/download/"
    
    username=get_jsonvalue_from_file("schema.dat","username")
    password=get_jsonvalue_from_file("schema.dat","password")
    
    auth_header="0"
    
    def __init__(self):
        pass
#         put_jsonvalue_to_file("schema.dat","token","0")
  

    def user_login(self):
        data = {"email": self.username,"password": self.password}
        try:
            # Sending POST request
            response = urequests.post(self.user_login_url, data=json.dumps(data), headers={"Content-Type": "application/json"})
            
            # Checking if the request was successful
            if response.status_code == 200:
                print("Login successful")
                response_data = response.json()
#                 print("Response:", response.text)
                # Extract token
                token = response_data["token"]
                user = response_data["user"]["username"]
                
                put_jsonvalue_to_file("schema.dat","token",token)
                put_jsonvalue_to_file("schema.dat","user",user)
                
                self.auth_header={"Authorization": f"Bearer {token}","Content-Type": "application/json"}
                
                print("Token:", token)
                print("User :", user)
            else:
                print("Login failed with status code:", response.status_code)
                print("Response:", response.text)
                return False

            # Always close the response
            response.close()
            return True

        except Exception as e:
            print("Error:", e)
            return False
    def get_projects(self):
        token=get_jsonvalue_from_file("schema.dat","token")
        if token!="0":
            
            try:
            # Sending POST request
                response = urequests.get(self.get_projects_url, headers=self.auth_header)
#                 print(response.text)
                
                if response.status_code == 200:
       
                    response_data = response.json()
#                     print(len(response_data["projects"]))
                    projects=response_data["projects"]
#                     print(projects)
                    self.save_projects(projects)
            except Exception as e:
                print("Error:", e)
                return False
    def save_projects(self,projects):
        folders=["activity1","activity2","activity3","activity4","activity5"]
        i=0
        for project in projects:
            files=project["files"]
#             print(files)
            for file in files:
                file_path=f"{folders[i]}/{file['filename'].split("-")[1]}"
                fileid=file['id']
                file_content=self.get_project_file(fileid)
                if file_content!="0":
                    with open(file_path, 'w') as f:
                        f.write(file_content)
                        print(f"{fileid} written to {file_path}")
                print(fileid)
            i+=1
    def get_project_file(self,id):
        try:
            # Sending POST request
            url=f"{self.get_projectfile_url}{id}"
            response = urequests.get(url, headers=self.auth_header)
#                 print(response.text)
#             print(response.text)
            if response.status_code == 200:
                return(response.text)

        except Exception as e:
            print("Error:", e)
            return "0"
        
            
            

# api=Api()
# api.user_login()
# api.get_projects()