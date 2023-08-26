import subprocess

"""
Das Programm stellt ein Menü zur Verfügung, mit dem verschiedene Befehle 
zur LaTeX-Verarbeitung ausgeführt werden können. 
Das Menü ermöglicht es, entweder alle Dateien zu konvertieren oder 
spezifische Dateien zu verarbeiten. 
Jeder Befehl ist mit einer eindeutigen Zahl verknüpft. 
Bei der Auswahl eines Befehls wird dieser sicher ausgeführt. 
Für bestimmte Befehle kann eine zusätzliche Eingabe erforderlich sein, z.B. der Name einer Datei.
"""

def sicherer_aufruf(befehl):
    """
    Führt einen Befehl sicher aus.
    """
    try:
        subprocess.run(befehl, check=True)
    except subprocess.CalledProcessError:
        print("Es gab einen Fehler beim Ausführen des Befehls.")
    except Exception as e:
        print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")

def main():
    # Definition der Befehlsvariablen
    LATEX_KONVERTIEREN = ["python3", "./latex-convert1.py"]
    LATEX_ENTFERNEN = ["python3", "./latexcode-entfernen2.py"]
    LATEX_ENTFERNEN_DATEI = ["python3", "./latexcode-entfernen2.py", "--datei"]
    MAKE = ["make"]
    MAKE_CLEAN = ["make", "clean"]
    MAKE_XELATEX = ["make", "compile_with_xelatex"]
    MAKE_PDFLATEX_EINZEL = ["make", "single_pdflatex", "FILE="]
    MAKE_XELATEX_EINZEL = ["make", "single_xelatex", "FILE="]
    HTML_PYTHON_MD = ["python3", "./html-konverter-py-markdown1.py"]
    HTML_PANDOC = ["python3", "./html-konverter-pandoc1.py"]
    HTML_VERARBEITEN = ["python3", "./html-dateien-verarbeiten2.py"]
    HTML_NAVIGATION = ["python3", "./navigationsseite-html.py"]

    # Befehle mit zugehörigen Namen und Kommandos
    BEFEHLE = {
        1: {"name": "LaTeX konvertieren", "command": LATEX_KONVERTIEREN},
        2: {"name": "LaTeX Code entfernen (Alle Dateien)", "command": LATEX_ENTFERNEN},
        3: {"name": "LaTeX Code entfernen (Spezifische Datei)", "command": LATEX_ENTFERNEN_DATEI},
        4: {"name": "PDFLaTeX (Alle Dateien)", "command": MAKE},
        5: {"name": "XeLaTeX (Alle Dateien)", "command": MAKE_XELATEX},
        6: {"name": "PDFLaTeX (Spezifische Datei)", "command": MAKE_PDFLATEX_EINZEL},
        7: {"name": "XeLaTeX (Spezifische Datei)", "command": MAKE_XELATEX_EINZEL},
        8: {"name": "Projekt aufräumen", "command": MAKE_CLEAN},
        9: {"name": "Markdown in HTML Konvertierung mit Python", "command": HTML_PYTHON_MD},
        10: {"name": "Markdown in HTML Konvertierung mit Pandoc", "command": HTML_PANDOC},
        11: {"name": "HTML Dateien verarbeiten", "command": HTML_VERARBEITEN},
        12: {"name": "Navigation über HTML Seiten erstellen", "command": HTML_NAVIGATION}
    }

    while True:
        # Menü für die Befehlsauswahl
        print("\nBitte wählen Sie einen Befehl aus:\n")
        for key, value in BEFEHLE.items():
            print(f"{key}. {value['name']}")

        # Eingabeaufforderung
        auswahl = input("\nGeben Sie die Nummer des gewünschten Befehls ein oder 'q' zum Beenden: ")

        if auswahl == 'q':
            break

        # Überprüfung der Eingabe
        if auswahl.isdigit() and int(auswahl) in BEFEHLE:
            befehl = BEFEHLE[int(auswahl)]['command'].copy()

            # Eingabeaufforderungen für Befehle, die spezifische Eingaben benötigen
            if auswahl == "3":
                datei = input("Bitte geben Sie den Dateinamen (ohne .tex) ein: ")
                befehl.append(datei)
            elif auswahl in ["6", "7"]:
                datei = input("Bitte geben Sie den Dateinamen (ohne .tex) für die Kompilierung ein: ")
                befehl[-1] += datei

            sicherer_aufruf(befehl)
        else:
            print("Ungültige Auswahl. Bitte erneut versuchen.")

if __name__ == "__main__":
    main()
