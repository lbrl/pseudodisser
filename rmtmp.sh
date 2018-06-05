#! /bin/bash

rm -rf *.aux
rm -rf *.bcf
rm -rf *.log
rm -rf *.run.xml
rm -rf *.toc
rm -rf *.bbl
rm -rf *.blg

pdflatex main.tex
biber main
pdflatex main.tex
pdflatex main.tex
