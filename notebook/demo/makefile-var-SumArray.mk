
CC=gcc

SRCDIR= ./src/
OBJDIR= ./obj/
BINDIR= ./bin/
INCDIR=./include/

all: SumApp

SumApp: sumobj  
	$(CC) -o $(BINDIR)SumApp.exe $(OBJDIR)SumApp.o $(OBJDIR)SumArray.o 

sumobj:  
	$(CC) -c -o $(OBJDIR)SumApp.o $(SRCDIR)SumApp.c -I$(INCDIR) 
	$(CC) -c -o $(OBJDIR)SumArray.o  $(SRCDIR)SumArray.c -I$(INCDIR) 
