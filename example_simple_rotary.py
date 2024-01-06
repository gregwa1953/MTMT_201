# MIT License (MIT)
# Copyright (c) 2021 Mike Teachman
# https://opensource.org/licenses/MIT
# ==============================================
# Modified by G.D. Walters 12/10/2023
# ==============================================
# Tested with Keyes Ky-040 Rotary Encoder
# Files required for project...
#     example_simple_rotary.py (this file)
#     rotary_irq_rp2.py
#     rotary.py
# ==============================================
#   Clockwise rotation increases value
#   Anti-Clockwise rotation decreases value
# ==============================================
# example for MicroPython rotary encoder

from machine import I2C
import sys
if sys.platform == 'esp8266' or sys.platform == 'esp32':
    from rotary_irq_esp import RotaryIRQ
elif sys.platform == 'pyboard':
    from rotary_irq_pyb import RotaryIRQ
elif sys.platform == 'rp2':
    from rotary_irq_rp2 import RotaryIRQ
else:
    print('Warning:  The Rotary module has not been tested on this platform')

import time
# For SSD1306 OLED Display
from ssd1306 import SSD1306_I2C
import framebuf

# ======================================
# Base setup for the SSD1306
# ======================================
## Set the Width of the OLED Display
WIDTH = 128
# Set the Height of the OLED Display
HEIGHT = 32
oled_i2c = I2C(1)
oled = SSD1306_I2C(WIDTH, HEIGHT, oled_i2c)
oled.fill(0)
oled.text("Starting up!", 5,8)
oled.show()
# ======================================

button = machine.Pin(14,machine.Pin.IN,machine.Pin.PULL_UP)   # set GPIO 14 (pin 19) as INPUT with PULL_UP
r = RotaryIRQ(pin_num_clk=12,
              pin_num_dt=13,
              min_val=0,
              max_val=15,
              reverse=True,
              range_mode=RotaryIRQ.RANGE_WRAP)

val_old = r.value()
print('result =', val_old)
while True:
    val_new = r.value()

    if val_old != val_new:
        val_old = val_new
        print('result =', val_new)
        oled.fill(0)    
        oled.text(str(val_new), 5,8)
        oled.show()        
    if button.value() == 0:
        print("Switch Pressed")
        oled.fill(0)    
        oled.text("Switch Pressed", 5,8)
        oled.show()        
    #time.sleep_ms(50)

    time.sleep_ms(50)    