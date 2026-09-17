# Der Plus-Operator

## Warum verursacht '123 + "123"' einen Fehler?

Es sieht einen integer und erwartet das ander andere dateitype auch ein integer ist. Dieser ist aber ein String.

## Warum verursacht '"123" + 123' einen Fehler?

Es sieht einen integer und erwartet das ander andere dateitype auch ein integer ist. Dieser ist aber ein String.

## Zusammenfassung: Unterschiedliche Funktion des Operators '+' bei Zahlen und Zeichenketten

Der Operator verhält sich anders je nachdem mit welchen dateitypen er interagiert bei einem string verbindet er die beiden strings zu einem.
Bei einem integer werden sie addiert.
