import time
import json
import os

from pin_mapping import TOUCH1,TOUCH2
from local_host.connect_wifi import  connect_wifi
from drivers.oled import *
oled_two_data(1,1,"System","Booting")
# from machine_id import get_update_flag
time.sleep(.5)

if TOUCH1.value()==True and TOUCH2.value()==True:
    from local_host.esp_as_AP import enable_AP
    enable_AP()
elif  TOUCH1.value()==True and TOUCH2.value()==False:
    from local_host.webServer import runWebServer
    oled_two_data(1,1,"Web server","Mode")
    time.sleep(1)
    runWebServer()

connect_wifi()

# -----------------------------------------
def copy_all_content(src, dest):
    # List all items (files and subdirectories) in the source directory
    for item in os.listdir(src):
        src_item = src + '/' + item  # Manually join the source directory path
        dest_item = dest + '/' + item  # Manually join the destination directory path
        if dest_item !=src_item:
            # Check if it's a file
            if os.stat(src_item)[0] == 32768:  # 32768 indicates a regular file
                with open(src_item, 'rb') as fsrc:  # Open the source file in binary mode
                    with open(dest_item, 'wb') as fdest:  # Open the destination file in binary mode
                        fdest.write(fsrc.read())  # Copy file content
            # Check if it's a directory
            elif os.stat(src_item)[0] == 16384:  # 16384 indicates a directory
                try:
                    os.mkdir(dest_item)  # Try to create the directory in the destination
                except OSError:
                    pass  # If the directory already exists, we catch the OSError and continue
                # Recursively copy the contents of the subdirectory
                copy_all_content(src_item, dest_item)

    print(f"Successfully copied all content from {src} to {dest}.")
# ------------------------------------------
def delete_all_content(directory):
    # List all items in the directory
    for item in os.listdir(directory):
        item_path = directory + '/' + item  # Manually join the directory path
        
        if os.stat(item_path)[0] == 32768:  # Check if it's a file (type 32768 means regular file)
            os.remove(item_path)  # Remove the file
        elif os.stat(item_path)[0] == 16384:  # Check if it's a directory (type 16384 means directory)
            # If it's a directory, remove its content recursively
            delete_all_content(item_path)
            os.rmdir(item_path)  # Remove the empty directory

    print(f"All content in '{directory}' has been deleted.")
# -------------------------------------------------------


with open('schema.dat', 'r') as f:
    data = json.load(f)
update_flag=str(data["update_flag"])
download_flag=str(data["download_flag"])
print(f"update_status={update_flag}")
print(f"download_status={download_flag}")


if update_flag=="True":
    print("Starting Update")
    oled_two_data(1,1,"Starting","Update")
    time.sleep(1)
    oled_two_data(1,1,"Clearing","Files")
    try:
        os.listdir("/backup")
        delete_all_content("/backup")
    except OSError:
        os.mkdir(folder)
        print(f"Created folder: /backup")
    try:
        from drivers.oled import oled_log
        oled_two_data(1,1,"Downloading","Update")
    except Exception as e:
        print("OLED Error:", e)
    from ota_update import run_update
    run_update()
    oled_two_data(1,1,"Downloading","Completed")
    with open('schema.dat', 'r') as f:
        data = json.load(f)
    data["update_flag"]="False"
    data["download_flag"]="True"
    with open('config.txt', 'w') as f:
        json.dump(data, f)
    time.sleep(2)
if download_flag=="True":
    oled_two_data(1,1,"Installing","Update")
    time.sleep(.5)
    copy_all_content("/backup", "/")
    oled_two_data(1,1,"Updation","Completed")
    with open('schema.dat', 'r') as f:
        data = json.load(f)
    data["download_flag"]="False"
    with open('config.txt', 'w') as f:
        json.dump(data, f)
    time.sleep(1)
    
    
time.sleep(.5)
from process.save_html import save_html
from process.fetch_projects import fetch_projects


oled_two_data(1,1,"Setting up","Activities")
time.sleep(.5)
fetch_projects()
oled_two_data(1,1,"Updating","Files")
time.sleep(.5)
save_html()
oled_two_data(1,1,"Starting","Activities")
time.sleep(.5)