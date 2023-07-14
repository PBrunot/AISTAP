from machine import Pin, TouchPad
from neopixel import NeoPixel
import apa106
import random
def disegna_dado(display, value, pos = 0):
    WIDTH = 32
    RADIUS = 4
    if pos > 0:
        xmin = (WIDTH + 2) * pos
    else:
        xmin = 0
    
    display.fill_rect(xmin, 0, WIDTH, WIDTH, 1)
    coordinate = { 1: [(16,16)],
                   2: [(8,8), (24,24)],
                   3: [(8,8), (16,16), (24,24)],
                   4: [(8,8), (8,24), (24,8), (24,24)],
                   5: [(8,8), (8,24), (24,8), (24,24), (16,16)],
                   6: [(8,8), (8,24), (24,8), (24,24), (8,16), (24,16)] }
    
    for center in coordinate[value]:
        display.ellipse(xmin + center[0], center[1], RADIUS, RADIUS, 0, True)
    
    display.show()

def lcd_main():
    cpt = 0
    led = Pin(10, Pin.OUT)
    touch = TouchPad(Pin(4))

    NUM_DADI = 1

    while True:
        if touch.read() > 10000:
            print("Tiro il dado")
            display.fill(0)
            led.value(not led.value())
            for num_dado in range(0, NUM_DADI):
                disegna_dado(display, random.randint(1, 6), num_dado)
        time.sleep_ms(1000)
        cpt += 1

lcd_main()