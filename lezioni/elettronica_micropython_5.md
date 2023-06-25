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

Lezione 5 : un dado elettronico

Note:
- Usare task indipendenti

[comment]: # (!!! data-background-color="aqua")

## Teoria
- Task paralleli con multitasking cooperativo

Perché? È molto più semplice pensare a task indipendenti che a thread con stato condiviso

- Parole chiave Async / Await
- Create un task con asyncio.create_task()
- Yield con asyncio.sleep_ms()
- Eseguire i task con asyncio.run(..)
- Riprendere esempio dei due led che lampeggiano a frequenza diversa

[comment]: # (!!!)

## Come fare un dado elettronico ?

_Divide ut impera_

![Elefante](media/divide_ut_impera.jpg)

[comment]: # (!!!)

## Come fare un dado elettronico ?

1. Aspettare richiesta di un tiro **
2. Tirare un numero a caso *
3. Disegnare il risultato sullo schermo ***

[comment]: # (!!!)

## Problema 1 : aspettare richiesta di un tiro

Abbiamo visto la lezione precedente che esistono dei TouchPad

Possiamo chiedere all'utente di toccare un pin per lanciare un dado

&#x1F6B8; Breadboard

&#x1F6B8; Codice Micropython

```python
touch = TouchPad(Pin(4))

if touch.read() > 10000:
    # L'utente ha toccato il pin
```

[comment]: # (!!!)

## Problema 2 : tirare un numero caso

In Python e Micropython ci sono delle librerie che aggiungono funzioni utili

Esiste una libreria, random, con una funzione <code>randint</code> fa il caso nostro

&#x1F6B8; Nel REPL scrivete e raccogliete 6 risultati

```python
import random
print(random.randint(1,6))
```

E' veramente casuale ?

[Jupyter](https://jupyter.org/try-jupyter/retro/notebooks/?path=Untitled1.ipynb)

Note:
- Farli provare tutti nel REPL
- Ottenere 6 risposte per gruppo
- Sommare i risultati per ottenere in grafico di distribuzione

[comment]: # (!!!)

## Problema 3 : disegnare il dado

Come disegnare un dado ?

![Imagine](media/dado%20coordinate.png)

[comment]: # (!!!)

## Problema 3

![Elefante](media/divide_ut_impera.jpg)

Disegnare rettangoli e cerchi

[comment]: # (!!!)

## Problema 3.1 : Disegnare un rettangolo

&#x1F6B8; Disegnare un quadrato di lato 32 pixels in alto a sinistra

Python fornisce solo rettangoli

```python
display.fill_rect(0, 0, 32, 32, 1)
```

```
X =0
Y =0
Larghezza = 32
Lunghezza = 32
```

[comment]: # (!!!)

## Problema 3.2 : Disegnare un cerchio

&#x1F6B8; Disegnare un cerchio di raggio 4 pixels in posizione 16,16

Python fornisce solo elissi

```python
display.ellipse(16, 16, 4, 4, 0, True)
```

```
Centro del cerchio : X = 16, Y = 16
Semiasse orizzontale : 4 pixels
Semiasse verticale : 4 pixels
Colore dell'elisse : 0
Ultimo parametro True per riempire il cerchio
```

[comment]: # (!!!)

## Problema 3.3 : Disegnare più cerchi

Facciamo una lista di centri di cerchi

```python [1-2|3-5]
# Facciamo una lista di coordinate (tuple)
centri = [(16,16),(8,8),(24,24)]

for centro in centri:
    display.ellipse(centro[0], centro[1], 4, 4, 0, True)
```

[comment]: # (!!!)

## Problema 3.4 : Disegnare i cerchi giusti

<div class="twocolumn">
<div>

&#x1F6B8; Approntiamo le coordinate per ogni faccia del dado

<small>

| Gruppo | Coordinate dei puntini (X,Y) |
| -- | -- |
| 1 | (.., ..) |
| 2 | (.., ..) (.., ..) |
| 3 | (.., ..) (.., ..) (.., ..) |
| 4 | (.., ..) (.., ..) (.., ..) (.., ..) |
| 5 | (.., ..) (.., ..) (.., ..) (.., ..) (.., ..) |
| 6 | (.., ..) (.., ..) (.., ..) (.., ..) (.., ..) (.., ..) |

</small>
</div>
<div>

![Dado](media/dado%20coordinate.png)

</div>
</div>

[comment]: # (!!!)

## Problema 3.4 : Disegnare i cerchi giusti

Ci serve un elenco che, per ogni valore del dado, ci dia una lista di coordinate

Un dizionario (<code>dict</code>) fa il caso nostro

```
dict = { chiave1: valore2, chiave2: valore2, chiave3: valore3}
```

&#x1F6B8; Applichiamolo ai risultati di prima

```python [1|2|3|4|5|6]
coordinate = { 1: [(16,16)],
               2: [(8,8), (24,24)],
               3: [(8,8), (16,16), (24,24)],
               4: [(8,8), (8,24), (24,8), (24,24)],
               5: [(8,8), (8,24), (24,8), (24,24), (16,16)],
               6: [(8,8), (8,24), (24,8), (24,24), (8,16), (24,16)] }
```

[comment]: # (!!!)

## Problema 3 : la soluzione

&#x1F6B8; Mettere in main.py, salvare, RESET

```python [1|2-4|5-11|12-13|14-15|16-20|1-20]
def disegna_dado(valore_tratto):
    display.fill(0) 
    display.fill_rect(0, 0, 32, 32, 1)

    dado = { 1: [(16,16)],
             2: [(8,8), (24,24)],
             3: [(8,8), (16,16), (24,24)],
             4: [(8,8), (8,24), (24,8), (24,24)],
             5: [(8,8), (8,24), (24,8), (24,24), (16,16)],
             6: [(8,8), (8,24), (24,8), (24,24), (8,16), (24,16)] }
    
    puntini = dado[valore_tratto]
    for punto in puntini:
        display.ellipse(punto[0], punto[1], 4, 4, 0, True)

    display.show()

# Proviamo con un numero
disegna_dado(6)
```

[comment]: # (!!!)

## Il risultato

<iframe width="560" height="560" src="media/dado-micropython.mp4" title="Video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

[comment]: # (!!!)

## Fonti

Se volete continuare la scoperta dell'elettronica

- Board Arduino o ESP32
- La robottica
- TBD
- Altri componenti collegabili (motori, sensori)
- Connessioni dati

[comment]: # (!!!)