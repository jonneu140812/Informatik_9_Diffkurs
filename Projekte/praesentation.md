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
    - Zero-Knowledge
    - Automatische Sync funktionalität

<!--- eine Kostenlose version ist mir wichtig, weil ich als schüler nicht viel gelt ausgeben will.
Zero-Knowledge heist das der anbieter deine Passworter nicht lesen kann, sie sind verschüselt, wie der name schon sagt braucht man einen schlüssel um die Passworter lesen zu können. 
Passwörter sollten automatisch überall gleich sein, denn der aufwand eines passwortmanagers sollte nicht zu groß sein.--->

---

## Warum braucht man einen Passwortmanager?

1. Warum ist es unsicher, dasselbe Passwort bei mehreren Diensten zu verwenden?

<!--- hat ein dienst ein datenleck ist dieses Passwort und alle acounts die es nutzen nicht mehr sicher. --->

2. Warum sind gute schwer selbst zu verwalten

<!--- gute passwörter bestehen ist meist lang zu fällig und schwer zu merken, sie aufzuschreiben sind auch unrealistisch, weil man meist viel zu viele passwörter für eine solche lösung --->

---

## Warum braucht man einen Passwortmanager?

1. Welche Vorteile kann ein Passwortmanager bieten?

<!--- Ein Passwortmanager gibt dir die möglichkeit deine Passwörter leicht und sicher zu speichern. --->

1. Welche Risiken oder Nachteile bleiben trotz Passwortmanager bestehen?
    - Datenlecks können eine Chat-history oder Passwörter öffendlich bekannt machen. Das Masterpasswort ist das was die alle passworter sicher hält wird dieses Passwort bekannt sind auch alle anderen nicht mehr sicher. Selbst ist man das grösste risiko denn teilt man Passworter ist dies naturlich auch ein Risiko.

---

## [1Password](https://1password.com/)

### Preise / Bezahlte Features

- Sicherheits benachrichtungen
- Autosave und Autofill von Passwortern
- Benachrichtigungen bei schwachen oder kompromittierten Zugangsdaten erhalten

<!-- wie man sieht bzw nicht sieht; 1Passwort hat keine Kostenlosen Versionen, d.h die erste kriterie ist nicht bei 1Password gegeben.
Automatische Sync gibt es hier auch was ein kriteritum erfüllt.-->

---

## [1Password](https://1password.com/)

### Sicherheit

- End-to-End Encryption
- PBKDF2-HMAC-SHA256 key strengthening
- AES-GCM-256 encryption
- dual-key encryption
    - Die Passwörter sind mit einem passwort und ein 128-bit Secret Key verschlüsselt
- Warnt bei Sicherheitsverletzung

<!--- Encryption gibt es und alle Passworter sind hinter Passwortern versteckt.
Eine Warnung bei sicherheits verletzung ein auch nettes feature. 
Am wichtigsten aber eine zero knowledge structure gibt es laut ihnen auch. --->

---

## [Proton](https://proton.me/pass)

### Preis

- Proten Free
    - Kostenlos
- Pass Plus
    - 2.99 € pro Monat
- Pass Unlimited
    - 9.99 € pro Monat

<!---  --->

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

---

## [Proton](https://proton.me/pass)

### Sicherheit

- End-to-end encryption
- 256-bit AES-GCM vault encryption
- Passkeys

---

## [KeyPassXC](keepassxc.org)

### Preise

<!---  --->
