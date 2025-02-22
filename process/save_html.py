import  json
from local_host.web_page import web_page
from machine_id import get_serial_no
from utils import get_jsonvalue_from_file,read_file,write_file
import gc
import traceback
from drivers.oled import oled_log 

def save_html():
    gc.collect()
    try:
       
        # -----------------------------------------------------------
        try:
#             with open('activity1/web_data.html', 'r') as f:
#                 data = json.load(f)
#             with open('activity1/config.txt', 'r') as f:
#                 project_name = json.load(f)
                
            description=get_jsonvalue_from_file('project/project_description.dat','activity1')
            project_name=get_jsonvalue_from_file('activity1/config.txt',"project_name")
            optons=get_jsonvalue_from_file('activity1/web_data.html',"data")
            optons=str(optons).replace("'",'"').replace("True",'true')
            
            response=read_file('local_host/project_page.html')
            response = response.replace('{*config_list*}',str(optons))
            response = response.replace('{*heading*}', project_name)
            response=response.replace('{Project_description}',description)

            write_file("html/activity1.html",response)
#             with open("html/activity1.html", "w") as f:
#                 f.write(response)
            del response
            print('Saved activity1.html')
            oled_log('Saved activity1.html')
            gc.collect()
        except Exception as e:
            print("Error on 'save_html() on activity1':", e)
            traceback.print_exc()
        # -----------------------------------------------------------
        try:
#             with open('activity2/web_data.html', 'r') as f:
#                 data = json.load(f)
#             
#             with open('activity2/config.txt', 'r') as f:
#                 project_name = json.load(f)
            description=get_jsonvalue_from_file('project/project_description.dat','activity2')                   
            project_name=get_jsonvalue_from_file('activity2/config.txt',"project_name")
            optons=get_jsonvalue_from_file('activity2/web_data.html',"data")
            optons=str(optons).replace("'",'"').replace("True",'true')
            
            response=read_file('local_host/project_page.html')
            response = response.replace('{*config_list*}',str(optons))
            response = response.replace('{*heading*}', project_name)
            response=response.replace('{Project_description}',description)
            
            write_file("html/activity2.html",response)
            del response
            print('Saved activity2.html')
            oled_log('Saved activity2.html')
            gc.collect()
#             with open("html/activity2.html", "w") as f:
#                 f.write(response)
#                 del response
        except Exception as e:
            print("Error on 'save_html() on activity2':", e)
            traceback.print_exc()
        # -----------------------------------------------------------
        try:
#             with open('activity3/web_data.html', 'r') as f:
#                 data = json.load(f)
#             with open('activity3/config.txt', 'r') as f:
#                 project_name = json.load(f)
            description=get_jsonvalue_from_file('project/project_description.dat','activity3')                    
            project_name=get_jsonvalue_from_file('activity3/config.txt',"project_name")
            optons=get_jsonvalue_from_file('activity3/web_data.html',"data")
            optons=str(optons).replace("'",'"').replace("True",'true')
            
            response=read_file('local_host/project_page.html')
            response = response.replace('{*config_list*}',str(optons))
            response = response.replace('{*heading*}', project_name)
            response=response.replace('{Project_description}',description)
            
            write_file("html/activity3.html",response)
            del response
            print('Saved activity3.html')
            oled_log('Saved activity3.html')
            gc.collect()

#             with open("html/activity3.html", "w") as f:
#                 f.write(response)
#                 del response
        except Exception as e:
            print("Error on 'save_html() on activity3':", e)
            traceback.print_exc()
        # -----------------------------------------------------------
        try:
#             with open('activity4/web_data.html', 'r') as f:
#                 data = json.load(f)
#             with open('activity4/config.txt', 'r') as f:
#                 project_name = json.load(f)
            description=get_jsonvalue_from_file('project/project_description.dat','activity4')                    
            project_name=get_jsonvalue_from_file('activity4/config.txt',"project_name")
            optons=get_jsonvalue_from_file('activity4/web_data.html',"data")
            optons=str(optons).replace("'",'"').replace("True",'true')
            
            response=read_file('local_host/project_page.html')
            response = response.replace('{*config_list*}',str(optons))
            response = response.replace('{*heading*}', project_name)
            response=response.replace('{Project_description}',description)
            
            write_file("html/activity4.html",response)
            del response
            print('Saved activity4.html')
            oled_log('Saved activity4.html')
            gc.collect()

#             with open("html/activity4.html", "w") as f:
#                 f.write(response)
#                 del response
        except Exception as e:
            print("Error on 'save_html() on activity4':", e)
            traceback.print_exc()
        # -----------------------------------------------------------
        try:
#             with open('activity5/web_data.html', 'r') as f:
#                 data = json.load(f)
#             with open('activity5/config.txt', 'r') as f:
#                 project_name = json.load(f)
            description=get_jsonvalue_from_file('project/project_description.dat','activity5')                    
            project_name=get_jsonvalue_from_file('activity5/config.txt',"project_name")
            optons=get_jsonvalue_from_file('activity5/web_data.html',"data")
            optons=str(optons).replace("'",'"').replace("True",'true')
            
            response=read_file('local_host/project_page.html')
            response = response.replace('{*config_list*}',str(optons))
            response = response.replace('{*heading*}', project_name)
            response=response.replace('{Project_description}',description)
            
            write_file("html/activity5.html",response)
            del response
            print('Saved activity5.html')
            oled_log('Saved activity5.html')
            gc.collect()


#             with open("html/activity5.html", "w") as f:
#                 f.write(response)
#                 del response
        except Exception as e:
            print("Error on 'save_html() on activity5':", e)
            traceback.print_exc()
        # -----------------------------------------------------------
        try:
            indexPage=str(web_page()).replace("{machine_id}",f"S/N: {get_serial_no()}")
            write_file("local_host/index_page.html",indexPage)
            del indexPage
            gc.collect()
#             with open("local_host/index_page.html", "w") as f:
#                 f.write(indexPage)
#                 del indexPage
            oled_log('Saved index.html')
            oled_log('Saved all html files')
            print("Successfully saved HTML files...")
        except Exception as e:
            print("Error on 'save_html() on indexpage':", e)
            traceback.print_exc()
    except Exception as e:
        print("Error on 'save_html()':", e)
        traceback.print_exc()
    
