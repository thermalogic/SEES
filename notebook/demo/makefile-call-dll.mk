
SRCDIR= ./src/
OBJDIR= ./obj/
BINDIR= ./bin/
INCDIR=./include/

all: mainexe

mainexe: sumobj  
	gcc -o $(BINDIR)mainSum.exe $(OBJDIR)mainSum.o -L$(BINDIR) -lSumArray

sumobj: $(SRCDIR)mainSum.c 
	gcc -c -o $(OBJDIR)mainSum.o $(SRCDIR)mainSum.c -I$(INCDIR)
