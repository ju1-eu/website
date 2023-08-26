---
title: 'Markdown zu HTML Konverter'
author: 'ju'
date: \today
bibliography: literatur-kfz.bib 
csl: zitierstil-number.csl
---
<!--update 1-8-23 Markdown zu HTML Konverter-->

## Markdown zu HTML Konverter

### Überblick

Dieses Skript ermöglicht die Konvertierung von Text, der in Markdown verfasst wurde, in HTML. Es ist in PHP geschrieben und verwendet die `Parsedown`-Bibliothek, um eine korrekte Umsetzung des Markdown-Formats sicherzustellen.

### Installation

1. **Voraussetzungen**
    - Ein Server mit PHP-Unterstützung.
    - [Composer](https://getcomposer.org/), ein Werkzeug für die Abhängigkeitsverwaltung in PHP.

2. **Bibliothek installieren**
    Nach der Installation von Composer führt man den folgenden Befehl im Hauptverzeichnis des Projekts aus:

    ```bash
    # Terminal
    php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
    mkdir -p /usr/local/bin
    mv composer.phar /usr/local/bin/composer
    composer
    composer require erusev/parsedown
    ```

    Dies wird die `Parsedown`-Bibliothek in das Projekt herunterladen und installieren.

3. **Skript bereitstellen**
    Das zuvor bereitgestellte PHP-Skript kann in einem geeigneten Verzeichnis auf dem Server abgelegt werden.

### Scriptaufruf

Nachdem alles installiert wurde, kann man das Skript über einen Webbrowser aufrufen, indem man die entsprechende URL in die Adressleiste des Browsers eingibt. Zum Beispiel:

```
http://meinedomain.de/pfad/zum/script.php
```

### Funktionsweise

Nach dem Aufrufen des Skripts im Browser sieht man ein Formularfeld, in das Markdown-Text eingegeben werden kann. Nachdem der Text eingegeben und das Formular abgeschickt wurde, zeigt das Skript den eingegebenen Markdown-Text als HTML formatiert an.

### Testergebnisse

Das Skript wurde mit verschiedenen Markdown-Eingaben getestet, einschließlich, aber nicht beschränkt auf:

- Überschriften
- Listen (sowohl geordnet als auch ungeordnet)
- Links
- Bilder
- Textformatierungen wie **Fett**, *Kursiv* und `Code`.

In allen Testszenarien wurde der Markdown-Text korrekt in HTML umgewandelt und angezeigt.

### Sicherheitshinweis

Das Skript verwendet `htmlspecialchars` zur Behandlung von Benutzereingaben, um Cross-Site-Scripting-Attacken (XSS) zu verhindern. Es ist jedoch immer ratsam, weitere sicherheitsrelevante Aspekte im Auge zu behalten und das Skript regelmäßig auf Sicherheitslücken zu überprüfen, insbesondere wenn es in einer Produktionsumgebung eingesetzt wird.

### Schlussfolgerung

Das bereitgestellte Skript ist ein nützliches Werkzeug, um Markdown schnell und einfach in HTML umzuwandeln. Es bietet eine einfache Benutzeroberfläche und zuverlässige Konvertierungsfunktionen.