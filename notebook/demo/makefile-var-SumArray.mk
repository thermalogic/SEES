
CC=gcc

SRCDIR= ./src/
OBJDIR= ./obj/
BINDIR= ./bin/
INCDIR=./include/

all: mainSum

mainSum: sumobj  
	$(CC) -o $(BINDIR)mainSum.exe $(OBJDIR)mainSum.o $(OBJDIR)SumArray.o 

sumobj:  
	$(CC) -c -o $(OBJDIR)mainSum.o $(SRCDIR)mainSum.c -I$(INCDIR) 
	$(CC) -c -o $(OBJDIR)SumArray.o  $(SRCDIR)SumArray.c -I$(INCDIR) 
