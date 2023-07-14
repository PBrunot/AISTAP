[comment]: # (THEME = league)
[comment]: # (CODE_THEME = base16/zenburn)
[comment]: # (controls: true)
[comment]: # (keyboard: true)
[comment]: # (markdown: { smartypants: true })
[comment]: # (hash: false)
[comment]: # (respondToHashChanges: false)
[comment]: # (slideNumber: true)


<style>
.reveal h1 { font-size: 2.5em; }
</style>
<style type="text/css">
    :root {
        --r-main-font-size: 32px;
    }
</style>
<style type="text/css">
.twocolumn {
   display: grid;
   grid-template-columns: 1fr 1fr;
   grid-gap: 10px;
   text-align: left;
}
</style>

[comment]: # (!!!)

## Elettronica con Micropython

![Micropython logo](media/micropython-logo.svg) <!-- .element: style="height:250px; max-width:200vw; image-rendering: crisp-edges;" -->

Pascal Brunot | AISTAP | Luglio 2023

Lezione 4 : Controllare LED, NeoPixel, LCD con Micropython

Note:
- Thonny, salvare file sul microprocessore
- Blink con LED interno
- Scrivere sul LCD
- LED esterno pilato da GPIO
- Blink alternati

[comment]: # (!!! data-background-color="aqua")


## Schermo LCD 1/2

La nostra board ha anche uno schermo piccolo, si usa così:

```python
display.text(testo, coordinata X, coordinata Y, colore [1 o 0])
display.show() 
```

<small>
Dimensioni schermo 

$$ 0 \leq X \leq 127 $$
$$ 0 \leq Y \leq 31 $$
</small>

&#x1F6B8; Fate scrivere "Ciao _nome_" *ad ogni poweron/reset*

[comment]: # (!!!)

## Schermo LCD 2/2

&#x1F6B8; Thonny > File > Apri > Dispositivo Micropython > main.py

Sostuitire con

```python
display.text('Ciao <nome>', 40, 12, 1)
display.show()
```

&#x1F6B8; Thonny > File > Salva

&#x1F6B8; Premere RESET

[comment]: # (!!!)

## Cicli

(ripasso Python)
&#x1F6B8;  Fare lampeggiare il led integrato con ciclo while True

```python
Pin(10, Pin.OUT)
while True:
    Pin(10).off() # E' scambiato
    sleep(1)
    Pin(10).on()
    sleep(1)
```

[comment]: # (!!!)

## TouchPAD

Il nostro ESP32 supporta la configurazione di alcuni PIN come sensori tattili

```python
from machine import TouchPad
from time import sleep_ms

tp = TouchPad(Pin(4))

while True:
    print(tp.read())
    sleep_ms(250)
```

Osservare il plotter

Note:
- Funziona perché il nostro corpo conduce un po' l'elettricità e perturba un oscillatore
- Aggiungere in boot.py gli import (from machine import TouchPad, from time import sleep_ms)

[comment]: # (!!!)

## TouchPAD

Accendiamo il LED quando rileviamo il tocco

```python
tp = TouchPad(Pin(4))
led = Pin(10, Pin.OUT)
SOGLIA = ... # Completare
while True:
    val = tp.read()
    if val > SOGLIA:
        led.off()
    else:
        led.on()
    print(val)
    sleep_ms(250)
```

```python
tp = TouchPad(Pin(4))
led = Pin(10, Pin.OUT)
SOGLIA = ... # Completare
while True:
    if tp.read() > SOGLIA:
        Pin(10).off()
        display.text('Ciao!', 40, 12, 1)
        display.show()
    else:
        Pin(10).on()
        display.text('Arrivederci!', 40, 12, 1)
        display.show()
    sleep_ms(250)
```

Note:
- Funziona perché il nostro corpo conduce un po' l'elettricità e perturba un oscillatore


&#x1F6B8;  Alternare il lampeggio fra i due LED

```python [6,8]
led1 = Pin(36, Pin.OUT)
led2 = Pin(10, Pin.OUT)

while True:
    led1.on()
    led2.off()    
    sleep(1)
    led1.off()
    led2.on()
    sleep(1)
```

[comment]: # (!!!)

## Esercizio 4

&#x1F6B8;  Fare lampeggiare il primo LED ogni 2 s e il secondo ogni secondo

