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

Benvenuti

Note:
- Disporre i ragazzi a gruppi

[comment]: # (!!!)

## Elettronica con Micropython
![Micropython logo](media/micropython-logo.svg) <!-- .element: style="height:250px; max-width:200vw; image-rendering: crisp-edges;" -->

Pascal Brunot | AISTAP | Luglio 2023

Lezione 1 : Elettricità


Note:
- Capire il concetto di carica (con elettricità statica)
- L'elettricità come un flusso di cariche
- Distinguere conduttori e isolanti
- Necessità di un circuito chiuso per il flusso (corda)
- Definizioni e unità di corrente, tensione, resistenza
- Approccio scientifico (ipotesi, esperimento, risultati, conclusioni)
- Imparare a fare misura di tensione con il multimetro

[comment]: # (!!! data-background-color="aqua")

## Introduzione

Perché queste due parole assieme ? Cosa possono fare ?

<iframe width="560" height="315" src="https://www.youtube.com/embed/aXW4dqvjFx0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

[comment]: # (!!!)
## Introduzione

1. Per programmare questi robot ci vuole ... Micropython
2. Per capire i componenti elettronica ci vuole... un po' di fisica
3. Inizieremo a capire l'elettricità nelle prossime lezioni


Note:
- Chiarire che non costruiremo un robot ma qualcos'altro

[comment]: # (!!!)

## Regole del corso

1. Si alza la mano per prendere la parola, a qualunque momento
2. Si ascoltano le domande degli altri
3. Non c'è una gara, non c'è un voto
4. Condividete il materiale che avete a disposizione


Note:
- Chiarire che non costruiremo un robot ma qualcos'altro

[comment]: # (!!!)


## Lezione 1

Elettricità

![Electricity](media/spark.jpg)

Note:
- Oggi sarà la lezione più teorica di tutte perché dobbiamo imparare i concetti ma ci divertiremo anche facendo esperimenti
- Materiali richiesti: palloni, pezzi di carta tagliati, piatto, corda 5-10m un po spessa
- Pile elettriche 1.5 V (2 a ragazzi), fili, alluminio, scotch
- Acqua / Acqua salata, monetine, ferro
- Alcuni multimetri

[comment]: # (!!!)

## Elettricità a casa

E' importante l'ettricità oggi ?

Vediamo senza

![Blackout](media/blackout.png)

Note:
- Avete già avuto un black out a casa? Come vi siete sentiti ?
- Chiedere a cosa serve l'elettricità?
- Acqua potabile (pompe), Forno elettrico, luce, conservazione del cibo

[comment]: # (!!!)

## Elettricità nella società

"Motore" della società moderna

_E per gli esseri viventi ?_

Note:
- Avere più energia a disposizione ha consentito alla popolazione umana di vivere in grandi città
- Menzionare idrocarburi come secondo "motore"
- Nervi
- Sapete come è stato scoperto ? Scienfico italiano, Galvani e le rane (1781)

[comment]: # (!!!)

## E prima ?

E' sempre stato così importante nella nostra vita?

Note:
- Cosa usavamo prima ? carbone, legna, animali

[comment]: # (!!! data-auto-animate)

## Animali, legna, carbone

E' sempre stato così importante nella nostra vita?

![Agricoltura](media/agricoltura.jpg)

Note:
- Adesso cosa si usa al posto degli animali ?
- Siamo diventati meno contadini e più urbani in poche decenni

[comment]: # (!!!)

## Vantaggi

_Ma perché è così comoda l'elettricità?_

_Da dove proviene l'elettricità che abbiamo in casa ?_

Note:
- Non inquina ed è facile da trasportare
- "Vettore energetico"
- Centrali elettriche (idroelettriche, termiche gas/carbone, eolico, solare, ...)
- La generazione può essere pulita spesso non lo è

[comment]: # (!!!)

## Quanta elettricità ?

- Elettricità nel mondo - tanta o poca?

---
![Domanda](media/iea-electricity.png)

3000 TWh = 3.000.000.000.000.000 Watt-ora

Ce ne vorrà di più in futuro ?

Note:
- Prima unità di misura, James Watt (1776 - macchina a vapore efficiente)
- Un asciugacapelli di 2000 W accesso un'ora quanto consuma?
- Accesso due ore? (1 anno=17.5MWh)
- 3000 TWh sono 171 millioni di acciugacappelli accessi in permanenza

[comment]: # (!!! data-auto-animate)

## Come la usiamo?

Elettrificazione come motore della riduzione CO2

![London Fog, 1952](media/london-fog.jpg)

Note:
- Dicembre 1952, 4000 morti, 100000 malati per via dello smog (carbone)
- Esempio delle macchine elettriche vs. a combustione
- Graduale sostituzione fossili con altre forme di energia e elettricità
- La combustione dei carburanti fossili producono CO2 nell'atmosfera che assorbe il calore (infrarossi) emesso dal suolo
- 2400 GT dalla fine della seconda guerra mondiale... ne possiamo emettere 1200 GT max per stare <2.5°C

[comment]: # (!!! data-auto-animate)

## Elettricità nel mondo 3/3

Elettronica sempra più potente e presente

![Datacenter](media/datacenter.jpg)

Note:
- Chiedere se l'hanno mai vista l'elettricità ?
- E' ora di guardarci da vicino

[comment]: # (!!! data-auto-animate)

## L'elettricità visibile 1/2

- In natura?...

---

![Fulmine](media/lightning.jpg) <!-- .element: style="height:400px; max-width:200vw; image-rendering: crisp-edges;" -->

Scarica di elettricità fra la nuvola e il suolo

