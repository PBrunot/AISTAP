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

Pascal Brunot | AISTAP | July 2023

Lezione 2 : Motori, Resistenze e Python

Note:
- Obiettivi
- Collegamento elettricità - magnetismo
- Motore DC 
- Approccio scientifico (osservazione-ipotesi-esperimento-conclusioni)
- Legge di Ohm
- Misurare resistenze
- Resistenze in parallelo e in serie

[comment]: # (!!!)

## Riassunto ultima lezione 1 / 2

Elettricità è *movimento di cariche elettriche*

Note:
- Abbiamo visto che l'elettricità è fondamentale nel mondo
- Abbiamo fatto circolare la corda fra le mani come l'elettricità nei conduttori
- Esistono conduttori e isolanti
- Abbiamo conosciuto alcuni scienzati famosi che hanno dato il loro nome a certe unità

[comment]: # (!!!)

## Riassunto ultima lezione

Le unità

| Grandezza (Abbr.) | Unità | Simbolo | Spiegazione |
| -- | -- | -- | -- |
| *Corrente* (I) | Ampère | A | Flusso delle cariche elettriche |
| *Tensione* (U o V) | Volt   | V | Potenziale delle cariche elettriche |
| *Resistenza* (R) | Ohm | Ω | "Freno" alle cariche elettriche |

[comment]: # (!!!)

## Riassunto ultima lezione

Abbiamo usato alcuni componenti elettrici...

- Pile (generatori di tensione)
- Fili
- Multimetro

[comment]: # (!!!)

## Magneti

Ricordare concetti base magneti
Poli - attrazione e ripulsione
Provate con i magneti che avete sul tavolo

Note:
- Cosa hanno i magneti ? (poli N e poli S)
- C'è però una differenza fondamentale - non esistono monopoli magnetici
- Abbiamo visto invece che esistono cariche elettriche isolate (palloni)

[comment]: # (!!!)

### La scoperta di Ørsted

Bussola e corrente elettrica (1820)

<iframe width="560" height="315" src="https://www.youtube.com/embed/h5N2grjG8d8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Magnetismo e elettricità sono legati

Si parla spesso di "elettromagnetismo"

Note:
- (Valutare se fare esperimento con batteria di macchina)
- L'elettricità era già nota e studiata da un secolo prima che si notasse questo effetto
- Maxwell nel 1864 scrisse le leggi che unificano elettricità e magnetismo
- vediamo come fare qualcosa di utile con tutti i due

[comment]: # (!!!)

### Uniamo elettricità e magnetismo

Costruiamo un motore elettrico

![Motor](media/motor%20symbol.png)

Note:
- Adesso scopriamo anche noi questo effetto nascosto

[comment]: # (!!!)

### Costruzione motore

Istruzioni
- Graffette su pongo
- Disporre bobina in mezzo alle graffette
- Collegare fili alle grafete
- Collegare batterie ai fili
- Dare un piccolo impulso alla bobina

Note:
- motore homopolo 
- quanto tutti hanno un motore funzionante passare alle domande

[comment]: # (!!!)

### Osservazione

Girano tutte nello stesso verso ?
Perché girano secondo voi ?
Provate a farlo girare nell'altro senso ?

[comment]: # (!!!)

### Ipotesi

- Senso di rotazione ?
- Motivo del movimento ?

Raccogliamo le vostre ipotesi

Note:
- "è l'elettricità" che lo fa girare ? -> allora togliamo il magnete
- "senso di rotazione diversi" -> cambiamo verso del magnete o della pila
- ricordare effetto di Orsted

[comment]: # (!!!)

### Spiegazione

Le cariche elettriche in movimento nella bobina creano un "magnete" che viene attratto o respinto dal magnete fisso

Questa spinta fa girare la bobina.

- esattamente come l'ago della bussola si spostava con la corrente
- però la bussola poi si fermava... perché questo no?

