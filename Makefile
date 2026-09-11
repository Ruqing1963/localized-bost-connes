.PHONY: all verify figures paper papers monograph clean quick

PYTHON ?= python3
LATEX  ?= pdflatex

# Every paper of the series: the foundational paper in paper/, the numbered
# papers I-XXV in papers/<numeral>-<slug>/, one .tex file per directory.
SERIES := $(wildcard papers/*/*.tex)

all: verify figures paper papers

verify:
	cd code && $(PYTHON) verify_claims.py
	cd code && $(PYTHON) verify_series.py

quick:
	cd code && $(PYTHON) verify_claims.py --quick

figures:
	cd code && $(PYTHON) make_figures.py

# Foundational paper (three passes for the table of contents).
paper:
	cd paper && $(LATEX) -interaction=nonstopmode master_bost_connes_paper.tex >/dev/null
	cd paper && $(LATEX) -interaction=nonstopmode master_bost_connes_paper.tex >/dev/null
	cd paper && $(LATEX) -interaction=nonstopmode master_bost_connes_paper.tex >/dev/null
	@echo "built paper/master_bost_connes_paper.pdf"

# Papers I-XXV.
papers:
	@for f in $(SERIES); do \
	  d=$$(dirname $$f); b=$$(basename $$f .tex); \
	  (cd $$d && $(LATEX) -interaction=nonstopmode $$b.tex >/dev/null \
	          && $(LATEX) -interaction=nonstopmode $$b.tex >/dev/null \
	          && $(LATEX) -interaction=nonstopmode $$b.tex >/dev/null) \
	  && echo "built $$d/$$b.pdf" || echo "FAILED $$f"; \
	done

# The monograph assembled from the papers (see monograph/README.md).
monograph:
	cd monograph && $(PYTHON) assemble.py
	cd monograph && $(LATEX) -interaction=nonstopmode main.tex >/dev/null
	cd monograph && $(LATEX) -interaction=nonstopmode main.tex >/dev/null
	cd monograph && $(LATEX) -interaction=nonstopmode main.tex >/dev/null
	@echo "built monograph/main.pdf"

clean:
	rm -f paper/*.aux paper/*.log paper/*.out paper/*.toc
	rm -f papers/*/*.aux papers/*/*.log papers/*/*.out papers/*/*.toc
	rm -f monograph/*.aux monograph/*.log monograph/*.out monograph/*.toc monograph/chapters/*.aux
	rm -rf code/__pycache__ code/bcloc/__pycache__
