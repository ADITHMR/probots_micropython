import machine,time
from machine import Pin,I2C
def set_pin_out(pin):A=pin;A=int(A);print(A);B=Pin(A,Pin.OUT);return B
def set_pin_in(pin):A=pin;A=int(A);return Pin(A,Pin.IN)
def get_trig_state(state):
	A=state
	if A=='Active Low':return 0
	elif A=='Active High':return 1
	else:return 0
