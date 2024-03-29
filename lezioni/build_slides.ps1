(Get-Content -Encoding utf8 elettronica_micropython_1.md ) | Out-File -Encoding utf8NoBOM .\elettronica_micropython.md
(Get-Content -Encoding utf8 elettronica_micropython_2.md | Select-Object -Skip 28) | Out-File -Encoding utf8NoBOM -Append .\elettronica_micropython.md
(Get-Content -Encoding utf8 elettronica_micropython_3.md | Select-Object -Skip 28) | Out-File -Encoding utf8NoBOM -Append .\elettronica_micropython.md
(Get-Content -Encoding utf8 elettronica_micropython_4.md | Select-Object -Skip 28) | Out-File -Encoding utf8NoBOM -Append .\elettronica_micropython.md
(Get-Content -Encoding utf8 elettronica_micropython_5.md | Select-Object -Skip 28) | Out-File -Encoding utf8NoBOM -Append .\elettronica_micropython.md
(Get-Content -Encoding utf8 elettronica_micropython_bonus.md | Select-Object -Skip 28) | Out-File -Encoding utf8NoBOM -Append .\elettronica_micropython.md

mdslides .\elettronica_micropython_1.md --include media --output_dir ..\html\lezione1
mdslides .\elettronica_micropython_2.md --include media --output_dir ..\html\lezione2
mdslides .\elettronica_micropython_3.md --include media --output_dir ..\html\lezione3
mdslides .\elettronica_micropython_4.md --include media --output_dir ..\html\lezione4
mdslides .\elettronica_micropython_5.md --include media --output_dir ..\html\lezione5
mdslides .\elettronica_micropython_bonus.md --include media --output_dir ..\html\lezione_extra
mdslides .\elettronica_micropython.md --include media --output_dir ..\html\full
