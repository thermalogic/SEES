nbs = $(wildcard *.ipynb)
	pdfs = $(nbs:%.ipynb=%.pdf)

all: $(pdfs)

%.pdf: %.ipynb
	jupyter-nbconvert --to pdf $<
