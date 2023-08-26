import os
import subprocess
import glob

"""
Dieser Quellcode ermöglicht die Konvertierung von Markdown-Dateien in LaTeX-Format mittels des Programms Pandoc. Nutzer können wählen, ob alle Dateien oder nur spezifische Dateien konvertiert werden sollen. Außerdem werden Systemchecks und Fehlermeldungen integriert, um eine reibungslose Konvertierung sicherzustellen.
python3 ./latex-convert1.py # alle Dateien konvertieren (A) oder nur eine bestimmte (B)
python3 ./latexcode-entfernen2.py # alle Dateien
python3 ./latexcode-entfernen2.py -h # Hilfe
python3 ./latexcode-entfernen2.py --datei DATEI # nur eine Datei ohne .tex
make # pdflatex - alle Dateien
make compile_with_xelatex # xelatex - alle Dateien
make single_pdflatex FILE=datei # pdflatex - nur eine Datei ohne .tex
make single_xelatex FILE=datei # xelatex - nur eine Datei ohne .tex
"""

# Konstanten
QUELLPFAD = "./md"
ZIELPFAD = "./tex"
VORLAGEPFAD = "vorlage-main.tex" # Latexvorlage

def ist_pandoc_installiert():
    """Prüft, ob Pandoc auf dem System installiert ist."""
    try:
        subprocess.run(["pandoc", "--version"], capture_output=True, check=True)
        return True
    except Exception:
        return False

def konvertiere_md_zu_tex(md_pfad, tex_pfad):
    """Konvertiert eine einzelne .md-Datei in .tex mit pandoc."""
    try:
        subprocess.run(["pandoc", "--template=" + VORLAGEPFAD, "--listings", md_pfad, "-o", tex_pfad], capture_output=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Fehler bei der Konvertierung der Datei {md_pfad}:\n{e.stderr.decode()}")

def konvertiere_dateien(dateiname=None):
    """Konvertiert ausgewählte oder alle Markdown-Dateien zu LaTeX."""
    if not os.path.exists(QUELLPFAD):
        print(f"Quellordner {QUELLPFAD} existiert nicht.")
        return

    if not os.path.exists(VORLAGEPFAD):
        print(f"Vorlage {VORLAGEPFAD} existiert nicht.")
        return

    if not os.path.isdir(ZIELPFAD):
        os.makedirs(ZIELPFAD)

    if dateiname:
        if not dateiname.endswith(".md"):
            print("Bitte eine gültige .md-Datei angeben.")
            return
        md_dateien = [os.path.join(QUELLPFAD, dateiname)]
    else:
        md_dateien = glob.glob(os.path.join(QUELLPFAD, "*.md"))

    for md_datei in md_dateien:
        if not os.path.exists(md_datei):
            print(f"Die Datei {md_datei} existiert nicht.")
            continue
        tex_datei = os.path.join(ZIELPFAD, os.path.splitext(os.path.basename(md_datei))[0] + ".tex")
        konvertiere_md_zu_tex(md_datei, tex_datei)

    print("Konvertierung abgeschlossen.")

def main():
    if not ist_pandoc_installiert():
        print("Pandoc ist nicht installiert. Bitte installieren Sie Pandoc, um fortzufahren.")
        return

    auswahl = input("Möchten Sie alle Dateien konvertieren (A) oder nur eine bestimmte (B)? [A/B]: ").strip().upper()
    if auswahl == "A":
        konvertiere_dateien()
    elif auswahl == "B":
        dateiname = input("Geben Sie den Namen der zu konvertierenden Datei ein (z.B. beispiel.md): ")
        konvertiere_dateien(dateiname)
    else:
        print("Ungültige Auswahl.")

if __name__ == "__main__":
    main()
