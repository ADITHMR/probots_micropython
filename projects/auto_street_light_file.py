


from imports import *





def auto_street_light_fun():
    last=0
    while True:
        if IR_LDR1.value() ==False:
            if last==0:
                all_set_color(255,255,255)
                disp_seq_str(["MOON"],0)
#                 oled_log("Street Light ON")
                oled_three_data(2,2,2,"Street","Light","ON")
                last=1
                one_beep()
        else:
            if last==1:
                all_set_color(0,0,0)
                disp_seq_str(["SUN"],0)
#                 oled_log("Street Light OFF")
                oled_three_data(2,2,2,"Street","Light","OFF")
                last=0
                one_beep()
        
