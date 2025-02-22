from time import sleep
import drivers.tm1637 as tm1637
from machine import Pin
disp=tm1637.TM1637(clk=Pin(27),dio=Pin(26))
def disp_seq_num(data,delay):
	for A in data:disp.show('    ');sleep(.5);disp.number(A);sleep(delay)
def disp_seq_str(data,delay):
	A=delay
	for B in data:
		disp.show('    ');disp.show(B)
		if A!=0:sleep(A)
def disp_scroll_str(data):disp.scroll(data,delay=150)