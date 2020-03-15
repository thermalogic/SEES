NOTEBOOKS= $(wildcard *.ipynb)
PDFSs = $(NOTEBOOKS:%.ipynb=%.pdf)

all: $(PDFS)

%.pdf: %.ipynb
	jupyter-nbconvert --to pdf $<
