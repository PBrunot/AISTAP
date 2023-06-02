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

Lezione 3

[comment]: # (!!!)

## I semi-conduttori

I componenti che abbiamo usati fin'ora erano lineari

- Differenza con conduttori e isolanti

Note:

- Lineari perché per resistenze U = R x I, Induttanze U = L x dV/dt, Capacità I =C x dV/dt

[comment]: # (!!!)

## La giunzione P-N

L'ingrediente fondamentale del diodo

![P-N](https://www.youtube.com/watch?v=JBtEckh3L9Q&t=3s)

[comment]: # (!!!)

## Proviamo il diodo elettroluminescente ("LED")

<div class="twocolumn">
<div>

- Riconoscere anodo da catodo
- Simbolo

![Symbol](media/symbol-diode2.png)

</div>
<div>

![LED](media/led.png)

</div>
</div>

[comment]: # (!!!)

## Esperimentazione

Schema di collegamento

[TinkerCad](https://www.tinkercad.com/things/8zAUERdv001)

Misurate la caduta di tensione attorno al LED

<small>

| Gruppo | Caduta di tensione |
| -- | -- |
| 1 | ..... V |
| 2 | ..... V |
| 3 | ..... V |
| 4 | ..... V |
| 5 | ..... V |
| 6 | ..... V |

</small>

[comment]: # (!!!)

## Circuiti integrati

- Cosa sono (tanti componenti – transistor) messi assieme per uno scopo (memorizzare, fare
operazioni logiche)
- Economici da fabbricare in grandi quantità
- Il transistor come oggetto più fabbricato dell’uomo …

[comment]: # (!!!)

## Struttura di una board

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

## Board

Accensione, collegamento USB (parte pratica)

- Thonny, arrivare al Python REPL
- Accendere e spegnere il led sulla board (machine.Pin(numero).on() / machine.Pin(numero).off())


[comment]: # (!!!)

## Riprendiamo Python
