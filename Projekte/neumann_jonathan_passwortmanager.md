---
marp: true
paginate: true
style: |
  section {
    display: flex;
    flex-direction: column;
    padding: 40px;
    background-color: #f8f7f7;
    color: #0f0f0f;
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
    - Passwortgenerator
        - Der Passwortmanager sollte es leicht machen sichere passwörter zu nutzen

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

- Einzelperson
    - Jahrlich: 3.65 € pro monat
    - Monatlich: 4.39 €

- Familie
    - Jahrlich: 4.31 € pro monat 
    - Monatlich: 6.99 €

- Keine Kostenlose option 

---

## [1Password](https://1password.com/)

### Sicherheit

- End-to-End Encryption
- PBKDF2-HMAC-SHA256 key strengthening
- AES-GCM-256 encryption
- dual-key encryption
    - Die Passwörter sind mit einem passwort und ein 128-bit Secret Key verschlüsselt
- Warnt bei Sicherheitsverletzung

-Nutzt eine Zero-Knowledge strukture
- Hat Passwortgenerator


---
## [Bitwarden](https://bitwarden.com/)


---
## [Proton](https://proton.me/pass)

### Preis
- Einzelperson
   - Kostenlos
- Einzelperson Premium
   - Jährlich 1,45 € im Monat: 17,39 € im Jahr
- Familie
   - Jährlich 3,50 € im Monat: 42,14 € im Jahr
- Team
   - 3,51 € im Monat pro Nutzer. Wird jährlich abgerechnet.
-  Enterprise
   - 5,27 € im Monat pro Nutzer. Wird jährlich abgrechnet.

- Proten Free
    - Kostenlos
- Pass Plus
    - 2.99 € pro Monat
- Pass Unlimited
    - 9.99 € pro Monat

---
## [Bitwarden](https://bitwarden.com/)

### Kostenlose Features
- Unbegrenzte Passwörter speichern
- Alle Browser-Erweiterung die es für Bitwarden gibt
- Zugriff auf die iOS, Android, Windows, macOS und Linux Apps
- Passwort-Synchronisierung auf allen Geräten
- *Grundlegende* Sicherheit mit Ende-zu-Ende Verschlüsselung
- Passwort Import Funktion
---
 ## [Bitwarden](https://bitwarden.com/)

 ### Bezahlte Features
 - Integrierter Authentifikator (2FA)
 - Datei-Anhänge (Bis zu 1GB Speicher)
 - Notfall-Zugriff: Falls was passiert können bestimmte Leute auf deinen Vault zugreifen
 - Vault-Gesundheitsberichte (Identifiziert schwache Passwörter) 
 -
 ---

## [Bitwarden](https://bitwarden.com/)

### Kostenlose Features

- Passwort genarator 
- 10 email ailiases
- Benachrichtigung bei schwachen Passwortern
- Passwort Import Funktion
- Passkey support

---
## [Proton](https://proton.me/pass)

### Bezahlte Features

- Two-Factor-Authentication
- Unendliche Email Aliase
- Sicheres Vault teilen

---
## [Proton](https://proton.me/pass)

### Sicherheit

- Verschlüsselung
   - HMAC-SHA-256: 600.000 Hashing-Vorgänge
   - Zero-Knowledge Verschlüsselung
   - Vault Health Reports: Warnt bei Sicherheitsverletzungen
- Sicherheitszertifikate
   - ISO 27001
   - SOC 2 Typ II

- 
