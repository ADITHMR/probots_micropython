import json
from local_host.web_page import web_page
from machine_id import get_serial_no
from utils import get_jsonvalue_from_file,read_file,write_file
import gc
from drivers.oled import oled_log
def save_html():
	gc.collect()
	try:
		try:D=get_jsonvalue_from_file('project/project_description.dat','activity1');E=get_jsonvalue_from_file('activity1/config.txt','project_name');B=get_jsonvalue_from_file('activity1/web_data.html','data');B=str(B).replace("'",'"').replace('True','true');A=read_file('local_host/project_page.html');A=A.replace('{*config_list*}',str(B));A=A.replace('{*heading*}',E);A=A.replace('{Project_description}',D);write_file('html/activity1.html',A);del A;print('Saved activity1.html');oled_log('Saved activity1.html');gc.collect()
		except Exception as C:print("Error on 'save_html() on activity1':",C)
		try:D=get_jsonvalue_from_file('project/project_description.dat','activity2');E=get_jsonvalue_from_file('activity2/config.txt','project_name');B=get_jsonvalue_from_file('activity2/web_data.html','data');B=str(B).replace("'",'"').replace('True','true');A=read_file('local_host/project_page.html');A=A.replace('{*config_list*}',str(B));A=A.replace('{*heading*}',E);A=A.replace('{Project_description}',D);write_file('html/activity2.html',A);del A;print('Saved activity2.html');oled_log('Saved activity2.html');gc.collect()
		except Exception as C:print("Error on 'save_html() on activity2':",C)
		try:D=get_jsonvalue_from_file('project/project_description.dat','activity3');E=get_jsonvalue_from_file('activity3/config.txt','project_name');B=get_jsonvalue_from_file('activity3/web_data.html','data');B=str(B).replace("'",'"').replace('True','true');A=read_file('local_host/project_page.html');A=A.replace('{*config_list*}',str(B));A=A.replace('{*heading*}',E);A=A.replace('{Project_description}',D);write_file('html/activity3.html',A);del A;print('Saved activity3.html');oled_log('Saved activity3.html');gc.collect()
		except Exception as C:print("Error on 'save_html() on activity3':",C)
		try:D=get_jsonvalue_from_file('project/project_description.dat','activity4');E=get_jsonvalue_from_file('activity4/config.txt','project_name');B=get_jsonvalue_from_file('activity4/web_data.html','data');B=str(B).replace("'",'"').replace('True','true');A=read_file('local_host/project_page.html');A=A.replace('{*config_list*}',str(B));A=A.replace('{*heading*}',E);A=A.replace('{Project_description}',D);write_file('html/activity4.html',A);del A;print('Saved activity4.html');oled_log('Saved activity4.html');gc.collect()
		except Exception as C:print("Error on 'save_html() on activity4':",C)
		try:D=get_jsonvalue_from_file('project/project_description.dat','activity5');E=get_jsonvalue_from_file('activity5/config.txt','project_name');B=get_jsonvalue_from_file('activity5/web_data.html','data');B=str(B).replace("'",'"').replace('True','true');A=read_file('local_host/project_page.html');A=A.replace('{*config_list*}',str(B));A=A.replace('{*heading*}',E);A=A.replace('{Project_description}',D);write_file('html/activity5.html',A);del A;print('Saved activity5.html');oled_log('Saved activity5.html');gc.collect()
		except Exception as C:print("Error on 'save_html() on activity5':",C)
		try:F=str(web_page()).replace('{machine_id}',f"S/N: {get_serial_no()}");write_file('local_host/index_page.html',F);del F;gc.collect();oled_log('Saved index.html');oled_log('Saved all html files');print('Successfully saved HTML files...')
		except Exception as C:print("Error on 'save_html() on indexpage':",C);traceback.print_exc()
	except Exception as C:print("Error on 'save_html()':",C)
