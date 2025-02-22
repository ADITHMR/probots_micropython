import network,json
def get_serial_no():
	try:
		B=network.WLAN(network.STA_IF);C=B.config('mac');D=C[3:];E=''.join('%02x'%A for A in D)
		with open('schema.dat','r')as F:A=json.load(F)
		G=f"{A['serial_prefix']}{E}{A['serial_suffix']}";return G
	except Exception as H:print('Error: on get_serial_no()',H);return'Serial Number ERROR'
def get_version():
	with open('version.dat','r')as A:B=json.load(A);C=f"{B['version']}";return C
def get_update_flag():
	try:
		with open('schema.dat','r')as B:A=json.load(B)
		if A['update_flag']=='enabled':return True
		elif A['update_flag']=='disabled':return False
		else:return'Error'
	except Exception as C:print('Error: on get_serial_no()',C);return'ERROR'
