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
[comment]: # (center: false)

<style>
.reveal h1 { font-size: 2.5em; }
</style>
<style type="text/css">
    :root {
        --r-main-font-size: 35px;
    }
</style>

## Elettronica con Micropython
![Micropython logo](media/micropython-logo.svg) <!-- .element: style="height:250px; max-width:200vw; image-rendering: crisp-edges;" -->

Pascal Brunot | AISTAP | July 2023

Note:
- Electricity concepts
- The idea of electricity involving a ‘flow’ (of … something… see 3!)
- The idea of a ‘complete circuit’ being necessary for the flow to occur (in a battery-powered circuit)
- The idea of charge (what flows in circuits)
- The idea of current (the rate of flow of charge)
- The idea of potential difference (the cause of the flow – ideas about how PD links to transferred energy)
- The idea of resistance (a measure of the ‘opposition’ to the flow of charge)

[comment]: # (!!!)

## Introduzione

Perché queste due parole assieme ? Cosa possono fare ?

<iframe width="560" height="315" src="https://www.youtube.com/embed/aXW4dqvjFx0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

[comment]: # (!!!)
## Introduzione

1. Per programmare questi robot ci vuole ... Micropython
2. Per capire i componenti elettronica ci vuole... un po' di fisica
3. Inizieremo a capire l'elettricità nelle prossime lezioni

Note:
- Chiarire che non costruiremo un robot

[comment]: # (!!!)


## Lezione 1
Elettricità

Note:
- Oggi sarà la lezione più teorica di tutte perché dobbiamo imparare i concetti
- Ma ci divertiremo anche facendo esperimenti
- Materiali richiesti: palloni. pezzi di carta tagliati, piatto, corda 5-10m un po spessa
- Il top sarebbero palloni di alluminio stile elio che si potrebbero scaricare

[comment]: # (!!!)

## Importanza dell’elettricità 1/2

- E' importante l'ettricità?

![Blackout](media/blackout.png)

Note:
- Avete già avuto un black out a casa? Come vi siete sentiti ?
- Chiedere a cosa serve l'elettricità?
- Acqua potabile (pompe), Forno elettrico, luce, conservazione del cibo

[comment]: # (!!! data-auto-animate)

## Importanza dell’elettricità 2/2

- "Motore" della società moderna

Note:
- Menzionare idrocarburi come secondo "motore"

---

E' sempre stato così?
Perché è così comoda?

Note:
- Cosa usavamo prima ? carbone, legna.
- Non inquina ed è facile da trasportare

[comment]: # (!!! data-auto-animate)

## Elettricità nel mondo 1/2

- Elettricità nel mondo - tanta o poca?

---
![Domanda](media/iea-electricity.png)

3000 TWh = 3.000.000.000.000.000 Watt-ora

Ce ne vorrà di più in futuro ?

Note:
- Il Watt-ora è un'unità di misura dell'energia (J) 
- Un calorifero di 500 W per 2 ore quanto consuma ?
- 3000 TW sono circa 685 millioni di caloriferi di 500 W accessi per un anno

[comment]: # (!!! data-auto-animate)
## Elettricità nel mondo 2/2

- Elettrificazione come motore della riduzione CO2
- Elettricità si trasporta e si consuma senza inquinamento
- La sua produzione spesso inquina - conoscete fonti di energia?
- Avete già visti serbatoi di elettricità ?

Note:
- Esempio delle automobili
- Graduale sostituzione fossili con altre forme di energia e elettricità
- Chiedere se l'hanno mai vista?

[comment]: # (!!! data-auto-animate)

## L'elettricità visibile 1/2

- In natura?...

---

![Fulmine](media/lightning.jpg) <!-- .element: style="height:400px; max-width:200vw; image-rendering: crisp-edges;" -->

Scarica di elettricità fra la nuvola e il suolo

Note:
- Elettricità "scorre" come un fluido
- C'è l'elettricità anche negli esseri viventi (impulsi nervosi)

[comment]: # (!!! data-auto-animate)

## L'elettricità visibile 2/2

![Cat](media/cat.jpg)

Cosa è successo in questa immagine ?
Cosa trattiene il polistirolo al gatto ?

Note:
- "ELETTRICITA' STATICA" è la parola
- Dato che non si vede spesso, si sono voluti due milleni per iniziare a capirla. Noi abbiamo 4 ore

[comment]: # (!!!)

## Esperimento con palloni 1/3

Ci sono dei palloni "non strisciati" disponibili

