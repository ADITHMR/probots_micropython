from pin_mapping import *
from time import sleep


def disp_seq_num(data,delay):
    for d in data:
        disp.show("    ")
        sleep(.5)
        disp.number(d)
        sleep(delay)
def disp_seq_str(data,delay):
    for d in data:
        disp.show("    ")
        
#         sleep(.1)
        disp.show(d) 
        if delay!=0:
            sleep(delay)

def disp_scroll_str(data):
    disp.scroll(data, delay=150)
# disp_scroll_str("PROBOT v1")