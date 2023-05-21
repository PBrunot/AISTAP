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

## Elettronica con Micropython
![Micropython logo](media/micropython-logo.svg) <!-- .element: style="height:250px; max-width:200vw; image-rendering: crisp-edges;" -->

Pascal Brunot | AISTAP | July 2023

[comment]: # (!!!)

## Lezione 2

### Ripasso

Elettricità è *movimento di cariche elettriche*

| Grandezza (Abbr.) | Unità | Simbolo | Spiegazione |
| -- | -- | -- | -- |
| *Corrente* (I) | Ampère | A | Flusso delle cariche elettriche |
| *Tensione* (U o V) | Volt   | V | Potenziale delle cariche elettriche |
| *Resistenza* (R) | Ohm | Ω | "Freno" alle cariche elettriche |

Componenti: Pile
Strumenti: Voltmetro

[comment]: # (!!!)

### La scoperta di Ørsted

- Bussola e corrente elettrica (1820)

<iframe width="560" height="315" src="https://www.youtube.com/embed/h5N2grjG8d8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Magnetismo e elettricità sono legati
_vediamo come fare qualcosa di utile con tutti i due_

[comment]: # (!!!)

### Motori DC

[comment]: # (!!!)

Inizio con domanda/quesito : scopriamo un effetto nascosto dell’elettricità !

[comment]: # (!!!)

### Costruzione motore

come ? costruzione motore homopolo per illustrare collegamento con magnetismo

Osservazioni dei vari gruppi sotto la guida dell’insegnante

[comment]: # (!!!)

### Perché gira?

Sfida alla classe: perché gira ?

Formulazione ipotesi della classe
(il magnete attrae/repelle)
(ma perché solo con la pila?)
(osservazione senso di rotazione della bobina)

Test ipotesi:

Togliere magnete, usare bobina isolata
Cambio verso della pila ? (POLO ELETTRICO) – cambia senso
Cambio verso del magnete? (POLO MAGNETICO) – cambia senso

[comment]: # (!!!)
### Spiegazione

La corrente circolando nella bobina crea un "magnete" che viene attratto o rimando dal magnete fisso e questo fa girare la bobina.
Ma perché non rimangono i magneti all’equilibrio e va avanti a girare ?
Trucco del filo conduttore solo a metà (si interrompe il magnete dopo mezzo giro per evitare questo)

[comment]: # (!!!)

### Resistenze
Simbolo elettrico e unità di misura
Fanno "resistenza" - Rallentano il flusso e si riscaldano
>Legge di Ohm = Tensione = Corrente x Resistenza
```python
U = R * I 
```
---

Un triangolo per ricordare

![VRI](media/ohm-law.jpg)

[comment]: # (!!!)

### Misura delle resistenze con il multimetro

Tabella risultati

[comment]: # (!!!)
### Breadboard
Schede di connessione senza fili (come funzionano) (1 slide)
Collegamento verticale vs. orizzontali

---

Esperimento 
Sfida : Cosa succede se ne metto una dopo l’altra ? Una sopra l’altra? 

Ipotesi della classe
Misuriamo 

Mettere 2 resistenze uguali in serie
Mettere 2 resistenze uguali in parallelo

---

Misure resistenze (di valori uguali possibilmente così abbiamo come risultato 2R ; 0.5R)
 valore ottenuto, R1//R2=(R1+R2)/(R1*R2)

[comment]: # (!!!)
### Altri componenti

Cenni su altri componenti (3 slides)

Interruttori e simboli
Bobina (induttore) e simbolo come "serbatoio di corrente" (in senso inverso...)
Condensatori e simbolo come "serbatoio di tensione"

[comment]: # (!!!)
### Schema elettrico
Conclusione : leggiamo uno schema elettrico assieme
Riconoscere i simboli
Seguire la corrente
Qualche simbolo misterioso per la prossima lezione

[comment]: # (!!!)


```python [1-2|3|4]
a = 1
b = 2
c = x => 1 + 2 + x
c(3)
```
[comment]: # (!!!)

## Imaggine

[comment]: # (!!!)

## Fonti usate in questa presentazione
