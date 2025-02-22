from process.file_mgr import*
from drivers.oled import*
IR_DATA=0
def get_IR_data():global IR_DATA;return int(IR_DATA)
def set_IR_data(data):
	global IR_DATA
	if data>-1 and data<15:IR_DATA=data
def callback(data,addr,ctrl):
	if data<0:pass
	else:
		ir_data=decodeKeyValue(data)
		if ir_data>-1 and ir_data<19:global IR_DATA;IR_DATA=ir_data;print(f"mode={get_IR_data()}");oled_log(f"IR-> {decodeKeyValue(data)}");print(decodeKeyValue(data))
def decodeKeyValue(data):
	if data==22:return 0
	if data==12:return 1
	if data==24:return 2
	if data==94:return 3
	if data==8:return 4
	if data==28:return 5
	if data==90:return 6
	if data==66:return 7
	if data==82:return 8
	if data==74:return 9
	if data==9:return 18
	if data==21:return 16
	if data==7:return 17
	if data==13:return'U/SD'
	if data==25:return'CYCLE'
	if data==68:return 13
	if data==67:return 15
	if data==64:return 14
	if data==69:return 10
	if data==71:return 12
	if data==70:return 11
	return'ERROR'