
SRCDIR= ./src/
OBJDIR= ./obj/
BINDIR= ./bin/
INCDIR=./include/

all: statApp

statApp: statobj  
	gcc -o $(BINDIR)statApp $(OBJDIR)statApp.o -L$(BINDIR) -lstat

statobj: $(SRCDIR)statApp.c 
	gcc -c -o $(OBJDIR)statApp.o $(SRCDIR)statApp.c -I$(INCDIR)
