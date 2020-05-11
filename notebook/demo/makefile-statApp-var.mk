
CC=gcc

SRCDIR= ./src/
OBJDIR= ./obj/
BINDIR= ./bin/
INCDIR=./include/

all: statApp

statApp: statobj  
	$(CC) -o $(BINDIR)statApp $(OBJDIR)statApp.o $(OBJDIR)statistics.o 

statobj:  
	$(CC) -c -o $(OBJDIR)statApp.o $(SRCDIR)statApp.c -I$(INCDIR) 
	$(CC) -c -o $(OBJDIR)statistics.o  $(SRCDIR)statistics.c -I$(INCDIR) 
