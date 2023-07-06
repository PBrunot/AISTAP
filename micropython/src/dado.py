from machine import Pin, TouchPad
from neopixel import NeoPixel
import apa106
import random
import uasyncio as asyncio
from time import sleep_ms, sleep

import time

ultimo_tiro = time.time()

async def animazione_neopixel(np):
    global ultimo_tiro
    lista = [0,1,2,5,4,3]
    while True:
        cpt_anim = 0
        while time.time() - ultimo_tiro > 3:
            cpt_anim = (cpt_anim + 1) % len(lista)
            for i in range(0,PXL_NUM):
                if i == lista[cpt_anim]:
                    color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
                else:
                    color = (0,0,0)
                np[i] = color
            np.write()
            await asyncio.sleep_ms(80)
        await asyncio.sleep_ms(100)
        
async def tira_dado(np, touch, led):
    global ultimo_tiro
    while True:
        if touch.read() > 10000:
            ultimo_tiro = time.time()
            print("Tiro il dado")
            led.value(not led.value())
            tiro = random.randint(1,6)
            for i in range(0,4):
                dado_neopixel(np, tiro)
                await asyncio.sleep_ms(250)
                dado_neopixel(np, 0)
                await asyncio.sleep_ms(100)     
            await asyncio.sleep_ms(1000)
        await asyncio.sleep_ms(100)

async def neopixel_main():
    led = Pin(10, Pin.OUT)
    touch = TouchPad(Pin(4))

    np=apa106.APA106(Pin(6, Pin.OUT), PXL_NUM, bpp=3, timing=1)

    t1 = asyncio.create_task(tira_dado(np, touch, led))
    t2 = asyncio.create_task(animazione_neopixel(np))
    await asyncio.gather(t1,t2)
    
def dado_neopixel(np, valore):
    dado = {0:[],1:[6],2:[3,2], 3:[3,2,6], 4:[0,2,3,5], 5:[0,2,3,5,6], 6:[0,1,2,3,4,5]}
    colors = [(0,0,255),(0,255,0),(255,0,0),(255,255,0),(255,0,255),(0,255,255),(255,255,255)]
    color = colors[random.randint(0,6)]
    for i in range(0, PXL_NUM):
        if i in dado[valore]:
            np[i] = color	
        else:
            np[i] = (0,0,0)
    np.write()
    
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

    NUM_DADI = 3

    while True:
        if touch.read() > 10000:
            print("Tiro il dado")
            display.fill(0)
            led.value(not led.value())
            for num_dado in range(0, NUM_DADI):
                disegna_dado(display, random.randint(1, 6), num_dado)
        time.sleep_ms(1000)
        cpt += 1

PXL_NUM = 7
asyncio.run(neopixel_main())
