---
marp: true
paginate: true
style: |
  section {
    display: flex;
    flex-direction: column;
    padding: 40px;
  }

---

# Passwortmanager: 

##  Sollte man einen Passwort Manager nutzen und wenn ja welchen?

- Meine Kriterien
    - Kostenlose Option + Eine Anzahl an Features

    - Zero-Knowledge

    - Automatische Sync funktionalität

<!--- eine Kostenlose version ist mir wichtig, weil ich als schüler nicht viel geld ausgeben will.
Zero-Knowledge heist das der anbieter deine Passworter nicht lesen kann, sie sind verschüsselt, wie der name schon sagt braucht man einen schlüssel um die Passworter lesen zu können. 
Das ist wichtig weil die Passworter sicher sein sollen.
Passwörter sollten automatisch überall gleich sein, denn der aufwand eines passwortmanagers sollte nicht zu groß sein.--->

---

## Warum braucht man einen Passwortmanager?

1. Warum ist es unsicher, dasselbe Passwort bei mehreren Diensten zu verwenden?

<!--- hat ein dienst ein datenleck ist dieses Passwort und alle acounts die es nutzen nicht mehr sicher. --->

2. Warum sind gute schwer selbst zu verwalten

<!--- gute passwörter bestehen ist meist lang zu fällig und schwer zu merken, sie aufzuschreiben sind auch unrealistisch, weil man meist viel zu viele passwörter für eine solche lösung --->

3. Welche Vorteile kann ein Passwortmanager bieten?

<!--- Ein Passwortmanager gibt dir die möglichkeit deine Passwörter leicht und sicher zu speichern. --->

---

## [1Password](https://1password.com/)

### Was bekomme ich für mein Geld? ( Es gibt keine kostenlose version )

- Sicherheits benachrichtungen
- Autosave und Autofill von Passwortern
- Benachrichtigungen bei schwachen oder kompromittierten Zugangsdaten erhalten

<!-- wie man sieht bzw nicht sieht; 1Passwort hat keine Kostenlosen Versionen,
d.h die erste kriterie ist nicht bei 1Password gegeben.
Automatische Sync gibt es hier auch was ein kriteritum erfüllt.-->

---

## [1Password](https://1password.com/)

### Wie sieht die sicherheit von 1Passwort aus?

- End-to-End Encryption
- PBKDF2-HMAC-SHA256 key strengthening
- AES-GCM-256 encryption
- Dual-key encryption
    - Die Passwörter sind mit einem passwort und ein 128-bit Secret Key verschlüsselt
- Warnt bei Sicherheitsverletzung

<!--- Encryption, der prozess passwort bzw text unleserlich zu machen , hat 1Passwort und alle Passworter sind durch ein Master Passwort geschüzt
Eine Warnung bei sicherheits verletzung ein auch nettes feature. 
Am wichtigsten aber eine zero knowledge structure gibt es laut ihnen auch. --->

---

## [Proton Pass](https://proton.me/pass)

### Was sind die optionen bei Proton Pass?

Besitzt eine Kostenlose version
und eine bezahlte version (ab 2.99 pro Monat )

<!--- Proton Pass besitzt eine kostenlose version, was heist das es mein erstes kriteritum erfühlt.
Die bezahlt version ist relativ güngstig und bringt ein paar nette features,
aber ist nichts was man essentiel braucht.  --->

### Wie sicher ist Proton Pass?

- End-to-end encryption
- 256-bit AES-GCM vault encryption
- Passkeys

<!--- Eine Zero-Knowledge Structure existiert und die encyption reicht zu meinen zwecken. --->

---

## [Proton Pass](https://proton.me/pass)

### Was sind die Kostenlose Features?

- Passwort generator
- 10 email Aliases
- Benachritiung bei schawchen Passworten
- Passkey support
- Passwort Import Funktion

<!--- Die kostenlosen features sind auch etwas was den anfang netter machen kann, denn eine Import Funktion macht die einrichtung kurzer und dazu fürt das du schneller beginnen kannst den Passwortmanager zu nutzte --->

---

## [Proton Pass](https://proton.me/pass)

### Was bekommt man von der bezahlten version? 

- Two-Factor-Authentication
- Unendliche Email Aliase
- Sicheres Vault teilen

<!--- 2FA ist immer ein gutes feature, aber das braucht man nicht essenziell.
Einen vault teilen zu können, und Unendliche Email Aliases sind eigendlich nutzlos für mich. --->

---

## [KeePassXC](https://keepassxc.org)

### Was kostet mich das?

- Es ist nur kostenlos erhaltbar, d. h. keine bezahlte version.

<!--- KeePass besitzt keine bezahlte version, alles ist kostenlos. --->

### Ist es sicher zu nutzen?

- KeePassXC kann lokal laufen

- Security Visa von ANSSI

<!--- Weil KeePass das macht das was alle anderen machen und dazu noch lokal laufen kann sind sie relativ Sichersten. 
Lokal zu laufen bring nämlich vor und nach teile mit dich, 
zwar ist es sehr sicher weil es nur auf eurem gerät lauft, 
aber macht das es auch schwerpasswörter zwischen geräten gleich zu halt.  --->

---

## Was soll ich jetzt nutzen?

- 1Passwort (2/3) Keine Kostenlose Version

- Proton Pass (3/3)

- KeePassXC (2/3) Kein Sync


<!--- Anhand der erfüllten krieterine würde ich von meinen dreien Proton Pass empfehlen.
Hier würde ich aber noch sage wollen das Proton Pass nicht der einzige gute dienst ist Bitwarde z.B würde laut meinen Kriterien auch empfehlenswert sein. --->

---

## Gibt es noch mehr zu wissen? ( Im schnell durchlauf )

- Warum ist der Google Passwortmanager so schlecht?

<!--- Weil eine Zero-Knowledge structure und richtige encyption fehlen ist der Google Passwortmanager sehr unsicher. --->

- Honorable Mentions: Bitwarden

<!--- Ich habe Bitwarden nicht in der Präsentation enthalten weil, durch meine kriterien zu ahnlich zu Proton Pass wäre --->
