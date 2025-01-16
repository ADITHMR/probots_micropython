import ssd1306
from pin_mapping import *
# Initialize I2C bus (SCL, SDA pins)
i2c = machine.I2C(0, scl=machine.Pin(22), sda=machine.Pin(21))

try:
    # Create an OLED object connected to the I2C bus
    global oled
    oled = ssd1306.SSD1306_I2C(128, 64, i2c)
    isOled=1
except:
    isOled=0

# Clear the display (optional)

logData=[""]
# Display text
def oled_log(data):
    if isOled==1:
        for i in range(0, len(data), 16):
            # Append each chunk (substring) to the list
            if len(logData )>5:
                logData.pop(0)
            logData.append(data[i:i+16])
            
        
        
        line=0
        oled.fill(0)
        oled.show()
        for data in  logData:
            oled.text(data,0,line)
            line+=10
        oled.show()
        


        
  