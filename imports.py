import machine
import time
import tm1637
import ssd1306
import neopixel
import _thread

from time import sleep
from machine import Pin,I2C

from ir_decode import *
from ir_rx.nec import NEC_8
from ir_rx.print_error import print_error

from esp_as_AP import *
from pin_mapping import *
from webServer import *
from display import *
from oled import *
from buzzer import *
from led_strip import *

from runProject import *

import ure  # MicroPython version of regular expressions
import socket
import network


