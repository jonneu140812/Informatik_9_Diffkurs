# Code beschreiben

## Aufgabe

"""
1. Analysiere die Ausführung des Codes für folgende Eingabewerte:

  a.  10

  b.  -7

  c.  0

   d. 'Hallo'

2. Dokumentiere für jede Eingabe:

 a.   Welche Verzweigungen werden überprüft?

 b.   Welche Bedingungen werden zu True und welche zu False ausgewertet?

 c.   Welcher Code-Block wird ausgeführt?

 d.   Was wird ausgegeben?

3. Stelle deine Analyse in einer übersichtlichen Tabelle oder einem Flussdiagramm dar.

4. Erkläre, wie die Verzweigungslogik in diesem Code funktioniert und warum die Reihenfolge der Bedingungen wichtig ist.
"""

```python
zahl: int = int(input("Bitte eine Zahl eingeben: "))
msg: str = ""

if zahl > 0:
    msg = "Die Zahl ist größer 0!"
elif zahl < 0:
    msg = "Die Zahl ist kleiner 0!"
else:
    msg = "Treffer!"

print(msg)
```

## Meine Lösung

3.
||10|-7|0|'Hallo'
|---|---|---|---|---
|a|zahl > 0|zahl > 0, zahl < 0|zahl > 0, zahl < 0, else|nicht ereicht
|b1|True|False|False|nicht ereicht
|b2|nicht ereicht|True|False|nicht ereicht
|b3|nicht ereicht|nicht ereicht|True|nicht ereicht
|c|1.|2.|3.|nicht ereicht
|d|Die Zahl ist größer 0!|Die Zahl ist kleiner 0!|Treffer!|ValueError

4.
In dem Code wird erst gefragt, ob Die Zahl größer als 0 ist, ist dies wahr gibt es "Die Zahl ist größer 0!" aus, dann ob Die Zahl kleiner als 0 ist, ist dies wahr gibt es "Die Zahl ist kleiner 0!" , ist keines von beiden wahr gibt es "Treffer!" aus 

## Musterlösung der KI

Read , lines 1 to 200
Completed with input: {
  "path": "/home/codespace/.vscode-remote/data/agentSessionData/84703a92-4e16-4325-b3bf-e0c33674f848/attachments/ab67f3dc-9370-42b3-ad96-1eba273606b3/vertiefung_1_verzweigung_bei_if-Anweisungen.md",
  "view_range": [
    1,
    200
  ]
}

Ich habe die Aufgabe in `vertiefung_1_verzweigung_bei_if-Anweisungen.md` gelesen. Insgesamt ist deine Lösung auf dem richtigen Weg, aber es gibt zwei wichtige Punkte, die du noch sauberer machen solltest.

Stärken:
- Die Grundlogik ist korrekt verstanden: `if` prüft zuerst, dann `elif`, dann `else`.
- Für 10, -7 und 0 sind die Aussagen zum ausgeführten Block und zur Ausgabe richtig.
- Du erkennst auch, dass bei `elif` nur geprüft wird, wenn die vorherige Bedingung falsch war.

Was noch verbessert werden muss:
1. Bei `'Hallo'` liegt ein wichtiger Fehler vor:
- `zahl = int(input(...))` versucht, den Text in eine Zahl umzuwandeln.
- `int('Hallo')` wirft eine `ValueError`-Ausnahme.
- Dadurch werden die Bedingungen `if zahl > 0` und `elif zahl < 0` gar nicht erst ausgewertet.
- Das ist ein sehr wichtiger Punkt der Aufgabe und sollte ausdrücklich erwähnt werden.

2. Deine Erklärung in Punkt 4 ist verständlich, aber nicht ganz präzise:
- Das `else` greift nicht nur bei “keines von beiden wahr” im Sinne von “0”, sondern bei allen Werten, die nicht größer als 0 und nicht kleiner als 0 sind.
- In diesem Code ist das genau der Fall für 0.
- Die Reihenfolge ist wichtig, weil die erste wahre Bedingung sofort den Rest überspringt. Sonst könnten mehrere Bedingungen gleichzeitig erfüllt sein, was hier nicht gewünscht ist.

Korrekte Analyse der Eingaben:
- 10:
  - `zahl > 0` → True
  - `zahl < 0` → nicht geprüft, weil `if` bereits wahr ist
  - Ausgeführt: erster Block
  - Ausgabe: "Die Zahl ist größer 0!"

- -7:
  - `zahl > 0` → False
  - `zahl < 0` → True
  - Ausgeführt: zweiter Block
  - Ausgabe: "Die Zahl ist kleiner 0!"

- 0:
  - `zahl > 0` → False
  - `zahl < 0` → False
  - Ausgeführt: `else`
  - Ausgabe: "Treffer!"

- 'Hallo':
  - `int('Hallo')` schlägt fehl
  - `if`/`elif`/`else` werden nicht erreicht
  - Ergebnis: Laufzeitfehler (`ValueError`)

Ein besserer Tabellenaufbau könnte so aussehen:

| Eingabe | Bedingung 1 | Bedingung 2 | Block | Ausgabe |
|---|---|---|---|---|
| 10 | True | nicht geprüft | `if` | Die Zahl ist größer 0! |
| -7 | False | True | `elif` | Die Zahl ist kleiner 0! |
| 0 | False | False | `else` | Treffer! |
| 'Hallo' | nicht erreicht | nicht erreicht | kein Block | ValueError |

Fazit:
- Deine Lösung zeigt das Prinzip der Verzweigung schon gut.
- Für eine volle Punktzahl solltest du bei `'Hallo'` klar anmerken, dass der Fehler schon vor dem `if` entsteht.
- Du solltest außerdem die Wichtigkeit der Reihenfolge explizit erklären: “Erst prüfen, wenn wahr, dann abbrechen; sonst weiter zur nächsten Bedingung.”

Wenn du möchtest, kann ich dir auch noch eine verbesserte Musterlösung formulieren, die du direkt in dein Dokument übernehmen kannst.

## Verbesserter Code mit try ... except

```python
try:
    zahl = int(input("Bitte eine Zahl eingeben: "))
except ValueError:
    print("Bitte gib eine ganze Zahl ein.")
else:
    if zahl > 0:
        msg = "Die Zahl ist größer 0!"
    elif zahl < 0:
        msg = "Die Zahl ist kleiner 0!"
    else:
        msg = "Treffer!"

    print(msg)
```