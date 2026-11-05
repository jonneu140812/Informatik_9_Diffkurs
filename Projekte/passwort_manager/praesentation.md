---
marp: true
paginate: true
style: 
  section {
    display: flex;
    flex-direction: column;
    padding: 40px;
  }

---

# Passwortmanager:

## Sollte man einen Passwortmanager nutzen und wenn ja, welchen?

- Meine Kriterien
    - Kostenlose Option + eine Anzahl an Funktionen

    - Zero-Knowledge

    - Automatische Sync-Funktionalität

<!--- Eine kostenlose Version ist mir wichtig, weil ich als Schüler nicht viel Geld ausgeben will.
Zero-Knowledge heißt, dass der Anbieter deine Passwörter nicht lesen kann, sie sind verschlüsselt. Wie der Name schon sagt, braucht man einen Schlüssel, um die Passwörter lesen zu können.
Das ist wichtig, weil die Passwörter sicher sein sollen.
Passwörter sollten automatisch überall gleich sein, denn der Aufwand eines Passwortmanagers sollte nicht zu groß sein. --->


---

## Warum braucht man einen guten Passwortmanager?

### Vorteile

1. Sicherheit

<!--- Hat ein Dienst ein Datenleck, ist dieses Passwort und alle Accounts, die es nutzen, nicht mehr sicher. --->

<!--- Gute Passwörter bestehen meist aus langen, zufälligen und schwer zu merkenden Zeichen. Sie aufzuschreiben ist ebenfalls unrealistisch. --->

2. Verwaltung

<!--- Ein Passwortmanager gibt dir die Möglichkeit, deine Passwörter leicht und sicher zu speichern. --->

---

## [1Password](https://1password.com/)

### Was bekomme ich für mein Geld? (Es gibt keine kostenlose Version.)

- Sicherheitsbenachrichtigungen
- Autosave und Autofill von Passwörtern
- Benachrichtigungen bei schwachen oder kompromittierten Zugangsdaten erhalten

<!-- Wie man sieht bzw. nicht sieht: 1Password hat keine kostenlosen Versionen,
d. h. das erste Kriterium ist bei 1Password nicht erfüllt.
Automatische Sync gibt es hier auch, was ein Kriterium erfüllt. -->

---

## [1Password](https://1password.com/)

### Wie sieht die Sicherheit von 1Password aus?

- End-to-End-Encryption
- PBKDF2-HMAC-SHA256 key strengthening
- AES-GCM-256 encryption
- Dual-Key-Encryption
    - Die Passwörter sind mit einem Passwort und einem 128-Bit-Secret-Key verschlüsselt
- Warnt bei Sicherheitsverletzungen

<!--- Encryption, der Prozess, Passwörter unleserlich zu machen, hat 1Password, und alle Passwörter sind durch ein Master-Passwort geschützt.
Eine Warnung bei Sicherheitsverletzungen ist auch ein nettes Feature.
Am wichtigsten ist aber eine Zero-Knowledge-Structure, die laut ihnen auch existiert. --->

---

## [Proton Pass](https://proton.me/pass)

### Was sind die Optionen bei Proton Pass?

Besitzt eine kostenlose Version
und eine bezahlte Version (ab 2,99 € pro Monat)

<!--- Proton Pass besitzt eine kostenlose Version, was heißt, dass es mein erstes Kriterium erfüllt.
Die bezahlte Version ist relativ günstig und bringt ein paar nette Features,
aber ist nichts, was man essenziell braucht.  --->

### Wie sicher ist Proton Pass?

- End-to-End-Encryption
- 256-Bit-AES-GCM-Vault-Encryption
- Passkeys

<!--- Proton hat End-to-End-Encryption und eine Zero-Knowledge structure was heißt das sie nie deine Daten sehen können.
Passkeys ist ein Gerät gebundenes Passwort, d. h. diese extra schicht an sicherheit ist einem Häcker nutzlos selbst wenn er sie hätte. --->

---

## [Proton Pass](https://proton.me/pass)

### Was sind die kostenlosen Features?

- Passwortgenerator
- 10 E-Mail-Aliase
- Benachrichtigung bei schwachen Passwörtern
- Passkey-Support
- Passwort-Import-Funktion

<!--- Die kostenlosen Features sind auch etwas, was den Anfang angenemer machen könnte, denn eine Import-Funktion macht die Einrichtung kürzer und führt dazu, dass du schneller beginnen kannst, den Passwortmanager zu nutzen. --->

---

## [Proton Pass](https://proton.me/pass)

### Was bekommt man von der bezahlten Version?

- Two-Factor-Authentication
- Unendliche E-Mail-Aliase
- Sicheres Vault teilen

<!--- 2FA ist immer ein gutes Feature, 2FA ist ein weitere schicht von verifizierung die beim log-in benötigt ist, aber das braucht man nicht essenziell.
Ein Vault teilen zu können und unendliche E-Mail-Aliase sind eigentlich nutzlos für mich. --->

---

## [KeePassXC](https://keepassxc.org)

### Was kostet mich das?

- Es ist nur kostenlos erhältlich

<!--- KeePass besitzt keine bezahlte Version, alles ist kostenlos,
d. h. es gibt keine bezahlten Extra-Features, was gut ist. --->

---

## [KeePassXC](https://keepassxc.org)

### Ist es sicher zu nutzen?

- KeePassXC kann lokal laufen

- Security Visa von ANSSI

<!--- Weil KeePass lokal laufen kann macht es das relativ sicher.
Lokal zu laufen bringt nämlich Vor- und Nachteile mit sich,
zwar ist es sehr sicher, weil es nur auf eurem Gerät läuft,
aber es macht es auch schwer, Passwörter zwischen Geräten gleich zu halten.  --->

---

## Was soll ich jetzt nutzen?

- 1Password (2/3) Keine kostenlose Version

- **Proton Pass** (3/3)

- KeePassXC (2/3) Kein Sync

<!--- Anhand der erfüllten Kriterien würde ich von meinen Dreien Proton Pass empfehlen.
Hier würde ich aber noch sagen wollen, dass Proton Pass nicht der einzige gute Dienst ist. Bitwarden z. B. wäre laut meinen Bitwarden Kriterien auch empfehlenswert. --->

- Honorable Mentions: Bitwarden

<!--- Ich habe Bitwarden nicht in der Präsentation enthalten, weil es durch meine Kriterien zu ähnlich zu Proton Pass wäre. --->

