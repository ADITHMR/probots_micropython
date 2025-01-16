


from imports import *

num_pixels = 5
np = neopixel.NeoPixel(LED_STRIP, num_pixels)
def set_color(r, g, b):
    for i in range(num_pixels):
        np[i] = (r, g, b)  # Set the color (Red, Green, Blue)
    np.write()  # Write the data to the strip






def auto_street_light_fun():
    last=0
    while True:
        if IR_LDR1.value() ==False:
            if last==0:
                set_color(255,255,255)
                disp_seq_str(["MOON"],0)
                oled_log("Street Light ON")
                last=1
                one_beep()
        else:
            if last==1:
                set_color(0,0,0)
                disp_seq_str(["SUN"],0)
                oled_log("Street Light OFF")
                last=0
                one_beep()
        
