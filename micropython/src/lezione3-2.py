# Versioni sincrone (classiche)

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

def blink_3s_11s():
    # 3 e 11 sono numeri primi, il minimo comune divisore è 1.
    # per farli lampeggiare serve un ciclo ogni secondo
    cpt = 0
    stato_led1 = False
    stato_led2 = False
    led1 = Pin(10, Pin.OUT)
    led2 = Pin(36, Pin.OUT)
    
    while True:
        if cpt % 3 == 0: # il contatore è divisibile da 3?
            stato_led1 = not stato_led1  # Inverte il valore corrent del led 1
            led1.value(stato_led1)
        if cpt % 11 == 0: # il contatore è divisbile da 11 ?
            stato_led2 = not stato_led2  # Inverte il valore corrente del led2
            led2.value(stato_led2)
        sleep(1)
        cpt += 1