A gruppi di due bambini (non umidi):
- uno strofina il pallone sulla propria maglietta 
- avvicina il pallone alla testa dell'altro bambino

*Domanda scientifica*
- Tutti i palloni fanno la stessa cosa ai cappelli ?

Che rapporto con il gatto di prima ?

Note:
- Prerequisito fondamentale bambini con vestiti secchi
- Magari prendere lana/mettere in asciugatrice panni per la lezione

[comment]: # (!!!)
## Esperimento con palloni 2/4

- [Spiegazione](https://phet.colorado.edu/sims/html/balloons-and-static-electricity/latest/balloons-and-static-electricity_en.html)
- Il movimento "carica" positivamente il pallone e "negativamente" la maglietta
- E' cambiato il numero di cariche + e - ?


Note:
- Attraverso l'animazione spiegare conservazione cariche
- Fare dire che le dariche diverse si attragono
- Come i poli magnetici

[comment]: # (!!!)
## Esperimento con palloni 3/4

- Cosa succede se avvicino due palloni "strisciati" sospesi con un filo ?

Note:
- Spiegazione cariche uguali che si rispingono
- Legge di Coulomb

[comment]: # (!!!)
## Esperimento con palloni 4/4

Proviamo con una materia non carica

- Pallone con pezzi di carta
- Vengono lo stesso attrati

Note:
- Induzione elettrostatica
- https://www.stem.org.uk/resources/elibrary/resource/27020/electric-sausage

[comment]: # (!!!)

### Definizione elettricità

- Il nome provviene dalla parola greca per l'ambra gialla in Greco

![Ambra](media/ambra.jpg)

- Ricordate l'atomo ? Com'è fatto ?

Note:
- Primo studioso dell'ettricità Talete (600 a.C) - lo stesso del teorema
- 
---

### Definizione elettricità 1/4

![Corso Dott. Carlini](media/atomo-corso-carlini.jpg) <!-- .element: style="height:350px; image-rendering: crisp-edges;" -->

Quali parti sono cariche elettricamente in questa immagine?

Note:
- Importante sottolineare che tutta la materia è fatta da atomi
- Ci sono particelle cariche in ogni atomo
- Le cariche elettriche sono dapertutto, non solo nell'elettricità

[comment]: # (!!! data-auto-animate)

### Definizione elettricità 2/4

Dobbiamo fare un po' di storia

- "Fluido elettrico" di Benjamin Franklin (1757)
- Capì che esistevano cariche diverse (+ e -)
- Decise che la corrente va dal + al -

---

- Benjamin Frankin è famoso per l'invenzione del parafulmine

![Esperimento con il figlio](media/franklin.jpg)

[comment]: # (!!! data-auto-animate)

![Esperimento con il figlio](media/franklin.jpg)

_Non è famoso per rispettare la sicurezza dei bambini_

[comment]: # (!!! data-auto-animate)

### Definizione elettricità 3/4

Tutti pensavano allora che l'elettricità fosse una specie di liquido invisible

- Scoperta dell'elettrone grazie ai "raggi catodici" (Thomson, 1897)

<iframe width="560" height="315" src="https://www.youtube.com/embed/8Q5QuXh2XH0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

---

Allora si capì che l'elettricità erano delle cariche in movimento

![Movimento cariche](media/current-flow.gif)

Note:
- Perché non si muovono i protoni invece? 10.000 volte più pesanti degli elettroni.
- Perché si muovono ? Perché c'è una differenza di potenziale abbastanza forte.

[comment]: # (!!! data-auto-animate)

### Definizione elettricità 4/4

*Elettricità = cariche in movimento*

Ma come si muovono ?

- Senso convenzionale della corrente in un circuito (Franklin)

<iframe src="media/conventional-current.mp4" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


Note:
- Si userà la convenzione usuale nel corso (dal + al -)
- Domande di verifica: cariche positive/negative, atomo

[comment]: # (!!! data-auto-animate)
### Come si muovono le cariche

![Illustrazione](media/rope.png) <!-- .element: style="height:350px; image-rendering: crisp-edges;" -->

1. Tutti i bambini tengono la corda senza stringerla - "fili"
2. Un bambino stringe leggermente la corda - "resistenza"
3. Il prof fa scorrere la corda fra le sue mani - "pila"
4. Com'è il movimento della corda? Che succede alla resistenza? 

Note:
- *Le cariche non vengono dalla pila*
- Conservazione della carica <-> conservazione della corda che entra/esce, non si "consuma" la carica
- Movimento delle cariche simultaneo della corda
- Analogia della resistenza che scalda la mano ma non degli altri
- E' solo un'analogia della corrente, non è perfetto (ad es. la tensione è problematica)

[comment]: # (!!!)

### Conduttori e isolanti

- Teoria: Facilità a strappare elettroni
- Le materie diverse ma... sono gli stessi elettroni
- Alcuni "conducono bene" -> "conduttori"
- Altri "non conducono bene" -> "isolanti"
- Verifichiamo se è possibile riconoscerli

Note:
- Strappare elettroni = resistenza = quant'era stretta la corda
- Chi conduce bene l'elettricità? Metalli
- I buoni conduttori hanno elettroni liberi di spostarsi
- E come chiamiamo quelli che se "tiriamo" abbastanza conducono, altrimenti no? Semi conduttori

---
### Misura dell'elettricità

Proviamo i materiali seguenti

| Materiale | BEEP o NO? |
| -- | -- |
| Carta | ??? |
| Alluminio | ??? |
| Filo | ??? |
| Plastica | ??? |
| Acqua | ??? |
| Acqua salata | ??? |


[comment]: # (!!!)

### Misura dell’elettricità

Abbiamo parlato in termini un po' generali

Tante unità diverse per l'elettricità
- L'unità di Alessandro Volta (inventore della pila)
- L'unità di André-Marie Ampère 
- L'unità di Georg Ohm
- e molte altre (Watt, Farad, Henry, Coulomb)...

Note:
- A cosa servono le unità ?
- Perché un scienzato deve creare delle unità ? 
---

In questo corso vedremo le 3 unità più importanti

Secondo voi chi se l'è passata meglio fra i tre?

(Volta divenne senatore e ebbe la sua villa a Como)

(Ampère ha il suo nome inciso nella Torre Eiffel)

(Ohm non fu creduto e rinunciò al posto in università)

[comment]: # (!!!)

### Misura dell’elettricità

Ricordiamo 3 grandezze

| Grandezza (Abbr.) | Unità | Simbolo | Spiegazione |
| -- | -- | -- | -- |
| *Corrente* (I) | Ampère | A | Flusso delle cariche elettriche |
| *Tensione* (U o V) | Volt   | V | Potenziale delle cariche elettriche |
| *Resistenza* (R) | Ohm | Ω | "Freno" alle cariche elettriche |
 
Note:
- La corda evita l'errore di pensare che le cariche vengono dalle batterie, sono già presenti
- Potenziale -> quello che spinge le cariche a muoversi, come la gravità che fa cadere le cose.

[comment]: # (!!!)
### Il multimetro

<img src="media/multimetro.jpg" width="350px" alt="Multimetro" />

Com'è fatto? Come si accende ?
Riconoscete delle unità ?
Colori dei fili ?

[comment]: # (!!!)
### Esperimento

- Misurare tensione di una pila (generatore di tensione)
- Domanda aperta : cosa succede se metto due pile in serie? In parallelo?
- Ipotesi di classe 
- Esperimenti a gruppo e raccolta delle misure

---

### Conclusioni esperimento

Generatori di tensioni in serie producono una tensione = somma. 

| Configurazione | Valore misurato | Conclusione |
| -- | -- | -- |
| Pile una dopo l'altra (serie) | ??? | ??? |
| Pile di fianco (//) | ??? | ??? |

---

Abbiamo scoperto una legge dell'elettricità

- Generatori di tensione uguali in serie = la tensione si somma
- Generatori di tensione uguali in parallelo = la tensione rimane la stessa

[comment]: # (!!!)

### Effetti dell’elettricità (slide finale)
- Produce calore, luce (lampadine)
- Movimento (motori)
- Rischi (pericolo tensioni sul corpo umano)

[comment]: # (!!!)

## Fonti usate in questa presentazione

<small>
- STEM

- Python

- AISTAP Chimica Dott. Carlini

- Sparkfun Creative commons https://learn.sparkfun.com/tutorials/what-is-electricity/all

- Images "Ka-boom (lightning)" by Leszek.Leszczynski is licensed under CC BY 2.0.

- Others : IEA, Global electricity demand by region in the Stated Policies Scenario, 2000-2040, IEA, Paris https://www.iea.org/data-and-statistics/charts/global-electricity-demand-by-region-in-the-stated-policies-scenario-2000-2040, IEA. Licence: CC BY 4.0
</small>