import os,json
def list_files_and_folders(directory):
	A=directory;B=[]
	try:
		G=os.listdir(A);C=[];D=[]
		for E in G:
			F=A+'/'+E
			try:H=os.listdir(F);D.append({'folder':F,'files':H})
			except OSError:C.append(E)
		if C:B.append({'folder':A,'files':C})
		if D:B.extend(D)
	except Exception as I:print('Error:',I)
	return B
def json_dumps_pretty(data):
	D=json.dumps(data);B='';C=0
	for A in D:
		if A=='{'or A=='[':B+=A+'\n'+'    '*(C+1);C+=1
		elif A=='}'or A==']':C-=1;B+='\n'+'    '*C+A
		elif A==',':B+=A+'\n'+'    '*C
		else:B+=A
	return B
def save_json_to_file(data,filename):
	A=filename
	with open(A,'w')as B:B.write(data.encode('utf-8'))
	print(f"File saved to: {A}")
directory_path='/'
folder_file_list=list_files_and_folders(directory_path)
folder_file_list.append(folder_file_list.pop(0))
json_data=json_dumps_pretty(folder_file_list)
output_filename='files_list.txt'
save_json_to_file(json_data,output_filename)
