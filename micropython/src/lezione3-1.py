# imports da aggiungere nel boot.py
from time import sleep

# Accendere e spegnere il LED integrato
# Pin(10).on()
# Pin(10).off()

# Blink led integrato
def blink_led1():
    while True:
        Pin(10).on()
        sleep(1)
        Pin(10).off()
        sleep(1)

def blink_led_esterno():
    while True:
        Pin(36).on()
        sleep(1)
        Pin(36).off()
        sleep(1)

# Togliere il commento per eseguire
#blink_led1()
#blink_led_esterno()

def blink_2s_1s():
    led1 = Pin(10, Pin.OUT)
    led2 = Pin(36, Pin.OUT)
    while True:
        led1.on()
        led2.off()
        sleep(1)
        
        # led1.on() non serve
        led2.on()
        sleep(1)
        
        led1.off()
        led2.off()
        sleep(1)
        
        # led1.off() non serve
        led2.on()
        sleep(1)

