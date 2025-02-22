_A='Brightness out of range'
__version__='1.3.0'
from micropython import const
from machine import Pin
from time import sleep_us,sleep_ms
TM1637_CMD1=const(64)
TM1637_CMD2=const(192)
TM1637_CMD3=const(128)
TM1637_DSP_ON=const(8)
TM1637_DELAY=const(10)
TM1637_MSB=const(128)
_SEGMENTS=bytearray(b'?\x06[Ofm}\x07\x7fow|9^yq=v\x06\x1ev8UT?sgPmx>\x1c*vn[\x00@c')
class TM1637:
	def __init__(A,clk,dio,brightness=7):
		B=brightness;A.clk=clk;A.dio=dio
		if not 0<=B<=7:raise ValueError(_A)
		A._brightness=B;A.clk.init(Pin.OUT,value=0);A.dio.init(Pin.OUT,value=0);sleep_us(TM1637_DELAY);A._write_data_cmd();A._write_dsp_ctrl()
	def _start(A):A.dio(0);sleep_us(TM1637_DELAY);A.clk(0);sleep_us(TM1637_DELAY)
	def _stop(A):A.dio(0);sleep_us(TM1637_DELAY);A.clk(1);sleep_us(TM1637_DELAY);A.dio(1)
	def _write_data_cmd(A):A._start();A._write_byte(TM1637_CMD1);A._stop()
	def _write_dsp_ctrl(A):A._start();A._write_byte(TM1637_CMD3|TM1637_DSP_ON|A._brightness);A._stop()
	def _write_byte(A,b):
		for B in range(8):A.dio(b>>B&1);sleep_us(TM1637_DELAY);A.clk(1);sleep_us(TM1637_DELAY);A.clk(0);sleep_us(TM1637_DELAY)
		A.clk(0);sleep_us(TM1637_DELAY);A.clk(1);sleep_us(TM1637_DELAY);A.clk(0);sleep_us(TM1637_DELAY)
	def brightness(A,val=None):
		B=val
		if B is None:return A._brightness
		if not 0<=B<=7:raise ValueError(_A)
		A._brightness=B;A._write_data_cmd();A._write_dsp_ctrl()
	def write(A,segments,pos=0):
		if not 0<=pos<=5:raise ValueError('Position out of range')
		A._write_data_cmd();A._start();A._write_byte(TM1637_CMD2|pos)
		for B in segments:A._write_byte(B)
		A._stop();A._write_dsp_ctrl()
	def encode_digit(A,digit):return _SEGMENTS[digit&15]
	def encode_string(D,string):
		A=string;B=bytearray(len(A))
		for C in range(len(A)):B[C]=D.encode_char(A[C])
		return B
	def encode_char(B,char):
		A=ord(char)
		if A==32:return _SEGMENTS[36]
		if A==42:return _SEGMENTS[38]
		if A==45:return _SEGMENTS[37]
		if A>=65 and A<=90:return _SEGMENTS[A-55]
		if A>=97 and A<=122:return _SEGMENTS[A-87]
		if A>=48 and A<=57:return _SEGMENTS[A-48]
		raise ValueError("Character out of range: {:d} '{:s}'".format(A,chr(A)))
	def hex(A,val):B='{:04x}'.format(val&65535);A.write(A.encode_string(B))
	def number(B,num):A=num;A=max(-999,min(A,9999));C='{0: >4d}'.format(A);B.write(B.encode_string(C))
	def numbers(C,num1,num2,colon=True):
		B=num2;A=num1;A=max(-9,min(A,99));B=max(-9,min(B,99));D=C.encode_string('{0:0>2d}{1:0>2d}'.format(A,B))
		if colon:D[1]|=128
		C.write(D)
	def temperature(A,num):
		B=num
		if B<-9:A.show('lo')
		elif B>99:A.show('hi')
		else:C='{0: >2d}'.format(B);A.write(A.encode_string(C))
		A.write([_SEGMENTS[38],_SEGMENTS[12]],2)
	def show(B,string,colon=False):
		A=B.encode_string(string)
		if len(A)>1 and colon:A[1]|=128
		B.write(A[:4])
	def scroll(B,string,delay=250):
		A=string;C=A if isinstance(A,list)else B.encode_string(A);D=[0]*8;D[4:0]=list(C)
		for E in range(len(C)+5):B.write(D[0+E:4+E]);sleep_ms(delay)
class TM1637Decimal(TM1637):
	def encode_string(E,string):
		A=string;C=bytearray(len(A.replace('.','')));B=0
		for D in range(len(A)):
			if A[D]=='.'and B>0:C[B-1]|=TM1637_MSB;continue
			C[B]=E.encode_char(A[D]);B+=1
		return C