import os
import glob
import argparse

"""
Das Programm bearbeitet LaTeX-Dateien, indem es spezifische Befehle entfernt und vorherige Versionen der Dateien in Backup-Dateien speichert. Es kann entweder alle Dateien in einem Verzeichnis oder eine bestimmte Datei bearbeiten. Am Ende werden alle Backup-Dateien gelöscht.
python3 ./latex-convert1.py # alle Dateien konvertieren (A) oder nur eine bestimmte (B)
python3 ./latexcode-entfernen2.py # alle Dateien
python3 ./latexcode-entfernen2.py -h # Hilfe
python3 ./latexcode-entfernen2.py --datei DATEI # nur eine Datei ohne .tex
make # pdflatex - alle Dateien
make compile_with_xelatex # xelatex - alle Dateien
make single_pdflatex FILE=datei # pdflatex - nur eine Datei ohne .tex
make single_xelatex FILE=datei # xelatex - nur eine Datei ohne .tex
"""

# Konstanten als Großbuchstaben (Python-Konvention)
VERZEICHNIS_PFAD = "./tex"
LATEX_BEFEHL = "\\passthrough"  # suchen und ersetzen von \passthrough

def entferne_befehl(tex_pfad, befehl):
    """
    Entfernt einen bestimmten LaTeX-Befehl aus einer .tex-Datei und erstellt eine .bak-Backup-Datei.
    """
    try:
        with open(tex_pfad, 'r') as datei:
            inhalt = datei.read()
            # debug
            if befehl in inhalt:
                print(f"Befehl {befehl} gefunden in {tex_pfad}")
            else:
                print(f"Befehl {befehl} nicht gefunden in {tex_pfad}")

        backup_pfad = tex_pfad + '.bak'
        with open(backup_pfad, 'w') as backup_datei:
            backup_datei.write(inhalt)
        with open(tex_pfad, 'w') as datei:
            datei.write(inhalt.replace(befehl, ""))
    except IOError as e:
        print(f"Fehler beim Bearbeiten der Datei {tex_pfad}: {e}")

def loesche_backup_dateien():
    """
    Löscht alle .bak-Dateien im angegebenen Verzeichnis.
    """
    for backup_datei in glob.iglob(os.path.join(VERZEICHNIS_PFAD, "*.bak")):
        try:
            os.remove(backup_datei)
        except OSError as e:
            print(f"Fehler beim Löschen der Backup-Datei {backup_datei}: {e}")

def bearbeite_dateien(spezifische_datei=None):
    """
    Bearbeitet .tex-Dateien im angegebenen Verzeichnis oder eine spezifische Datei.
    """
    dateien = [os.path.join(VERZEICHNIS_PFAD, spezifische_datei + '.tex')] if spezifische_datei else list(glob.iglob(os.path.join(VERZEICHNIS_PFAD, "*.tex")))
    # debug
    print(f"Zu bearbeitende Dateien: {dateien}")

    for tex_datei in dateien:
        if os.path.isfile(tex_datei):
            entferne_befehl(tex_datei, LATEX_BEFEHL)
            print(f"Datei {tex_datei} bearbeitet.")

def main():
    """
    Hauptfunktion, die andere Funktionen in der richtigen Reihenfolge aufruft.
    """
    parser = argparse.ArgumentParser(description='Bearbeitet LaTeX-Dateien.')
    parser.add_argument('--datei', help='Name der spezifischen .tex-Datei, die bearbeitet werden soll. Ohne .tex-Endung.')
    args = parser.parse_args()

    # Sicherheitsüberprüfung: Stellen Sie sicher, dass der Dateiname keine unsicheren Zeichen oder Pfade enthält.
    if args.datei and (not args.datei.isalnum() or '..' in args.datei or '/' in args.datei):
        print("Ungültiger Dateiname. Bitte geben Sie einen sicheren Dateinamen ohne Pfadangaben an.")
        return

    bearbeite_dateien(args.datei)
    loesche_backup_dateien()

if __name__ == "__main__":
    main()
