import  json
from local_host.web_page import web_page
from machine_id import get_serial_no
from utils import get_jsonvalue_from_file,read_file,write_file,file_exists,put_jsonvalue_to_file
import gc
import re
from drivers.oled import oled_log,oled_two_data,oled_three_data




    
    
def save_html():
    
    try:
        print(0)
        gc.collect()
        folders=["activity1","activity2","activity3","activity4","activity5"]
        
#         project_list=[]
        progress=0
        for folder in folders:
            web_items_path=f"{folder}/web_data.html"
            config_items_path=f"{folder}/config.txt"
           
            if file_exists(web_items_path) and file_exists(config_items_path):
                web_items_list=get_jsonvalue_from_file(web_items_path,"data")
                project_name=get_jsonvalue_from_file(config_items_path,"project_name")
                output_path=f"html/{folder}.html"
                project_page=read_file('local_host/project_page.html')
                if web_items_list != "error" and project_name!= "error" and project_page!="error":
                    web_items_list_modified=str(web_items_list).replace("'",'"').replace("True",'true')
                    del web_items_list
                    gc.collect()
                    description=get_jsonvalue_from_file('project/project_description.dat',folder)
                    response=project_page
                    del project_page
                    gc.collect()
                    write_file(output_path,response)
                    del response
                    gc.collect()
                    progress+=5
                    print(progress)
                    oled_three_data(1,1,2,"Saving","Pages",f"{progress}%")
                    replace_item(output_path,'{*config_list*}',str(web_items_list_modified))
                    progress+=5
                    print(progress)
                    oled_three_data(1,1,2,"Saving","Pages",f"{progress}%")
                    replace_item(output_path,"{*heading*}",str(project_name))
                    progress+=5
                    print(progress)
                    oled_three_data(1,1,2,"Saving","Pages",f"{progress}%")
                    replace_item(output_path,"{description}",str(description))
                    progress+=5
                    print(progress)
                    oled_three_data(1,1,2,"Saving","Pages",f"{progress}%")
                    
    except Exception as e:
        print("Error in save_html():", e)
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
#         traceback.print_exc()
        
               
def replace_item(path,ref,text):
    data=read_file(path)
    write_file(path,data.replace(ref,text))
    
# save_html()            
                