```python [6,8]
led1 = Pin(36, Pin.OUT)
led2 = Pin(10, Pin.OUT)

while True:
    led1.on()
    led2.off()    
    sleep(1)
    led1.on()
    led2.on()
    sleep(1)
    led1.off()
    led2.off()
    sleep(1)
    led1.off()
    led2.on()
    sleep(1)
```

Se dovessi aggiungere un terzo LED ogni 5 secondi ?

Note:
- L'approccio con un unico ciclo infinito ha dei limiti
- Sarebbe più semplice creare più cicli 

[comment]: # (!!!)

## Blink

```python
import asyncio

led1 = Pin(36, Pin.OUT)
led2 = Pin(10, Pin.OUT)

async def blink_1():
    global led1
    while True:
        led1.value(not(led1.value()))
        await asyncio.sleep_ms(2000)

async def blink_2():
    global led2
    while True:
        led2.value(not(led2.value()))
        await asyncio.sleep_ms(1000)

def main():
    t1 = asyncio.create_task(blink_1)
    t2 = asyncio.create_task(blink_2)
    asyncio.gather(t1, t2)
```

Note:
- Obiettivo : dimostrare che le cose diventano difficili quando ci sono varie azioni da fare in parallelo.
- Se dovessi aggiungere 7 LED ?

[comment]: # (!!!)

## Asynchronous version

Aggiungiamo un conta secondi sul display

```python [5,19-25,30-31]
import asyncio

led1 = Pin(36, Pin.OUT)
led2 = Pin(10, Pin.OUT)
contatore = 0

async def blink_1():
    global led1
    while True:
        led1.value(not(led1.value()))
        await asyncio.sleep_ms(2000)

async def blink_2():
    global led2
    while True:
        led2.value(not(led2.value()))
        await asyncio.sleep_ms(1000)

async def conta():
    global contatore
    while True:
        contatore += 1
        display.text(str(contatore), 40, 12, 1)
        display.show()
        await asyncio.sleep_ms(1000)

def main():
    t1 = asyncio.create_task(blink_1)
    t2 = asyncio.create_task(blink_2)
    t3 = asyncio.create_task(conta)
    asyncio.gather(t1, t2, t3)
```

[comment]: # (!!!)

## Synchronous version

```python
contatore = 0
led1 = Pin(36, Pin.OUT)
led2 = Pin(10, Pin.OUT)

while True:
    led1.on()
    led2.off()
    contatore += 1
    display.text(str(contatore), 40, 12, 1)
    display.show()

    sleep(1)
    led1.on()
    led2.on()
    contatore += 1
    display.text(str(contatore), 40, 12, 1)
    display.show()

    sleep(1)
    led1.off()
    led2.off()
    contatore += 1
    display.text(str(contatore), 40, 12, 1)
    display.show()

    sleep(1)
    led1.off()
    led2.on()

    contatore += 1
    display.text(str(contatore), 40, 12, 1)
    display.show()
    sleep(1)
```

[comment]: # (!!!)

## NeoPixel

Il nostro ESP32 ha un LED RGB programmabile sul pin 48

I LED RGB si chiamano spesso NEOPIXEL

&#x1F6B8; Preparate il programma con Thonny con il colore che preferite

```python
pin = Pin(48, Pin.OUT)    # 48 è il PIN dello schema
np = NeoPixel(pin, 1)     # Un solo led   
np[0] = (255, 255, 255)   # Imposta il primo LED (0) con colori R, G, B
np.write()
```

---

## Colori RGB

![RGB](media/rgb.jpg)

&#x1F6B8; Esecuzione programma sulla board

[comment]: # (!!!)

## Slide aggiuntive

## Micropython: Sequenza di boot

Quando si accende il computer, parte il sistema operativo

Con Micropython al "power-on" o pulstane "reset"

- Esegue il file boot.py *non lo toccate*
- Esegue il file main.py *noi lavoremo qua*

Note:
- Nel file boot.py ho preparato gli import e le funzioni utili per il resto del corso

[comment]: # (!!!)

## Micropython 

Come programmare senza board collegata?

[WOKWI](https://wokwi.com/projects/305568836183130690)

Note:
- Quelli che hanno un computer e rete wifi si possono collegare a www.wokwi.com e selezionare "ESP32 with Micropython"

[comment]: # (!!!)

