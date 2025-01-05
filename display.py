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
        sleep(.5)
        disp.show(d)
        sleep(delay)

def disp_scroll_str(data):
    disp.scroll(data, delay=200)
disp_scroll_str("PROBOT v1")