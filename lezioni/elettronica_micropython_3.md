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

Lezione 3 : semi-conduttori, diodi, board ESP32

[comment]: # (!!! data-background-color="aqua")

## I semi-conduttori

I componenti che abbiamo usati fin'ora erano lineari

- Alcuni materiali possono essere sia isolanti che conduttori
- Li chiamiamo semi-conduttori

Note:
- Lineari perché per resistenze U = R x I, Induttanze U = L x dV/dt, Capacità I =C x dV/dt
- Esempi : diodi, transistori, celle fotovoltaiche
- Ricordate perché alcuni materiali lasciano passare la corrente elettrica?

[comment]: # (!!!)

## La giunzione P-N

L'ingrediente fondamentale del diodo

![P-N](https://www.youtube.com/watch?v=JBtEckh3L9Q&t=3s)

Note:
- Prima di usare un semiconduttore dobbiamo capire il principio fisico che lo rende possibile.
- Valutare se tagliare o meno. E' interessante il video ma troppo lungo.

[comment]: # (!!!)

## Proviamo il diodo elettroluminescente ("LED")

<div class="twocolumn">
<div>

Riconoscere anodo da catodo

Simbolo

![Symbol](media/symbol-diode2.png)

</div>
<div>

![LED](media/led.png)

</div>
</div>

[comment]: # (!!!)

## Esperimentazione

&#x1F6B8; Collegare come da schema con le vostre pile e la resistenza

[TinkerCad](https://www.tinkercad.com/things/8zAUERdv001)

&#x1F6B8; Misurate la tensione attorno al LED (1) e alla resistenza (2)

<small>

| Gruppo | Tensione U(LED) | Tensione U(R) |
| -- | -- | -- | 
| 1 | ..... V | .... V |
| 2 | ..... V | .... V |
| 3 | ..... V | .... V |
| 4 | ..... V | .... V |
| 5 | ..... V | .... V |
| 6 | ..... V | .... V |

</small>

Note:
- Fare osservare la correlazione con il colore?
- Fare osservare che U(LED) + U(R) = U(pile) - Legge di Kirshoff
- La caduta di tensione è dovuta alla giunzione P-N ed è indipendente dalla corrente

[comment]: # (!!!)

## Circuiti integrati

Cosa sono (tanti componenti – transistor) messi assieme per uno scopo (memorizzare, fare
operazioni logiche)

Economici da fabbricare in grandi quantità

Il transistor come oggetto più fabbricato dell’uomo

[comment]: # (!!!)

## Struttura della board S2 PICO

<div class="twocolumn">
<div>

- Microprocessore con memoria integrata
- Antenna WiFi
- Componenti di alimentazione
- Ingressi/Uscite del controllore (GPIO)
- Bus (USB x PC, SPI x LCD)
- Pulsanti (RESET, GPIO0)
- Schermo LCD (128x32 pixels)

</div>
<div>

![Board](media/Wemos-S2-Pico-pinout.webp)

</div>
</div>

[comment]: # (!!!)

## Board S2 PICO - primo uso

&#x1F6B8; Collegamento USB al computer

&#x1F6B8; Individuare la porta seriale (COM)

&#x1F6B8; Configurare Thonny per usare ESP32 con porta COM

&#x1F6B8; Nel REPL dovreste vedere Micropython

&#x1F6B8; Accendere il led blu sulla board

```python
Pin(10).on()
```

Note:
- Porta seriale varia da computer
- Tutti devono collegare il computer una volta
- Quando scollegano la board si spegne il LED

[comment]: # (!!!)

&#x1F6B8; Spegnere il led blu sulla board

```python
Pin(10).off()
```

Note:
- Porta seriale varia da computer

[comment]: # (!!!)

## Come provare senza essere connesso alla BOARD

[WOKWI ESP32](https://wokwi.com/projects/new/micropython-esp32)

![Struttura](media/wokwi-struttura.png)

Note:
- Serve connessione internet
- Possibile collegare vari componenti

[comment]: # (!!!)

## Conclusioni

Sito Micropython (dove scaricare firmware e documentazione)

[Micropython](https://micropython.org/)

Componenti usati

- [S2 Pico](https://www.wemos.cc/en/latest/s2/s2_pico.html)

- [Ali Express](https://it.aliexpress.com/item/1005003215673294.html) 

- [APA 106](https://it.aliexpress.com/item/1005001863273661.html)

[comment]: # (!!!)