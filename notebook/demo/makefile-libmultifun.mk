
CC=gcc
CFLAGS=-O3 -Wall -fPIC

SRCDIR= ./src/
OBJDIR= ./obj/
BINDIR= ./bin/
INCDIR=./include/

all: libmultifuns

libmultifuns: multifunsobj
	 $(CC) -shared -o $(BINDIR)libmultifuns.dll $(OBJDIR)funs.o $(OBJDIR)SumArray.o
   
multifunsobj: $(SRCDIR)funs.c $(SRCDIR)SumArray.c
	$(CC) -c $(CFLAGS) -o $(OBJDIR)SumArray.o $(SRCDIR)SumArray.c -I$(INCDIR)
	$(CC) -c $(CFLAGS) -o $(OBJDIR)funs.o $(SRCDIR)funs.c -I$(INCDIR)
