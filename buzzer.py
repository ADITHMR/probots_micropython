from imports import *
from machine import PWM

buzzer = PWM(BUZZER, freq=1000, duty=512)  
def buzzer_on(frequency=1000, duty_cycle=512):
    buzzer.freq(frequency)    # Set the frequency of the buzzer
    buzzer.duty(duty_cycle)   # Set the duty cycle (controls volume)
    
def buzzer_off():
    buzzer.duty(0)  # Set the duty cycle to 0, turning the buzzer off
buzzer_off()

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
