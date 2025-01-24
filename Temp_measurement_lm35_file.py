from machine import Pin, ADC
import time
from imports import *

# Create ADC object on GPIO34 (or any ADC-capable pin)
adc = ADC(Pin(34))  # Use an appropriate GPIO pin
adc.atten(ADC.ATTN_0DB)  # Set the attenuation to 0 dB for 0-1V range (you can use others depending on your needs)
adc.width(ADC.WIDTH_12BIT)  # Set the resolution (12 bits is typical for ESP32)

# Conversion factor for LM35 (10mV per degree Celsius)
# ESP32 ADC values range from 0 to 4095
# 3.3V corresponds to ADC value 4095, so each step is approximately 0.0008V.
# LM35 gives 10mV/°C, so divide by 0.01 to get the temperature in Celsius.

def read_temperature():
    raw_value = adc.read()  # Read raw ADC value (0 to 4095)
    voltage = (raw_value / 4095) * 3.3  # Convert the raw value to a voltage
    temperature = voltage * 100  # Convert voltage to temperature (since LM35 gives 10mV per °C)
    return temperature

# Main loop
def Temp_measurement_lm35_fun():
    
    while True:
        temp = int(read_temperature())
        print("Temperature: {:.2f} °C".format(temp))
        formatted_temp = f"{temp}C" 
        oled_two_data(1,3,"Temperature",str(formatted_temp))
        disp_seq_str([formatted_temp],0)
        time.sleep(2)  # Wait for 2 seconds before taking another reading
