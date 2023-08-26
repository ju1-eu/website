---
title: 'Aufgaben zum C/C++ Kurs'
author: 'ju'
date: \today
bibliography: literatur-kfz.bib 
csl: zitierstil-number.csl
---
<!--update 4-6-23 Aufgaben zum C/C++ Kurs-->
# Aufgaben zum C/C++ Kurs 

Quelle: Universität Regensburg / Fakultät Physik


1. Aufgabe: "Schreiben Sie ein Programm, das den Namen des Benutzers einliest und ihn dann mit seinem Namen begrüßt. Verwenden Sie sowohl printf bzw. scanf als auch cout und cin."

```C
// Quellcode in C
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int istGueltigerName(char name[]) {
    for (int i = 0; i < strlen(name); i++) {
        if (!isalpha(name[i]) && name[i] != ' ') {
            return 0; // Falsch, wenn ein ungültiges Zeichen gefunden wird
        }
    }
    return 1; // Richtig, wenn alle Zeichen gültig sind
}

int main() {
    char name[50];

    while (1) {
        printf("Bitte geben Sie Ihren Namen ein: ");
        scanf(" %49[^\n]", name); // Eingabe von bis zu 49 Zeichen plus Null-Terminator

        if (istGueltigerName(name)) {
            printf("Hallo, %s!\n", name);
            break; // Schleife verlassen, wenn gültiger Name
        } else {
            printf("Ungültige Eingabe. Bitte geben Sie einen gültigen Namen ein.\n");
        }
    }

    return 0;
}
```

```C++
// Quellcode in C++
#include <iostream>
#include <string>
#include <cctype>

bool istGueltigerName(const std::string &name) {
    for (char c : name) {
        if (!std::isalpha(c) && c != ' ') {
            return false; // Falsch, wenn ein ungültiges Zeichen gefunden wird
        }
    }
    return true; // Richtig, wenn alle Zeichen gültig sind
}

int main() {
    std::string name;

    while (true) {
        std::cout << "Bitte geben Sie Ihren Namen ein: ";
        std::cin >> name;

        if (istGueltigerName(name)) {
            std::cout << "Hallo, " << name << "!" << std::endl;
            break; // Schleife verlassen, wenn gültiger Name
        } else {
            std::cout << "Ungültige Eingabe. Bitte geben Sie einen gültigen Namen ein." << std::endl;
        }
    }

    return 0;
}
```

```Python
# Quellcode in Python
def ist_gueltiger_name(name):
    return all(c.isalpha() or c == ' ' for c in name)

while True:
    name = input("Bitte geben Sie Ihren Namen ein: ")

    if ist_gueltiger_name(name):
        print(f"Hallo, {name}!")
        break
    else:
        print("Ungültige Eingabe. Bitte geben Sie einen gültigen Namen ein.")

```

```PHP
// Quellcode in PHP
<?php
function istGueltigerName($name) {
    return ctype_alpha(str_replace(' ', '', $name));
}

while (true) {
    echo "Bitte geben Sie Ihren Namen ein: ";
    $name = trim(fgets(STDIN));

    if (istGueltigerName($name)) {
        echo "Hallo, $name!\n";
        break;
    } else {
        echo "Ungültige Eingabe. Bitte geben Sie einen gültigen Namen ein.\n";
    }
}
?>
```

```C++
// Quellcode in Arduino
String name;

bool istGueltigerName(String name) {
    for (unsigned int i = 0; i < name.length(); i++) {
        if (!isAlpha(name[i]) && name[i] != ' ') {
            return false;
        }
    }
    return true;
}

void setup() {
    Serial.begin(115200);
    Serial.println("Bitte geben Sie Ihren Namen ein:");
}
void loop() {
    if (Serial.available()) {
        name = Serial.readStringUntil('\n');
        
        if (istGueltigerName(name)) {
            Serial.print("Hallo, ");
            Serial.print(name);
            Serial.println("!");
            while(1); // Programm beenden
        } else {
            Serial.println("Ungültige Eingabe. Bitte geben Sie einen gültigen Namen ein.");
        }
    }
}
```

**Testergebnisse:**

```
Bitte geben Sie Ihren Namen ein: 22
Ungültige Eingabe. Bitte geben Sie einen gültigen Namen ein.

Bitte geben Sie Ihren Namen ein: Jan Unger
Hallo, Jan Unger!

Bitte geben Sie Ihren Namen ein: Jan
Hallo, Jan!
```



2. Aufgabe: ""

```C
// Quellcode in C

```

```C++
// Quellcode in C++

```

```Python
# Quellcode in Python

```

```PHP
// Quellcode in PHP

```

```C++
// Quellcode in Arduino

```

**Testergebnisse:**

```
# Ausgabe

```