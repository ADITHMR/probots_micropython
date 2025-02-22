import neopixel,machine
class CustomNeoPixel:
	def __init__(A,pin,num_pixels,enabled=True):
		A.is_enabled=enabled;A.num_pixels=num_pixels
		if A.is_enabled:A.np=neopixel.NeoPixel(machine.Pin(pin,machine.Pin.OUT),A.num_pixels)
	def set_color(A,index,r,g,b):
		B=index
		if A.is_enabled:
			if 0<=B<len(A.np):A.np[B]=r,g,b;A.np.write()
	def clear(A):
		if A.is_enabled:A.np.fill((0,0,0));A.np.write()
	def set_color_All(A,r,g,b):
		if A.is_enabled:
			for B in range(A.num_pixels):A.set_color(B,r,g,b)