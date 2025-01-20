from imports import *

def buzzer_on():
    BUZZER.off()
def buzzer_off():
    BUZZER.on()   

def one_beep():
    buzzer_on()
    time.sleep(.2)
    buzzer_off()
   
#     time.sleep(.2)
def two_beep():
    buzzer_on()
    time.sleep_ms(50)
    buzzer_off()
    time.sleep_ms(50)
    buzzer_on()
    time.sleep_ms(75)
    buzzer_off()
    time.sleep_ms(50)
