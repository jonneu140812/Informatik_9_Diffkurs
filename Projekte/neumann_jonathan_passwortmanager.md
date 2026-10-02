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

# Passwortmanager

- Sollte man einen Passwort Manager nutzen und wenn ja welchen? 

- Meine Kriterien
    - Kostenlose Option + Eine Anzahl an Features
        - man sollte ihn ausprobieren können bevor man sich dazu enscheidet Geld auszugeben oder die kostenlose version nutzen können
        - Die Kostenlose Version sollte 
    - Zero-Knowledge
        - Wichtig ist es das die passworter nur von mir gelesen werden können 
    - Import und Sync funktionalität
        - Das Setup und die nutzung sollte leicht sein.

---
## Warum braucht man einen Passwortmanager

1. Warum ist es unsicher, dasselbe Passwort bei mehreren Diensten zu verwenden?
    - Wird ein passwort öffendlich bekannt wie z.B. durch einen datenleck sind alle accounts unsicher
1. Warum sind lange, einzigartige und zufällig erzeugte Passwörter schwer selbst zu verwalten
    - gute passwörter sind lange und bestehen aus zufälligen zeichen. Diese Passwörter sind sich schwer zu merken weil sie meist >12 zeichen sind und besondere zeichen beinhalten. Deswegen wurden die meisten leute sie sich nicht merken sonderen anderwegst speichen wie auf z.B post-it notes oder in Text datein, beide dies optionen haben große sicherheits risiken.
---
## Warum braucht man einen Passwortmanager

1. Welche Vorteile kann ein Passwortmanager bieten?
    - Ein Passwortmanager gibt die möglichkeit Passwörter sicher zu speichern. Dies erreicht der Passwortmanager indem er die Passwörter nicht in reintext speichert. Um diese Passwörter lesen zu können muss man ein Masterpasswort nutzen.
1. Welche Risiken oder Nachteile bleiben trotz Passwortmanager bestehen?
    - Datenlecks können eine Chat-history oder Passwörter öffendlich bekannt machen. Das Masterpasswort ist das was die alle passworter sicher hält wird dieses Passwort bekannt sind auch alle anderen nicht mehr sicher. Selbst ist man das grösste risiko denn teilt man Passworter ist dies naturlich auch ein Risiko.
---
## [1Password](https://1password.com/)

### Preise

- 

<!-- 1Passwort hat keine Kostenlosen Versionen  -->

### Bezahlte Features

- Sicherheits benachrichtungen
- Autosave und Autofill von Passwortern
- Benachrichtigungen bei schwachen oder kompromittierten Zugangsdaten erhalten

---
## [1Password](https://1password.com/)

### Sicherheit

- End-to-End Encryption
- PBKDF2-HMAC-SHA256 key strengthening
- AES-GCM-256 encryption
- dual-key encryption
    - Die Passwörter sind mit einem passwort und ein 128-bit Secret Key verschlüsselt
- Warnt bei Sicherheitsverletzung

- Nutzt eine Zero-Knowledge strukture
- Hat Passwortgenerator


---
## [Proton](https://proton.me/pass)

### Preis

- Proten Free
    - Kostenlos
- Pass Plus
    - 2.99 € pro Monat
- Pass Unlimited
    - 9.99 € pro Monat

---
## [Proton](https://proton.me/pass)

### Kostenlose Features

- Passwort generator
- 10 email Aliases
- Benachritiung bei schawchen Passworten
- Passkey support
- Passwort Import Funktion

---
## [Proton](https://proton.me/pass)

### Bezahlte Features

- Two-Factor-Authentication
- Unendliche Email Aliase
- Sicheres Vault teilen

<!--- Proton besitzt keine  --->
---
## [Proton](https://proton.me/pass)

### Sicherheit

- End-to-end encryption
- 256-bit AES-GCM vault encryption
- Passkeys

---
## [KeyPassXC](keepassxc.org)