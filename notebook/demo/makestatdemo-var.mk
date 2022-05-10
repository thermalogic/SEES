
CC=gcc

SRCDIR= ./src/
OBJDIR= ./obj/
BINDIR= ./bin/
INCDIR=./include/

all: statdemo

statdemo: statobj  
	$(CC) -o $(BINDIR)statdemo $(OBJDIR)statdemo.o $(OBJDIR)statistics.o 

statobj:  
	$(CC) -c -o $(OBJDIR)statdemo.o $(SRCDIR)statdemo.c -I$(INCDIR) 
	$(CC) -c -o $(OBJDIR)statistics.o  $(SRCDIR)statistics.c -I$(INCDIR) 
