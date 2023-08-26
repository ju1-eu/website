import os
import subprocess

"""
Zusammenfassung:
Dieser Quellcode beinhaltet notwendige Programme und stellt Funktionen bereit, um Markdown-Dateien in HTML umzuwandeln. Dabei nutzt er das Tool "Pandoc" für die Konvertierung und stellt sicher, dass Dateipfade ordnungsgemäß verknüpft werden.
pip install markdown
pyhton3 ./html-konverter-py-markdown1.py # Markdown in HTML Konvertierung mit Python
pyhton3 ./html-konverter-pandoc1.py # Markdown in HTML Konvertierung mit pandoc
pyhton3 ./html-dateien-verarbeiten2.py # HTML Dateien verarbeiten
"""

# Konstanten
QUELL_ORDNER = "md"
ZIEL_ORDNER = "html"
ERWEITERUNG = ".md"

def sicher_verknuepfen(ordner, dateiname):
    """Verknüpft einen Ordner und einen Dateinamen sicher, um Traversierungsversuche zu vermeiden."""
    if os.path.isabs(dateiname) or dateiname.startswith(".."):
        return None
    return os.path.join(ordner, dateiname)

def markdown_nach_html_konvertieren(quell_datei, ziel_datei):
    """Verwendet Pandoc, um eine Markdown-Datei in HTML zu konvertieren."""
    try:
        subprocess.run(["pandoc", "--mathjax", quell_datei, "-o", ziel_datei], check=True)
    except subprocess.CalledProcessError:
        print(f"Fehler beim Konvertieren von '{quell_datei}' mit Pandoc.")

def main():
    if not os.path.exists(QUELL_ORDNER):
        print(f"Der Ordner '{QUELL_ORDNER}' existiert nicht.")
        return

    os.makedirs(ZIEL_ORDNER, exist_ok=True)

    for dateiname in os.listdir(QUELL_ORDNER):
        if not dateiname.endswith(ERWEITERUNG):
            continue

        quell_pfad = sicher_verknuepfen(QUELL_ORDNER, dateiname)
        ziel_pfad = sicher_verknuepfen(ZIEL_ORDNER, os.path.splitext(dateiname)[0] + ".html")

        if not quell_pfad or not ziel_pfad:
            print(f"Ungültiger Dateiname: {dateiname}")
            continue

        markdown_nach_html_konvertieren(quell_pfad, ziel_pfad)

    print("Konvertierung abgeschlossen.")

if __name__ == "__main__":
    main()
