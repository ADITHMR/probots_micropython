import machine
from  project.projectList import  *
from machine_id import get_serial_no



# <option value=" ">--Select Project--</option>

# Generate HTML for the dropdown
html_dropdown =  """
<select id="mydropdown" name="selectedItem" class="form-select" required>
<option value="">--Select Project--</option>

"""
for proj in project_topic_list:
    html_dropdown += f"<option value=\"{proj}\">{proj}</option>\n"
html_dropdown+="</select>"    
            




# print(html_dropdown)
def web_page():
    with open('local_host/index.html', 'r') as f:
                html_content = f.read()
                html_content=html_content.replace("{html_dropdown}",html_dropdown)
                html_content=html_content.replace("{*Serial No*}",get_serial_no())
    return html_content
def successProjectPage(data):
    with open('local_host/project_sel_success.html', 'r') as f:
                html_content = f.read()
                html_content=html_content.replace("{data}",data)
                
                
    return html_content

def errorPage():
    with open('local_host/error404.html', 'r') as f:
                html_content = f.read()
               
    return html_content
def restartSuccessPage():
    
    with open('local_host/restart_success_page.html', 'r') as f:
                html_content = f.read()
               
    return html_content
def message_page(message):
    
    with open('local_host/message.html', 'r') as f:
                html_content = f.read()
    html_content=html_content.replace("{machine_id}",f"S/N: {get_serial_no()}")
    html_content=html_content.replace("{message}",message)

    return html_content    
 