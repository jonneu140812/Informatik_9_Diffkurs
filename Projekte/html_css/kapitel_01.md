# Einführung

<!-- Ich bin ein Kommentar. -->

<!--
  Ich bin auch ein Kommentar.
  Ich gehe über 2 Zeilen.
-->

das ist ein Kommentar er ist nicht im browser sichbar sondern nur wenn man die html datei selbst liest
er startet mit <!-- 
und endet mit -->

<h1>Ich bin eine Überschrift</h1>
<h2>Ich auch</h2>
<h3>Ich auch</h3>
<h4>Ich auch</h4>
<h5>Ich auch</h5>
<h6>Ich auch</h6>

das sind mehrere  überschriften bzw eine überschrift mit einer unterüberschrift die auch eine unterüberschrift hat und so weiter

<p>
    Eines Tages sprach seine Mutter zu ihm: "Komm, Rotkäppchen, da hast du ein Stück Kuchen und eine


                  Flasche Wein, bring das der Großmutter hinaus; sie ist krank und schwach und wird sich daran laben. Mach dich auf,

    bevor es heiß wird, und wenn du hinauskommst, so geh hübsch sittsam und lauf nicht vom Wege ab, sonst fällst du und zerbrichst das Glas, und die
Großmutter hat nichts.
      Und wenn du in ihre Stube kommst, so vergiss nicht guten
      Morgen zu sagen und guck nicht erst in allen Ecken herum!"
</p>

das ist ein Text.
Die Tabs und lehren zeilen werden ignoriert.

<ol>
  <li>Äpfel</li>
  <li>Birnen</li>
  <li>Pfirsiche</li>
</ol>

das ist eine Liste

<h1>Huckleberry Finn</h1>
<!--
  Was war ich nochmal?
-->
<p>Huckleberry Finn ist eine von dem amerikanischen Schriftsteller Mark Twain erfundene literarische Figur.</p>

eine überschrift gefolgt von einem kommentar und einem Text.
Sichbar sind nur dir überschrift und der kommentar.

<p>
  Im HTML-Quelltext steht dieser Satz über mehrere Zeilen.
  Im Browser werden Zeilenumbrüche und mehrere Leerzeichen im normalen Text
  meist zu einem Leerzeichen zusammengefasst.
</p>

das ist eine zeile Text. Die zeilen umbrüche werden ignoriert.

# Vertiefung

## A1

als .docx kann vscode es nicht lesen und es gibt fiel extra zeichen 

als .txt ist nur text in der datei

txt und md sind warscheinlich plain text

## A2

<!DOCTYPE html>
<html lang="en">
<head>
<!--  Element head is missing a required instance of child element title. 
head braucht einen titel. ich habe ihm einen -->
    <title> hallo </title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
<!--  End tag h2 seen, but there were open elements. h1 wurde nie geschlossen. h2 wurde geschlossen aber nie geoffnet. ich habe h1 geschlossen. -->
    <h1>Meine tolle Webseite</h1>
    <p>Text</p>
<ol>
    <li>Zimmer aufräumen
    <li>Hausaufgaben machen<br>Mit Bello Gassi gehen</li>
    <li>Spülmaschine ausräumen</li>
<!-- Unclosed element ol. ol wurde nie geschlossen und ul nie gefönnet. ich habe /ul zu /ol gemacht -->
</ol>
</body>
</html>