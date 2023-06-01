[comment]: # (This presentation was made with markdown-slides)
[comment]: # (This is a CommonMark compliant comment. It will not be included in the presentation.)
[comment]: # (Compile this presentation with the command below)
[comment]: # (mdslides elettronica_micropython.md --include media)

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

L'ingrediente fondamentale

![P-N](https://www.youtube.com/watch?v=JBtEckh3L9Q&t=3s)

[comment]: # (!!!)

## Proviamo il diodo

- Esempio Diodo (schema costruzione fisica del diodo)
- Prova esperimentale con LED e polarità
- Riconoscere anodo da catodo
- Circuito Elettronico vs.circuito elettrico


## Circuiti integrati

- Cosa sono (tanti componenti – transistor) messi assieme per uno scopo (memorizzare, fare
operazioni logiche)
- Economici da fabbricare in grandi quantità
- Il transistor come oggetto più fabbricato dell’uomo …

[comment]: # (!!!)

## Struttura di una board

- Processore
- Memoria (Flash, RAM) e la differenza
- Micro-controllore (integrazione)
- Componenti di alimentazione
- Ingressi/Uscite del controllore
o GPIO
o Bus (USB x PC, SPI x LCD)
o RESET pin
o Power pin
- Schermo LCD

[comment]: # (!!!)

## Board

Accensione, collegamento USB (parte pratica)
- Thonny, arrivare al Python REPL
- Accendere e spegnere il led sulla board (machine.Pin(numero).on() / machine.Pin(numero).off())

[comment]: # (!!!)

## Riprendiamo Python