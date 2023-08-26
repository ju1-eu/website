# Makefile
# Das Makefile ermöglicht die automatisierte Umwandlung von .tex-Dateien in .pdf-Formate, 
# wobei sowohl "pdflatex" als auch "xelatex" als Kompilierungsoptionen bereitstehen. 
# Es bietet auch die Möglichkeit, unerwünschte Dateierweiterungen zu bereinigen.
# python3 ./latex-convert1.py # alle Dateien konvertieren (A) oder nur eine bestimmte (B)
# python3 ./latexcode-entfernen2.py # alle Dateien
# python3 ./latexcode-entfernen2.py -h # Hilfe
# python3 ./latexcode-entfernen2.py --datei DATEI # nur eine Datei ohne .tex
# make # pdflatex - alle Dateien
# make compile_with_xelatex # xelatex - alle Dateien
# make single_pdflatex FILE=datei # pdflatex - nur eine Datei ohne .tex
# make single_xelatex FILE=datei # xelatex - nur eine Datei ohne .tex

# Variablen
TEX_FILES := $(wildcard tex/*.tex)
PDF_PDFLATEX_FILES := $(patsubst tex/%.tex,pdf_pdflatex/%.pdf,$(TEX_FILES))
PDF_XELATEX_FILES := $(patsubst tex/%.tex,pdf_xelatex/%.pdf,$(TEX_FILES))
CLEAN_EXTENSIONS := aux bcf log out run.xml toc
DIRECTORIES := pdf_pdflatex pdf_xelatex

# Standardregel
all: pdflatex

# Regel für pdflatex für eine einzelne Datei
single_pdflatex: pdf_pdflatex/$(FILE).pdf

pdf_pdflatex/$(FILE).pdf: tex/$(FILE).tex
	$(compile_pdflatex)

# Regel für xelatex für eine einzelne Datei
single_xelatex: pdf_xelatex/$(FILE).pdf

pdf_xelatex/$(FILE).pdf: tex/$(FILE).tex
	$(compile_xelatex)


# Kompilieren mit pdflatex
pdflatex: $(PDF_PDFLATEX_FILES)

# Erstellungsregeln für pdflatex
define compile_pdflatex
	@echo "Kompilieren mit pdflatex: $<"
	@mkdir -p pdf_pdflatex
	@pdflatex -interaction=nonstopmode -shell-escape -output-directory=pdf_pdflatex $< 
	@pdflatex -interaction=nonstopmode -shell-escape -output-directory=pdf_pdflatex $< 
	@pdflatex -interaction=nonstopmode -shell-escape -output-directory=pdf_pdflatex $< || (cat pdf_pdflatex/$*.log && exit 1)
endef

pdf_pdflatex/%.pdf: tex/%.tex
	$(compile_pdflatex)

# Erstellungsregeln für xelatex (nur bei Bedarf)
compile_with_xelatex: $(PDF_XELATEX_FILES)

define compile_xelatex
	@echo "Kompilieren mit xelatex: $<"
	@mkdir -p pdf_xelatex
	@xelatex -interaction=nonstopmode -shell-escape -output-directory=pdf_xelatex $< 
	@xelatex -interaction=nonstopmode -shell-escape -output-directory=pdf_xelatex $< 
	@xelatex -interaction=nonstopmode -shell-escape -output-directory=pdf_xelatex $< || (cat pdf_xelatex/$*.log && exit 1)
endef

pdf_xelatex/%.pdf: tex/%.tex
	$(compile_xelatex)

# Aufräumen
clean:
	@for dir in $(DIRECTORIES); do \
		for ext in $(CLEAN_EXTENSIONS); do \
			rm -rf $$dir/*.$$ext; \
		done; \
	done
	@echo "Aufräumen abgeschlossen."

.PHONY: debug
debug:
	@echo "TEX_FILES: $(TEX_FILES)"
	@echo "PDF_PDFLATEX_FILES: $(PDF_PDFLATEX_FILES)"
	@echo "PDF_XELATEX_FILES: $(PDF_XELATEX_FILES)"
