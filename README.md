# AISTAP-Elettronica

Elettronica con Micropython, corso per associazione

[Versione online](https://aistap-micropython.pages.dev/)

[Supporto studenti](https://github.com/PBrunot/AISTAP/blob/7e9b8256f30b1230bd28bc3ea5775618a24819e6/support/supporto_studenti.pdf)

Contenuti
- Lezione 1: elettricità, U, I, R, misure con multimetro (1h30)
- Lezione 2: motore elettrico, resistenze in serie e parallelo, legge di Ohm con Python, cenni induttanze/condensatori (1h30)
- Lezione 3: semi-conduttori, misure di tensioni, board PICO S2 e Wokwi, errori di misura (1h30)
- Lezione 4: blink, LCD, NeoPixel, TouchPad con Micropython (1h30)
- Lezione 5: dado elettronico con Micropython (1h30)
- Lezione bonus: materiali extra, asyncio  (1 ora)

## Come preparare la lezione

Elenco materiali [XLSX](https://github.com/PBrunot/AISTAP/blob/7e9b8256f30b1230bd28bc3ea5775618a24819e6/support/BOM-xlsx.xlsx)

Disporre banchi a gruppi di ragazzi con il materiale della lezione preparato sul tavolo

Distribuire per gruppo le pagine corrispondenti del PDF di supporto


## Come ri-creare la presentazione HTML

Requisiti : installare mdslides

```ps
python -m pip install git+https://gitlab.com/da_doomer/markdown-slides.git
```

Trasformare codice MD in pagina html

```ps
mdslides .\elettronica_micropython_1.md --include media --output_dir ..\html\lezione1
```

Trasformare tutte le lezioni in una pagine HTML unica (richiede PowerShell 7.0+)

```ps
.\lezioni\build_slides.ps1
```
