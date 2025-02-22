from micropython import const
import framebuf
SET_CONTRAST=const(129)
SET_ENTIRE_ON=const(164)
SET_NORM_INV=const(166)
SET_DISP=const(174)
SET_MEM_ADDR=const(32)
SET_COL_ADDR=const(33)
SET_PAGE_ADDR=const(34)
SET_DISP_START_LINE=const(64)
SET_SEG_REMAP=const(160)
SET_MUX_RATIO=const(168)
SET_IREF_SELECT=const(173)
SET_COM_OUT_DIR=const(192)
SET_DISP_OFFSET=const(211)
SET_COM_PIN_CFG=const(218)
SET_DISP_CLK_DIV=const(213)
SET_PRECHARGE=const(217)
SET_VCOM_DESEL=const(219)
SET_CHARGE_PUMP=const(141)
class SSD1306(framebuf.FrameBuffer):
	def __init__(A,width,height,external_vcc):A.width=width;A.height=height;A.external_vcc=external_vcc;A.pages=A.height//8;A.buffer=bytearray(A.pages*A.width);super().__init__(A.buffer,A.width,A.height,framebuf.MONO_VLSB);A.init_display()
	def init_display(A):
		for B in(SET_DISP,SET_MEM_ADDR,0,SET_DISP_START_LINE,SET_SEG_REMAP|1,SET_MUX_RATIO,A.height-1,SET_COM_OUT_DIR|8,SET_DISP_OFFSET,0,SET_COM_PIN_CFG,2 if A.width>2*A.height else 18,SET_DISP_CLK_DIV,128,SET_PRECHARGE,34 if A.external_vcc else 241,SET_VCOM_DESEL,48,SET_CONTRAST,255,SET_ENTIRE_ON,SET_NORM_INV,SET_IREF_SELECT,48,SET_CHARGE_PUMP,16 if A.external_vcc else 20,SET_DISP|1):A.write_cmd(B)
		A.fill(0);A.show()
	def poweroff(A):A.write_cmd(SET_DISP)
	def poweron(A):A.write_cmd(SET_DISP|1)
	def contrast(A,contrast):A.write_cmd(SET_CONTRAST);A.write_cmd(contrast)
	def invert(A,invert):A.write_cmd(SET_NORM_INV|invert&1)
	def rotate(A,rotate):B=rotate;A.write_cmd(SET_COM_OUT_DIR|(B&1)<<3);A.write_cmd(SET_SEG_REMAP|B&1)
	def show(A):
		B=0;C=A.width-1
		if A.width!=128:D=(128-A.width)//2;B+=D;C+=D
		A.write_cmd(SET_COL_ADDR);A.write_cmd(B);A.write_cmd(C);A.write_cmd(SET_PAGE_ADDR);A.write_cmd(0);A.write_cmd(A.pages-1);A.write_data(A.buffer)
	def write_text(B,text,x,y,size):
		C=text;A=size;H=0;E=[];B.text(C,x,y)
		for F in range(x,x+8*len(C)):
			for G in range(y,y+8):I=B.pixel(F,G);E.append((F,G,I))
		B.text(C,x,y,H)
		for D in E:B.fill_rect(A*D[0]-(A-1)*x,A*D[1]-(A-1)*y,A,A,D[2])
class SSD1306_I2C(SSD1306):
	def __init__(A,width,height,i2c,addr=60,external_vcc=False):A.i2c=i2c;A.addr=addr;A.temp=bytearray(2);A.write_list=[b'@',None];super().__init__(width,height,external_vcc)
	def write_cmd(A,cmd):A.temp[0]=128;A.temp[1]=cmd;A.i2c.writeto(A.addr,A.temp)
	def write_data(A,buf):A.write_list[1]=buf;A.i2c.writevto(A.addr,A.write_list)
class SSD1306_SPI(SSD1306):
	def __init__(A,width,height,spi,dc,res,cs,external_vcc=False):B=res;A.rate=10485760;dc.init(dc.OUT,value=0);B.init(B.OUT,value=0);cs.init(cs.OUT,value=1);A.spi=spi;A.dc=dc;A.res=B;A.cs=cs;import time as C;A.res(1);C.sleep_ms(1);A.res(0);C.sleep_ms(10);A.res(1);super().__init__(width,height,external_vcc)
	def write_cmd(A,cmd):A.spi.init(baudrate=A.rate,polarity=0,phase=0);A.cs(1);A.dc(0);A.cs(0);A.spi.write(bytearray([cmd]));A.cs(1)
	def write_data(A,buf):A.spi.init(baudrate=A.rate,polarity=0,phase=0);A.cs(1);A.dc(1);A.cs(0);A.spi.write(buf);A.cs(1)
__version__='0.1.0'