Note:
- Non è affatto semplice spiegare che il campo magnetico del magnete fisso attrae metà bobina e respinge metà bobina creando il movimento 
- Spiegare la regola della mano sinistra mi sembra troppo ambizioso

[comment]: # (!!!)

### Spiegazione

Ma perché non rimangono i magneti all’equilibrio e va avanti a girare ?
Trucco del filo conduttore solo a metà (si interrompe il magnete dopo mezzo giro per evitare questo)

Note:
- Trovare animazioni?
- Valutare se fare l'esperimento con multimetro e bobina in rotazione per osservare 
- Legge di Faraday $$ {\displaystyle {\mathcal {E}}=-{\frac {\mathrm {d} \Phi _{B}}{\mathrm {d} t}},} $$

[comment]: # (!!!)

### Resistenze

Simbolo elettrico e unità di misura
Fanno "resistenza" - Rallentano il flusso e si riscaldano

![Resistenza](media/resistor%20symbol.png)


[comment]: # (!!!)

### Resistenze

Le resistenze seguono la legge di Ohm

Tensione = Corrente x Resistenza

$$ U = R . I $$

Note:
- Usare Python per provare a fare l'operazione?
- Si possono manipolare i termini dell'equazione

---

### Resistenze

Un triangolo per ricordare

![VRI](media/ohm-law.jpg)

Esercizio Python


[comment]: # (!!!)

### Misura delle resistenze con il multimetro

Spiegare come si misurano le resistenze

Tabella risultati

Note:
- Le resistenze di misurano con il simbolo Ω
- Come le tensioni le resistenze di misurano fra due punti del circuito con il multimetro in parallelo

[comment]: # (!!!)

### Breadboard

Schede di connessione senza fili (come funzionano) (1 slide)
Collegamento verticale vs. orizzontali

![Breadboard](media/breadboard.jpg)

---

### Breadboard

Mettere 2 resistenze uguali una dopo l'altra
Mettere 2 resistenze uguali accanto l'uno l'altra

![Resistenze](media/resistenze.jpg)

Note:
- [Circuito](https://www.tinkercad.com/things/8aVDNguOsCs-sizzling-borwo/editel)
- Accanto = parallelo
- Dopo = Serie
- Fili = ricordatevi la corda che deve circolare

[comment]: # (!!!)

### Pausa Python 1/3

Installare Thonny

REPL

Sintassi tab

Ripasso variabili, funzioni

Parole chiavi def, return

[comment]: # (!!!)

### Pausa Python 2/3

Facciamo la formula delle resistenze in parallelo

$$ R_{parallelo} = \frac{1}{\frac{1}{R_{1}} + \frac{1}{R_{2}}} $$

```python [1-2|3-4]
def parallelo(r1, r2):
    return 1/(1/r1 + 1/r2)

print(parallelo(100, 200))
```

Verifica sperimentale con R=100 Ω, R=200 Ω, multimetro

Note:
- inverso della resistenza equivalente = Somma degli inversi delle resistenze
- Risultato atteso 66.66 Ω


[comment]: # (!!!)

### Pausa Python 3/3

Adesso facciamo la legge di Ohm in Python

$$ U = R . I $$

```python [1-2|3-4]
def ohm_u(r, i):
    return r * i

print(ohm_u(200, 0.1))
```

Risultato con R=200 Ω, I=0.1A ?

Note:
- Risultato 20 V
- Esercizi extra possibili

[comment]: # (!!!)

### Altri componenti

- Interruttori e simboli
- Bobina (induttore) e simbolo come "serbatoio di corrente" (in senso inverso...)
- Condensatori e simbolo come "serbatoio di tensione"

[comment]: # (!!!)

### Schema elettrico

Conclusione : leggiamo uno schema elettrico assieme
Riconoscere i simboli
Seguire la corrente
Qualche simbolo misterioso per la prossima lezione

[comment]: # (!!!)

