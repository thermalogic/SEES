
SRCDIR= ./src/
OBJDIR= ./obj/
BINDIR= ./bin/
INCDIR=./include/


all: main

main: sumobj 
	gcc -o $(BINDIR)mainSum.exe $(OBJDIR)mainSum.o -L$(BINDIR) -lSumArray -Wl,-rpath=./bin/ 

sumobj: $(SRCDIR)mainSum.c 
	gcc -c -o $(OBJDIR)mainSum.o $(SRCDIR)mainSum.c -I$(INCDIR)  
     
