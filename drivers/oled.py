import ssd1306,machine
i2c=machine.I2C(0,scl=machine.Pin(22),sda=machine.Pin(21))
try:global oled;oled=ssd1306.SSD1306_I2C(128,64,i2c);isOled=1
except:isOled=0
logData=['']
def oled_log(data):
	A=data
	if isOled==1:
		for B in range(0,len(A),16):
			if len(logData)>5:logData.pop(0)
			logData.append(A[B:B+16])
		C=0;oled.fill(0);oled.show()
		for A in logData:oled.text(A,0,C);C+=10
		oled.show()
def oled_two_data(s1,s2,head,value):
	B=value
	if isOled==1:oled.fill(0);C=s1*8+s2*8+3;H=(64-C)//3;A=(len(head)+2)*6*s1;E=(128-A)//2;D=(64-C)//2;oled.write_text(head,E,D,s1);A=(len(B)+2)*6*s2;F=(128-A)//2;G=D+s1*8+3;oled.write_text(B,F,G,s2);oled.show()
def oled_three_data(s1,s2,s3,head,value1,value2):
	D=value2;C=value1;A=s2
	if isOled==1:oled.fill(0);E=s1*8+A*8+s3*8+5;L=(64-E)//3;B=len(head)*6*s1;H=(128-B)//2;F=(64-E)//2;oled.write_text(head,H,F,s1);B=len(C)*6*A;I=(128-B)//2;G=F+s1*8+3;oled.write_text(C,I,G,A);B=len(D)*6*A;J=(128-B)//2;K=G+A*8+3;oled.write_text(D,J,K+1,s3);oled.show()