import network,urequests,ujson,json,time,os,machine
from local_host.connect_wifi import connect_wifi
try:from drivers.oled import*
except Exception as e:print('Error:',e)
led=machine.Pin(2,machine.Pin.OUT)
progress=0
def connect_wifi(ssid,password):
	wlan=network.WLAN(network.STA_IF);wlan.active(True)
	if not wlan.isconnected():
		print('Connecting to WiFi...');wlan.connect(ssid,password);timeout=30
		while not wlan.isconnected()and timeout>0:time.sleep(1);timeout-=1
		if timeout==0:print('Failed to connect to Wi-Fi.');return False
	print('Connected to WiFi',wlan.ifconfig());return True
def get_github_file_list(owner,repo,path):
	url='https://raw.githubusercontent.com/ADITHMR/probots_micropython/refs/heads/device_branch/files_list.txt';print(f"Fetching file list from: {url}")
	try:
		response=urequests.get(url)
		if response.status_code==200:file_list=ujson.loads(response.text);print(file_list);return file_list
		else:print(f"Failed to fetch file list: {response.status_code}");return[]
	except Exception as e:print(f"Error fetching file list: {e}");return[]
def download_file(url,folder,filename):
	try:
		try:os.listdir(folder)
		except OSError:os.mkdir(folder);print(f"Created folder: {folder}")
		file_path=f"{folder}/{filename}";response=urequests.get(url)
		if response.status_code==200:
			with open(file_path,'w')as f:f.write(response.text)
			print(f"Downloaded and saved to: {file_path}")
		else:print(f"Failed to download {filename}: {response.status_code}")
	except Exception as e:print(f"Error downloading {filename}: {e}")
	finally:response.close()
def ota_update():
	global progress;progress=0;owner='ADITHMR';repo='probots_micropython';path='';file_folders=get_github_file_list(owner,repo,path);file_count=0
	for folder in file_folders:file_count+=len(folder['files'])
	if not file_folders:print('No files to update.');return
	finished_files=0
	for folder_data in file_folders:
		folder=folder_data['folder'];files=folder_data['files']
		for filename in files:
			print(f"Downloading {filename} from {folder}...");url=f"https://raw.githubusercontent.com/ADITHMR/probots_micropython/refs/heads/device_branch/"
			if folder=='/':url+=filename
			else:url+=folder.strip('/')+'/'+filename
			print(url);led.value(not led.value());download_file(url,folder.strip('/'),filename);finished_files+=1;progress=int(finished_files/file_count*100)
			try:from drivers.oled import oled_log;oled_two_data(1,3,'Updating',f"{progress}%")
			except Exception as e:print('OLED Error:',e)
			print(f"progress={progress}")
			if progress>=100:
				with open('schema.dat','r')as f:data=json.load(f)
				data['update_flag']='False'
				with open('schema.dat','w')as f:json.dump(data,f)
				try:from drivers.oled import oled_log;oled_two_data(1,3,'Update',f"Complete.");print('Update complete');time.sleep(1)
				except Exception as e:print('OLED Error:',e)
def run_update():
	try:
		if not connect_wifi():
			try:from drivers.oled import oled_log;oled_two_data(1,3,'WIFI Conn',f"Failed")
			except Exception as e:print('OLED Error:',e)
			time.sleep(2);return()
	except:
		if not connect_wifi(ssid='Probot',password='Probot@1234'):
			try:from drivers.oled import oled_log;oled_two_data(1,3,'WIFI Conn',f"Failed")
			except Exception as e:print('OLED Error:',e)
			time.sleep(2);return()
	try:ota_update()
	except Exception as e:
		print('Error on ota_update()',e)
		with open('schema.dat','r')as f:data=json.load(f)
		data['update_flag']='False'
		with open('schema.dat','w')as f:json.dump(data,f)
		from drivers.oled import oled_log;oled_two_data(1,3,'Update',f"Failed.");print('Update Failed')
