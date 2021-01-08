
SRCDIR= ./src/
OBJDIR= ./obj/
BINDIR= ./bin/
INCDIR=./include/

all: statdemoso

statdemoso: statobj  
	gcc -o $(BINDIR)$@ $(OBJDIR)statdemo.o -L$(BINDIR) -lstat
#	gcc -o $(BINDIR)$@ $(OBJDIR)statApp.o -L$(BINDIR) -lstat -Wl,-rpath=./bin/  

statobj: $(SRCDIR)statdemo.c 
	gcc -c -o $(OBJDIR)statdemo.o $(SRCDIR)statdemo.c -I$(INCDIR)
