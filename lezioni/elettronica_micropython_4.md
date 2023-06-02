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

Lezione 4 : Micropython

Note:
- Thonny, salvare file sul microprocessore
- Blink con LED interno
- Scrivere sul LCD
- LED esterno pilato da GPIO
- Blink alternati

[comment]: # (!!! data-background-color="aqua")

## Teoria (5 slides)

- Micropython; ambiente di sviluppo compatibile (Thonny)
- Life-cycle (RESET / BOOT.PY / STARTUP.PY)
- Librerie machine.Pin ; time.sleep
- Librerie dispositivi (LCD) e come si aggiungono (pip -&gt; mip.install(...))

[comment]: # (!!!)

## Pratica

- Caricare un file PY in Thonny
- Caricare il file PY sul controllore

[comment]: # (!!!)

## Esercizio 1

Fare che la board scriva "Ciao nome" ad ogni poweron/reset

Per scrivere sul display bisogna fare

```python
display.text(testo, coordinata X, coordinata Y, colore [1 o 0])
display.show() 
```

Dimensioni schermo 

$$ 0 \leq X \leq 127 $$
$$ 0 \leq Y \leq 31 $$

---

Thonny > File > Apri > Dispositivo Micropython > main.py

```python
display.text('Ciao AISTAP!', 40, 12, 1)
display.show()
```

Thonny > File > Salva

Premere RESET

[comment]: # (!!!)

## Esercizio 2

Fare lampeggiare LED esterno con una resistenza
- Dare Pin-out delle board usata, ripassare GPIO / Bus
- Proiettare CIRCUITO DA REALIZZARE con simboli standard
- Realizzare un circuito con board su scheda a connessione senza fili
- Modificare script fornito per fare lampeggiare il LED
- Ripasso diodo (verso giusto)

[comment]: # (!!!)

## Esercizio 2 (soluzione)

WOKWI

Codice

[comment]: # (!!!)

## Esercizio 3

(ripasso Python)
- Fare lampeggiare il led integrato + il led esterno con ciclo while True
- Alternare il lampeggio fra i due LED
- Lampeggiare a tempo i due LED (1s)

[comment]: # (!!!)

## Esercizio 4

- Fare lampeggiare il primo LED ogni 2 s e il secondo ogni secondo
Obiettivo : dimostrare che le cose diventano difficili quando ci sono varie azioni da fare in parallelo.
Se dovessi aggiungere 7 LED ?

[comment]: # (!!!)

## TouchPAD

[comment]: # (!!!)

## NeoPixel

[comment]: # (!!!)

## Conclusioni