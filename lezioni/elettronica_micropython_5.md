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

Lezione 5 : un dado elettronico

Note:
- Usare task indipendenti

[comment]: # (!!!)

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

## Pratica

- Dado elettronico

Se le schede hanno LCD:
- Lancio con GPIO Touch pin o switch se non supportato
- Risultato del dato su LCD
- Animazione su LCD fra i tiri

Task1 : blink led
Task2 : animazione schermo
Task3 : attesa touch e scelta numero

[comment]: # (!!!)

## Grazie

Se volete continuare la scoperta dell'elettronica

- Board Arduino o ESP32
- La robottica

