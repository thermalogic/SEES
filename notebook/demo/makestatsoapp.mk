
SRCDIR= ./src/
OBJDIR= ./obj/
BINDIR= ./bin/
INCDIR=./include/

all: statappso

statappso: statobj  
	gcc -o $(BINDIR)$@ $(OBJDIR)statapp.o -L$(BINDIR) -lstat
#	gcc -o $(BINDIR)$@ $(OBJDIR)statApp.o -L$(BINDIR) -lstat -Wl,-rpath=./bin/  

statobj: $(SRCDIR)statapp.c 
	gcc -c -o $(OBJDIR)statapp.o $(SRCDIR)statapp.c -I$(INCDIR)
