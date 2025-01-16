from file_mgr import  *
from oled import *


IR_DATA=0
# User callback for IR receiver
def get_IR_data():
    global IR_DATA
    return int(IR_DATA)

    
def callback(data, addr, ctrl):
    proj=get_parameter("PROJECT") 
    if data < 0:  # NEC protocol sends repeat codes.
        pass
    else:
        
        
        if decodeKeyValue(data)>-1 or decodeKeyValue(data)<10:
            global IR_DATA
            IR_DATA=decodeKeyValue(data)
            print(f"mode={get_IR_data()}")
            
        oled_log(f"IR-> {decodeKeyValue(data)}")
        print(decodeKeyValue(data))
        
            
           

# Decode the received data and return the corresponding key name
def decodeKeyValue(data):
    if data == 0x16:
        return 0
    if data == 0x0C:
        return 1
    if data == 0x18:
        return 2
    if data == 0x5E:
        return 3
    if data == 0x08:
        return 4
    if data == 0x1C:
        return 5
    if data == 0x5A:
        return 6
    if data == 0x42:
        return 7
    if data == 0x52:
        return 8
    if data == 0x4A:
        return 9
    if data == 0x09:
        return "EQ"
    if data == 0x15:
        return "+"
    if data == 0x7:
        return "+"
    if data == 0x0D:
        return "U/SD"
    if data == 0x19:
        return "CYCLE"
    if data == 0x44:
        return "BACKWARD"
    if data == 0x43:
        return "PLAY/PAUSE"
    if data == 0x40:
        return "FORWARD"
    if data == 0x45:
        return "CH-"
    if data == 0x47:
        return "CH+"
    if data == 0x46:
        return "CH"
    return "ERROR"