Note:
- Elettricità "scorre" come un fluido
- C'è l'elettricità anche negli esseri viventi (impulsi nervosi, Galvani)

[comment]: # (!!! data-auto-animate)

## L'elettricità visibile 2/2

![Cat](media/cat.jpg)

Cosa è successo in questa immagine ?

Cosa trattiene il polistirolo al gatto ?

Note:
- "ELETTRICITA' STATICA" è la parola
- Dato che non si vede spesso, si sono voluti due milleni per iniziare a capirla. Noi abbiamo 5 lezioni

[comment]: # (!!!)

## Esperimento con palloni

&#x1F6B8; A gruppi di due bambini, uno strofina il pallone sulla maglietta dell'altro

&#x1F6B8; Sentite qualcosa ?

&#x1F6B8; Cosa succede ai vostri cappelli quando avvicinate il pallone ?

&#x1F6B8; Cosa succede quando avvicinate due palloni ?

&#x1F6B8; Potete scaricare un pallone ?

---
## Esperimento con palloni

[Spiegazione](https://phet.colorado.edu/sims/html/balloons-and-static-electricity/latest/balloons-and-static-electricity_en.html)

Il movimento "carica" positivamente il pallone e "negativamente" la maglietta

Le cariche uguali si rispongono, le cariche opposte si attragono

Note:
- Spiegazione cariche 
- Dove sono le cariche ? Alla superficie del pallone
- Forza elettrostatica (Legge di Coulomb)

[comment]: # (!!!)

### Definizione elettricità

Il nome provviene dalla parola greca per l'*ambra gialla* in Greco

![Ambra](media/ambra.jpg)

Ricordate l'atomo ? Com'è fatto ?

Note:
- Primo studioso dell'ettricità Talete (600 a.C) - lo stesso del teorema
- Avevano visto che come il pallone l'ambra strofinata attraeva piccoli oggetti

[comment]: # (!!!)

### Definizione elettricità

![Corso Dott. Carlini](media/atomo-corso-carlini.jpg) <!-- .element: style="height:250px; max-width:200vw; image-rendering: crisp-edges;" -->

Quali parti sono cariche elettricamente in questa immagine?

Note:
- Importante sottolineare che tutta la materia è fatta da atomi
- Ci sono particelle cariche in ogni atomo
- Le cariche elettriche sono dapertutto, non solo nell'elettricità

[comment]: # (!!! data-auto-animate)

## Induzione elettrostatica

Pallone con pezzi di carta. La carta è carica ?

![Pallone](media/dalle-balloon.png)

Note:
- Induzione elettrostatica
- Cosa è successo ?
- https://www.stem.org.uk/resources/elibrary/resource/27020/electric-sausage

[comment]: # (!!!)

## Induzione elettrostatica

La presenze di cariche nel pallone ha allontanato gli elettroni nella carta

Così, la carta si è caricata positivamente da un lato, e negativamente dall'altro

Ma perché è stata attrata ? Dopotutto, l'altra parte era respinta...

[Simulatore](https://javalab.org/en/electrostatic_induction_metal_bonding_en/)

Note:
- La parte carica positivamente è più vicina alle cariche negative
- La forza dipende dalla distanza (dal quadrato in realtà, come la gravità)
- La forza attrattiva è quindi maggiore rispetto alla forza repulsiva e la carta vola
- L'obiettivo di questa dimostrazione è di mostrare che le cariche sono presenti dapertutto, non solo in oggetti positivamente/negativamente carichi

[comment]: # (!!!)

## Quizz

![Bambino](media/domanda%20di%20verifica.jpg)

_perché questo bambino ha i cappelli rizzati ?_

Note:
- Strisciando sullo scivolo si sono spostate delle cariche fra bambino e scivolo (come il movimento per caricare il pallone)
- Il risultato è che, come il pallone, il bambino ha una carica elettrica sul suo corpo (e lo scivolo ha la carica esattamente opposta)
- Le cariche uguali si rispongono e i capelli vogliono stare più lontano possibili gli uni dagli altri
- Se i cappelli sono bagnati non funziona, perché l'acqua è un conduttore

[comment]: # (!!!)

### Il fluido elettrico (1757)

Dobbiamo fare un po' di storia con Benjamin Franklin

Capì lui che esistono solo cariche positive e negative

Capì lui che le cariche non si creano, si spostano soltanto

Decise lui che la corrente va dal + al -

Note:
- Franklin è anche famoso per essere un padre fondatore degli Stati Uniti d'America, un musicista, uno scacchista, un impreditore, un giornalista
- Prima di lui si pensava che le cariche erano diverse da materiale a materiale (cariche dallo scivolo, del capello, ...)

---

Benjamin Frankin è famoso per l'invenzione del parafulmine (1752)

![Esperimento con il figlio](media/franklin.jpg)

Note:
- Nel quadro sopra, Franklin voleva dimostrare che le nuvole sono cariche (come i nostri palloni)
- Filo elettrico avvolto attorno al filo dell'acquilone, terminava con una chiave
- Riuscì a osservare scariche elettriche all'estremità della chiave al riparo del portico di casa

[comment]: # (!!! data-auto-animate)

![Esperimento con il figlio](media/franklin.jpg)

_Non è famoso per rispettare la sicurezza dei bambini_

Note:
- Se il fulmine avesse colpito il loro acquilone loro sarebbero stati uccisi
- Parafulmine faceva paura alle popolazioni, attraeva la colera di Dio 
- Si sarebbero evitati 3000 morti a Brescia quando un fulmine colpì la polveriera nel 1769

[comment]: # (!!! data-auto-animate)

### Definizione elettricità 2/3

Tutti pensavano allora che l'elettricità fosse una specie di liquido invisible

Scoperta dell'elettrone grazie ai "raggi catodici" (Thomson, 1897)

<iframe width="560" height="315" src="https://www.youtube.com/embed/8Q5QuXh2XH0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Note:
- Il passaggio degli elettroni fa emettere luce verde al fosforo
- Si vede anche che sono sensibili al magnete, lo vedremo nella seconda lezione

---

Allora si capì che l'elettricità erano delle cariche in movimento!

![Movimento cariche](media/current-flow.gif)

Note:
- Perché non si muovono i protoni invece? 10.000 volte più pesanti degli elettroni.

[comment]: # (!!! data-auto-animate)

### Definizione elettricità 3/3

Un movimento in quale direzione ? 

Franklin decise il senso convenzionale della corrente in un circuito 

<iframe src="media/conventional-current.mp4" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Note:
- Si userà la convenzione usuale nel corso
- Franklin visse un secolo prima di Thomson... non poteva sapere degli elettroni
- Domande di verifica: cariche positive/negative, atomo

[comment]: # (!!!)

## Come circola la corrente elettrica?

&#x1F6B8; La corda

1. Un gruppo di ragazzi tengono la corda senza stringerla
2. Uno stringe leggermente la corda
3. L'insegnante inizia a fare scorrere la corda fra le sue mani
4. Aggiungiamo un ragazzo che stringe al massimo

![Corda](media/rope.jpg)

Note:
- E' solo un'analogia della corrente, non è perfetto (ad es. la tensione è problematica, si potrebbe approssimare con altezza della corda...)
- Conservazione della carica <-> conservazione della corda che entra/esce, non si "consuma" la carica
- Movimento delle cariche simultaneo della corda (non si muove prima da una parte)
- La corrente è la stessa in tutto il circuito (la corda non circola più veloce da una parta rispetto all'altra)
- Analogia della resistenza che scalda la mano ma non degli altri
- La corda evita l'errore di pensare che le cariche vengono dalle batterie, sono già presenti

[comment]: # (!!!)

### Conduttori e isolanti #1

Tutti i materiali fanno passare le cariche?

![Corrente](media/corrente.jpg)

&#x1F6B8; Prova con tester di continuità + vari materiali

Note:
- Chi conduce bene l'elettricità? Metalli
- I buoni conduttori hanno elettroni liberi di spostarsi
- I ragazzi portanno i materiali da testare all'istruttore con il tester

[comment]: # (!!!)

### Conduttori e isolanti #2

Usiamo un simulatore per vedere:

[JavaLab](https://javalab.org/en/electric_current_en/)

- Alcuni atomi "si tengono stetti" i loro elettroni (isolanti)
- Altri li possono prestare (conduttori)

[comment]: # (!!!)

### Misura dell’elettricità

Tante unità diverse per l'elettricità
- L'unità di Alessandro Volta (inventore della pila)
- L'unità di André-Marie Ampère 
- L'unità di Georg Ohm
e molte altre (Watt, Farad, Henry, Coulomb) che non useremo...

Note:
- Vediamo questi tre scienzati da dove venivano
- Volta, Italia. Ampère, Francia. Ohm, Germania.
- Pila elettrica 1745. Legge di Ohm 1826.
---

Secondo voi chi se l'è passata meglio fra i tre scienzati ?

[comment]: # (!!! data-auto-animate)
Volta divenne senatore e ebbe la sua villa a Como

![Volta](media/volta.jpg)

[comment]: # (!!! data-auto-animate)
Ampère ha il suo nome inciso nella Torre Eiffel

![Ampère](media/ampere.jpg)

[comment]: # (!!! data-auto-animate)
Ohm non fu creduto e rinunciò al posto in università

![Ohm](media/ohm.jpg)

[comment]: # (!!!)

### Misura dell’elettricità

Ricordiamo 3 grandezze

| Grandezza (Abbr.) | Unità | Simbolo | Spiegazione |
| -- | -- | -- | -- |
| *Corrente* (I) | Ampere | A | Flusso delle cariche elettriche |
| *Tensione* (U o V) | Volt   | V | Potenziale delle cariche elettriche |
| *Resistenza* (R) | Ohm | Ω | "Freno" alle cariche elettriche |
 
Note:
- Tensione come differenza di altitudine che fa scorrere l'acqua del fiume
- I simboli delle unità che provvengono da un personaggio storico sono in maiuscole (A non a)
- Non si usano gli accenti nelle unità (Ampère->Ampere)
- Alle unità si possono aggiungere i soliti prefissi come per le lunghezze (milli-m, chilo-k, mega-M)
- Domande : che corrente fa 100 mA + 1 A in A ?
- Domande : che tensione c'è fra 1 kV - 500 V in V ?

[comment]: # (!!!)

### Il multimetro

<img src="media/multimetro.jpg" width="200px" alt="Multimetro" />

Com'è fatto? Come si accende ? Colori dei fili ?

Note:
- Per misurare le tre unità di prima si può usare il MULTIMETRO
- Come si misura una tensione ? Simbolo V DC
- La tensione si misura fra due punti del circuito
- La tensione si misura "IN PARALLELO" ai due punti
- Accendete e mettelo su misura di tensione

[comment]: # (!!!)

### Esperimento

&#x1F6B8; Misurare tensioni

- Misurare tensione di una pila
- Di due pile attaccate
- Disposte in modo diverso

[TinkerCad](https://www.tinkercad.com/things/kFyHZJa3gyv)

- Ipotesi di classe : cambierà qualcosa?

Note:
- Far votare i bambini a mano alta

[comment]: # (!!!)

### Risultati esperimento

&#x1F6B8; Risultati

| Configurazione | Valore misurato | Conclusione |
| -- | -- | -- |
| 1 Pila | ??? | ??? |
| Pile una dopo l'altra (serie) | ??? | ??? |
| Pile connesse in parallelo (//) | ??? | ??? |
| Pile che non si toccano | ??? | ??? |
| Portabatterie | ??? | ??? |

Note:
- Obiettivo è che tutti i bambini sappiano misurare una tensione
- Raccolta valori
- Generatori di tensione in serie si sommano
- In parallelo, non si sommano (quando hanno la stessa tensione)

[comment]: # (!!!)

### Rappresentazione schematica

Le "pile" sono un tipo di "generatore di tensione"

![Generatori](media/generatori.jpg)

Esistono due simboli per questi concetti

![Simbolo](media/voltage_source.png)

Note:
- A cosa servono i simboli ? A disegnare schemi elettrici più complessi
- A trasmettere in modo preciso le informazioni (rispetto ad una lettera)

[comment]: # (!!!)

### Effetti dell’elettricità

<div class="twocolumn">
<div>

Produce calore, luce (lampadine)

Movimento (motori)

&#9888; Ma è molto pericolosa &#9888;

</div>
<div>

![Pericoli](media/pericoli.png)

</div>
</div>

Note:
- Ricordare contrazione muscolari (Galvani e le rane)
- Insistere che non si gioca con l'elettricità 
- In questo corso useremo tensioni <= 5V e correnti limitate continue
- Il grafico è valido per tensioni attorno a 200 V
- La corrente alternata è più pericolosa della corrente continua

[comment]: # (!!!)

### Riassunto finale

Elettricità
: cariche in movimento

![Movimento cariche](media/current-flow.gif)

Conduttori e isolanti

Unità di misura
- Ampere per il flusso di cariche
- Volt per il potenziale elettrico
- Ohm per la resistenza al flusso di cariche

Note:
- se c'è tempo elettrolisi acqua salata


[comment]: # (!!!)

### Prossima lezione

Chi deve installare Thonny e il driver sul proprio computer?

Note:
- Verificare che siano tutti più o meno pronti con Thonny per la prossima lezione
- Per la lezione 2 non serve la connessione alla board

[comment]: # (!!!)
## Elettronica con Micropython
![Micropython logo](media/micropython-logo.svg) <!-- .element: style="height:250px; max-width:200vw; image-rendering: crisp-edges;" -->

Pascal Brunot | AISTAP | Luglio 2023

http://aistap-micropython.pages.dev/

Lezione 2 : Motori, Resistenze e Python

Note:
- Obiettivi della lezione
- Collegamento elettricità - magnetismo
- Motore DC
- Approccio scientifico (osservazione-ipotesi-esperimento-conclusioni)
- Legge di Ohm
- Misurare resistenze
- Resistenze in parallelo e in serie

[comment]: # (!!! data-background-color="aqua")

## Riassunto ultima lezione 1 / 2

Corrente elettrica = *movimento di cariche elettriche*

![Movimento cariche](media/current-flow.gif)


Note:
- Abbiamo visto che l'elettricità è fondamentale nel mondo
- Abbiamo fatto circolare la corda fra le mani come l'elettricità nei conduttori
- Esistono conduttori e isolanti
- Abbiamo conosciuto alcuni scienzati famosi che hanno dato il loro nome a certe unità

[comment]: # (!!!)

## Riassunto ultima lezione 2/2

*Unità di misura*

| Grandezza (Abbr.) | Unità | Simbolo | Spiegazione |
| -- | -- | -- | -- |
| *Corrente* (I) | Ampere | A | Flusso delle cariche elettriche |
| *Tensione* (U o V) | Volt   | V | Differenza di potenziale |
| *Resistenza* (R) | Ohm | Ω | "Freno" alle cariche elettriche |

[comment]: # (!!!)

## La tensione

La tensione in Volt fra 2 punti è definita la differenza di potenziale elettrico fra i due punti

![Differenza](media/tensione.png)

Mette in moto le cariche elettriche (flusso)

[comment]: # (!!!)

## Riassunto ultima lezione

Abbiamo usato alcuni componenti elettrici

- Pile (generatori di tensione)
- Fili
- Multimetro (Voltmetro)

[comment]: # (!!!)

## Magneti

![Magnete](media/magnete.jpg)

Cosa vedete su questa immagine ?
- Che cosa osservate ?

Note:
- Cosa hanno i magneti ? (poli N e poli S)
- C'è però una differenza fondamentale con l'elettricità - non esistono monopoli magnetici
- Abbiamo visto invece che esistono cariche elettriche isolate (palloni)

[comment]: # (!!!)

### La scoperta di Ørsted

Bussola e corrente elettrica (1820)

<iframe width="560" height="315" src="https://www.youtube.com/embed/h5N2grjG8d8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Magnetismo e elettricità sono legati

Si parla spesso di "elettromagnetismo"

Note:
- Orsted era convinto che le forze della natura erano unite fra di loro, e provò per 13 anni a scoprire il collegamento fra elettricità e magnetismo.
- L'elettricità era già nota e studiata da un secolo prima che si notasse questo effetto
- Grazie a lui Maxwell nel 1864 scrisse le leggi che unificano elettricità e magnetismo
- Vedremo come fare qualcosa di utile con tutti i due

[comment]: # (!!!)

### Hans Christian Ørsted

![Orsted](media/orsted.png)

_secondo voi per lui com'è andata la vita?_

Note:
- Dopo l'elettromagnetismo è stato il primo chimico a produrre alluminio
- Scrisse poesia
- Il suo nome è stato dato ad un asteroide

[comment]: # (!!!)

[comment]: # (!!!)

### Resistenze 1/3

Ogni componente elettrico ha un simbolo

Ecco la resistenza

![Resistenza](media/resistor%20symbol.png)

Note:
- Fanno "resistenza" - Rallentano il flusso delle cariche
- Ciò facendo prendono si riscaldano prendendo l'energia 
- Cosa succedeva alla mano che stringeva la corda? si riscaldava
- Si riscaldono le resistenze? Resistenza del forno, della lavatrice...

---

Resistenza del forno

![Forno](media/forno.png)

Note:
- Attenzione che la RESISTENZA ELETTRICA c'è dapertutto (salvo superconduttori)
- Potremmo dire che un conduttore ha una resistenza ... (bassa)
- E un isolante ha una resistenza ... (alta)

---

Resistenze usate in elettronica

![Resistors](media/resistors.png)

Note:
- Commentare resistenze che hanno i ragazzi
- Resistenze che variano con la temperature (termistori)
- Resistenze aggiustabili con un bottone (potenziometri, reostati)
- Piccole resistenze saldate in superficie
- Noi useremo le resistenze a film di carbone per montaggio con foro passante
- Menzionare che esiste un codice di colore sulle resistenze per capirne il valore

[comment]: # (!!!)

### Misura delle resistenze con il multimetro

Le resistenze si misurano con il multimetro in posizione Ω

![Misura](media/misura_resistenza.jpg)

Note:
- Come le tensioni le resistenze di misurano fra due punti del circuito con il multimetro in parallelo

[comment]: # (!!!)

### Breadboard 1/2

_Breadboard_ = scheda di connessione senza fili

Servono a creare circuiti semplici

Le righe verticali servono per collegare le alimentazioni (pile)

Le righe orizzontali servono per collegare i componenti 

![Breadboard](media/breadboard.jpg)

Note:
- I fori di una riga della breadboard sono internamente collegati fra loro mediante una barretta metallica
- non si deve forzare l'inserimento nei fori delle zampe dei componenti 
- non si devono inserire nei fori conduttori con le estremità piegate, ma occorre raddrizzarle prima servendosi di una pinza
- i fili devono passare attorno, non sopra i componenti

[comment]: # (!!!)

### Python

![Micropython logo](media/micropython-logo.svg)

Note:
- Chi ha già scritto programmi ?
- Chi ha già fatto un corso di Python ?
- Conoscete altri linguaggi di programmazione ?

[comment]: # (!!! data-background-color="aqua")

### Python

Lanciare Thonny

![Python](media/python%20execution.png)

---

REPL = _Read, Print, Eval, Loop_

![Thonny](media/thonny-python.png)

Esegue subito un commando

---

&#x1F6B8; Nel REPL scrivete le istruzioni dopo >>> e fate INVIO

```python [1|2|3|4]
>>> 1+1
2
>>> 3*10**15
3000000000000000
```

Python è un ottimo calcolatore

---

Adesso passiamo alla parte programma

```python
print("Sono un programma in Python")
```

&#x1F6B8; Clic sul triangolo bianco nel cerchio verde

Note:
- Aspettare che tutti abbiano eseguito il programma

---

&#x1F6B8; Ripasso variabili, funzioni

```python [1-2]
nome = input("Come ti chiami ?")
print ("Ciao " + nome)
```

Note:
- Verificare che tutti abbiano scritto il programma
- Domanda cos'è una variabile ? Scatola (nome, tipo, valore)

---

Funzioni utili

```python
print("testo") # stampa nella console il testo indicato
type(variabile) # mostra il tipo della variabile
str() # trasforma in stringa di testo
int() # trasforma in interno
range(a,b) # l'intervallo fra a (incluso) e b (non incluso)
```

Parole chiavi def, for, while

```python
def funzione(parametro1):  # definisce una funzione di un parametro
    return valore          # ritorna il valore della funzione

for x in ...        # Per ogni x in ...
while condizione:   # Fin quando è vera condizione, ....
```

Note:
- Valutare cheatsheet per sintassi Python

[comment]: # (!!!)

### Pausa Python 2/4

&#x1F6B8; Facciamo la formula delle resistenze in serie

$$ R_{serie} = R_{1} + R_{2} $$

```python [1-2|3-4]
def serie(r1, r2):
    return r1 + r2

print(serie(100, 100))
```

[comment]: # (!!!)

### Pausa Python 3/4

&#x1F6B8; Facciamo la formula delle resistenze in parallelo

$$ R_{parallelo} = \frac{R_{1} \times R_{2}}{R_{1} + R_{2}} $$

```python [1-2|3-4]
def parallelo(r1, r2):
    return (r1 * r2)/(r1 + r2)

print(parallelo(100, 100))
```

&#x1F6B8; Verificate se ritrovate il valore misurato in parallelo

Note:
- Risultato atteso 100//200= 66.66 Ω
- Con due resistenze in parallelo la resistenza equivalente è sempre *più piccola* di entrambe resistenze

[comment]: # (!!!)

### Legge di Ohm 1/2

Le cariche elettriche che passano attraverso una resistenza seguono la *legge di Ohm*

$$ U = R \times I $$

Tensione = Corrente x Resistenza

Note:
- Spiegare il concetto di legge fisica ? 
- Sarà l'unica formula che vedremo durante il corso ma è la più importante
- Si possono manipolare i termini dell'equazione U/R=I, I=U/R

[comment]: # (!!!)

### Legge di Ohm 2/2

Un triangolo per ricordare la legge di Ohm

![VRI](media/ohm-law.jpg)

_V era il simbolo della tensione, come U, ricordate?_

[comment]: # (!!!)

### Pausa Python 3/3

&#x1F6B8; Adesso facciamo la legge di Ohm in Python

$$ U = R . I $$

```python [1-2|3-4]
def ohm_u(r, i):
    return r * i

print(ohm_u(200, 0.1))
```

&#x1F6B8; Risultato con R=200 Ω, I=0.1A ?

Note:
- Risultato 20 V
- Esercizi extra possibili

[comment]: # (!!!)

### Altri componenti : interruttore

![Interrutore luce](media/interruttore.png)

Simbolo

![Interrutore simbolo](media/interruttore-simbolo.jpg)

A cosa serve?

Note:
- Imparare i simboli è come riconoscere i mattoncini di Lego
- Poi si assemblano i componenti per fare circuiti più o meno complessi

[comment]: # (!!!)

### Altri componenti : Condensatori

Condensatori, sono "serbatoio di tensione"

![Condensatori](media/condensatori%20foto.png)

Abbreviazione (C), Simbolo, Unità (F)

![Condensatori](media/capacit%C3%A0.jpg)

Note:
- Usano un campo elettrico per immaganizzare energia, scoperti nel 1745
- Si misurano in Farad ma è un'unità enorme, si usa di solito il micro-farad o addirittura il pico-farad (10^-12)
- Il nome arriva dall'inglese Michael Faraday. E' uno dei scienzati più importanti al mondo, Einstein aveva il suo ritratto sulla scrivania.
- Costruisse lui la prima dinamo
- Molto utili per regolare una tensione, fanno dà serbatorio per eliminare variazioni

[comment]: # (!!!)

### Altri componenti : Induttori

Bobina (induttore), sono "serbatoio di corrente"

![Induttore](media/induttori.png)

Abbreviazione (L), Simbolo, Unità (Farad)

![Simbolo](media/induttore.jpg)

Note:
- Usano un campo magnetico per immaganizzare energia, scoperti attorno al 1830
- Molto utili per filtrare parasiti, si oppongono alle variazioni veloci
- Perché si usa L ? Per Lenz, un fisico russo che scoprì il rapporto fra la corrente e la tensione.
- E' stato dato il suo nome ad un cratere sulla Luna
- Si misurano in Henry, ma è un'unità enorme, si usa spesso il milli-Henry. Il suo nome è stato dato ad una montagna negli USA.

[comment]: # (!!!)

### Schema elettrico

Conclusione : leggiamo uno schema elettrico assieme

![Radio](media/schema-radio.jpg)

Che simboli riconoscete?

Provate a indovinare cosa fa?

Note:
- Resistenze, Condensatori, Induttori (bobine), Diodo
- E' una radio AM
- Non lo costruiamo perché dobbiamo imparare a programmare l'elettronica nelle prossime lezioni
- Transistor al centro, è un componente a tre zampe semiconduttore
- Invece guarderemo da vicino i DIODI

[comment]: # (!!!)

### FINE TEORIA

Risolviamo problemi con Thonny/Board

[comment]: # (!!!)

### Uniamo elettricità e magnetismo

Oggi anche noi faremo esperimenti

&#x1F6B8; Costruiamo un motore elettrico

Il simbolo del motore

![Motor](media/motor%20symbol.png)

Note:
- Adesso scopriamo anche noi questo effetto nascosto

[comment]: # (!!!)

### Costruzione motore

&#x1F6B8; Istruzioni

- Mettere le due graffette sulle connessioni laterali della breadboard
- Disporre bobina in mezzo alle graffette
- Collegare le 3 batterie alle connessioni
- Dare un piccolo impulso alla bobina
- Avvicinare con la mano i magneti

Note:
- motore homopolo 
- quanto tutti hanno un motore funzionante passare alle domande

[comment]: # (!!!)

### Osservazione

Girano tutte nello stesso verso ?

Perché girano secondo voi ?

![Esempio](media/motore-1.png)

[comment]: # (!!!)

### Ipotesi

&#x1F6B8; Riassunto risultati

| Chi | Come gira | Perché gira ? |
| -- | -- | -- |
| Gruppo 1 | $$ \hookleftarrow \hookrightarrow ? $$ | ...... |
| Gruppo 2 | ..... | .... |
| Gruppo 3 | ..... | .... |
| Gruppo 4 | ..... | .... |
| Gruppo 5 | ..... | .... |
| Gruppo 6 | ..... | .... |

Provate a farlo girare nell'altro senso ?

[comment]: # (!!!)

## Ipotesi 

&#x1F6B8; Da cosa dipende il senso di rotazione ?

Osserviamo

<iframe width="560" height="315" src="media/motore.mp4" title="Video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Note:
- "è l'elettricità" che lo fa girare ? -> allora togliamo il magnete
- "senso di rotazione diversi" -> cambiamo verso del magnete 
- provare a cambiare il + e il - della pila
- ricordare effetto di Orsted

[comment]: # (!!!)

### Conclusioni scientifiche

Le cariche elettriche in movimento nella bobina creano un "magnete" che viene attratto o respinto dal magnete fisso

Questa spinta fa girare la bobina.
- esattamente come l'ago della bussola si spostava con la corrente
- però la bussola poi si fermava... perché questo no?

Note:
- Non è affatto semplice spiegare che il campo magnetico del magnete fisso attrae metà bobina e respinge metà bobina creando il movimento 
- Spiegare la regola della mano sinistra mi sembra troppo ambizioso

[comment]: # (!!!)

### Conclusioni scientifiche

Perché non rimangono i magneti in equilibrio (e invece va avanti a girare) ?

La parte di filo in contatto con la graffetta è conduttrice *solo a metà* 

Ad ogni mezza-rotazione si interrompe la corrente *ma la bobina continua per inerzia*

Note:
- Valutare se fare l'esperimento con multimetro e bobina in rotazione per osservare generazione

### Misura delle resistenze con il multimetro

&#x1F6B8; Misurate le resistenze che avete sul tavolo

| Chi | Valore 1 | Valore 2  |
| -- | -- | -- |
| Gruppo 1 | ..... Ω | -- |
| Gruppo 2 | ..... Ω | -- |
| Gruppo 3 | ..... Ω | -- |
| Gruppo 4 | ..... Ω | -- |
| Gruppo 5 | ..... Ω | -- |
| Gruppo 6 | ..... Ω | -- |

[comment]: # (!!!)

### Esperimento 3

&#x1F6B8; Circuito su breadboard

Mettere 2 resistenze uguali una dopo l'altra
Mettere 2 resistenze uguali accanto l'uno l'altra
Misurate la resistenza totale 

[TinkerCad](https://www.tinkercad.com/things/8aVDNguOsCs)

![Resistenze](media/resistenze.jpg)

Note:
- [Circuito](https://www.tinkercad.com/things/8aVDNguOsCs-sizzling-borwo/editel)
- Accanto = parallelo
- Dopo = Serie
- Fili = ricordatevi la corda che deve circolare

[comment]: # (!!!)

### Esperimento 3

&#x1F6B8; Risultati

| Gruppo | Valore singola resistenza | Valore in serie | Valore in parallelo |
| -- | -- | -- | -- |
| 1 | ..... Ω | ..... Ω |..... Ω |
| 2 | ..... Ω | ..... Ω |..... Ω |
| 3 | ..... Ω | ..... Ω |..... Ω |
| 4 | ..... Ω |  ..... Ω |..... Ω |
| 5 | ..... Ω | ..... Ω |..... Ω |
| 6 | ..... Ω | ..... Ω |..... Ω |

Note:
- Cosa possiamo concludere?

[comment]: # (!!!)

### Analisi risultati

| Gruppo | Misura Rparallelo | Teoria | Errore |
| -- | -- | -- | -- |
| 1  | ..... Ω | ..... Ω | ..... % |

## Elettronica con Micropython

![Micropython logo](media/micropython-logo.svg) <!-- .element: style="height:250px; max-width:200vw; image-rendering: crisp-edges;" -->

Pascal Brunot | AISTAP | Luglio 2023

Lezione 3 : semi-conduttori, diodi, board ESP32

[comment]: # (!!! data-background-color="aqua")

## I semi-conduttori

I componenti che abbiamo usati fin'ora erano "lineari"

Alcuni materiali possono essere sia isolanti che conduttori a secondo delle condizioni

Li chiamiamo semi-conduttori

Note:
- Lineari perché per resistenze U = R x I, Induttanze U = L x dV/dt, Capacità I =C x dV/dt
- Esempi : diodi, transistori, celle fotovoltaiche
- Ricordate perché alcuni materiali lasciano passare la corrente elettrica? (gli elettroni stretti o meno)

[comment]: # (!!!)

## La giunzione P-N

L'ingrediente fondamentale del diodo, creata nel 1939

![P-N](https://www.youtube.com/watch?v=JBtEckh3L9Q&t=3s)

Note:
- Ci stiamo avvicinando pian piano ai nostri giorni
- Prima di usare un semiconduttore dobbiamo capire il principio fisico che lo rende possibile.
- Valutare come tagliare il video. E' interessante ma troppo lungo.

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

## Esperimento 1 - LED e tensioni nel circuito

&#x1F6B8; Collegare come da schema con le vostre pile e la resistenza

[TinkerCad](https://www.tinkercad.com/things/8zAUERdv001)

&#x1F6B8; Misurate la tensione attorno al LED (1) e alla resistenza (2)

<small>

| Gruppo | Colore | Tensione U(LED) | Tensione U(R) |
| -- | -- | -- | -- |
| 1 | -- | ..... V | .... V |
| 2 | -- | ..... V | .... V |
| 3 | -- | ..... V | .... V |
| 4 | -- | ..... V | .... V |
| 5 | -- | ..... V | .... V |
| 6 | -- | ..... V | .... V |

</small>

Note:
- Fare osservare che U(LED) + U(R) = U(pile) - Legge di Kirshoff
- La caduta di tensione è dovuta alla giunzione P-N ed è indipendente dalla corrente (non si può applicare la legge di Ohm al diodo)
- Fare calcolare la corrente nel circuito ? (utile per ritornare su corrente uguale e legge di Ohm)

[comment]: # (!!!)

## Circuiti integrati

Tanti transistor messi assieme per uno scopo (memorizzare, fare operazioni logiche)

Economici da fabbricare in grandi quantità

- Fabbrichiamo migliari di migliardi di transistor ogni anno

![Wafer](media/wafer_45nm.jpg)

Note:
- Esistono circuiti integrati per tutte le operazioni comuni in elettronica
- Esistono circuiti integrati che sono capaci di ricevere istruzioni da altri circuiti e di eseguirle
- Diventano così "microprocessori" o più semplicemente "processori"


[comment]: # (!!!)

## Struttura della board S2 PICO

<div class="twocolumn">
<div>

- Microprocessore con memoria integrata
- Antenna WiFi
- Interrutori ("switch")
- Resistenze, Condensatori
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

Note: prendete la board e guardatela tutti

[comment]: # (!!!)

## Unità di misura : velocità

Processore: la frequenza alla quale prende istruzioni
- 1 Hertz = 1 istruzione al secondo
- Il nostro può arrivare a 240.000.000 Hz

E' un processore molto potente

![Gameboy ESP32](media/esp32gb_detail.jpg)

Note:
- Con questa board abbiamo abbastanza potenza per una console di gioco

[comment]: # (!!!)

## Unità di misura : memorie

*Memoria volatile* (RAM)
- Circa 2 millioni di bytes (2 Mb)
- Viene persa quando perde la corrente

*Memoria flash*
- Circa 4 millioni di bytes (4Mb)
- Rimane anche senza corrente grazie ad un condensatore

Note:
- Il tedesco Heinrich Rudolf Hertz scoprì le onde elettromagnetiche nel 1885
- Quando sentite parlare di Gigabytes? cosa vuole dire?
- Qual'è la memoria più veloce? La PSRAM (10-50ns vs. 500 us)

[comment]: # (!!!)

## Esperimento 2 - Board S2 PICO

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

## Premi ai gruppi scientifici più precisi

* Migliore precisione per la verifica esperimentale delle resistenze in parallelo ?

* Migliore precisione per la verifica esperimentale delle tensioni in un circuito ?

Vince chi ha l'errore più piccolo

$$ Errore = \lvert \frac{Misura - Teoria}{Teoria} \rvert $$

Note:
- Usare foglio excel a supporto e dati raccolti sui moduli
- Premio potrebbe essere un LED? Il pallone di elio?

[comment]: # (!!!)

## Conclusioni

Sito Micropython (dove scaricare firmware e documentazione)

[Micropython](https://micropython.org/)

Componenti usati

- [S2 Pico](https://www.wemos.cc/en/latest/s2/s2_pico.html)

- [Ali Express](https://it.aliexpress.com/item/1005003215673294.html) 

- [APA 106](https://it.aliexpress.com/item/1005001863273661.html)

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

## Micropython

Micropython e Python

[micropython.org](https://micropython.org/)

Librerie (<code>import X / from X import A</code>)

Note:
- Storia di Micropython, creato da un fisico teorico australiano
- Kickstarter per finanziare il progetto, è stato poi usato a bordo di satelliti
- E' un Python più leggero per microprocessori, bastano KB invece di MB di RAM

[comment]: # (!!!)

## Micropython 

Come programmare senza board collegata?

[WOKWI](https://wokwi.com/projects/305568836183130690)

Note:
- Quelli che hanno un computer e rete wifi si possono collegare a www.wokwi.com e selezionare "ESP32 with Micropython"

[comment]: # (!!!)

## Micropython: Sequenza di boot

Quando si accende il computer, parte il sistema operativo

Con Micropython al "power-on" o pulstane "reset"

- Esegue il file boot.py *non lo toccate*
- Esegue il file main.py *noi lavoremo qua*

Note:
- Nel file boot.py ho preparato gli import e le funzioni utili per il resto del corso

[comment]: # (!!!)

## Librerie Python e Micropython

E' molto importante riusare codice già testato (librerie)

Micropython dà librerie utili

- Librerie machine [Link](https://docs.micropython.org/en/v1.20.0/library/machine.html)
- Librerie dispositivi (NeoPixel, Bluetooth...) [Link](https://docs.micropython.org/en/v1.20.0/library/neopixel.html)
- Librerie Python (random, math, time, ecc..) [Link](https://docs.micropython.org/en/v1.20.0/library/random.html)

[comment]: # (!!!)

## Pratica BOARD

&#x1F6B8; Caricare un file PY in Thonny

```python
while True:
    Pin(10).on()
    sleep_ms(1000)
    Pin(10).off()
    sleep_ms(1000)
```

&#x1F6B8; Caricare il file PY sul controllore come main.py

&#x1F6B8; Premere RESET

[comment]: # (!!!)

## Breadboard e LED esterno

Fare lampeggiare LED esterno con una resistenza

Note:
- Dare Pin-out delle board usata, ripassare GPIO / Bus
- Proiettare CIRCUITO DA REALIZZARE con simboli standard
- Realizzare un circuito con board su scheda a connessione senza fili
- Modificare script fornito per fare lampeggiare il LED
- Ripasso diodo (verso giusto)

[comment]: # (!!!)

## LED esterno

Circuito da realizzare

[WOKWI](https://wokwi.com/projects/366723277993554945)

![Wokwi](media/wokwi-1.jpg)

&#x1F6B8; Realizzatelo sulla board o con WOKWI

[comment]: # (!!!)

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
while True:
    Pin(10).on()
    sleep(1)
    Pin(10).off()
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

Note:
- Funziona perché il nostro corpo conduce un po' l'elettricità e perturba un oscillatore
- Aggiungere in boot.py gli import (from machine import TouchPad, from time import sleep_ms)

[comment]: # (!!!)

## TouchPAD

Accendiamo il LED quando rileviamo il tocco

```python
tp = TouchPad(Pin(4))
SOGLIA = ...
while True:
    if tp.read() > SOGLIA:
        Pin(10).on()
    else:
        Pin(10).off()
    sleep_ms(250)
```

```python
tp = TouchPad(Pin(4))
SOGLIA = ...
while True:
    if tp.read() > SOGLIA:
        Pin(10).on()
        display.text('Ciao!', 40, 12, 1)
        display.show()
    else:
        Pin(10).off()
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

- Board Arduino o ESP32 (AliExpress)
- La robottica
- Altri componenti collegabili (motori, sensori)
- Connessioni e bus dati (USB,seriali)

[comment]: # (!!!)
