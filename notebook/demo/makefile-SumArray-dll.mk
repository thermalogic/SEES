
CC=gcc
CFLAGS=-O3 -Wall -fPIC 

SRCDIR= ./src/
OBJDIR= ./obj/
BINDIR= ./bin/
INCDIR=./include/

all: libdll

libdll: obj
	 $(CC) -shared -o $(BINDIR)libSumArray.dll $(OBJDIR)SumArray.o
    
obj: $(SRCDIR)SumArray.c
	 $(CC) -c $(CFLAGS)  -o $(OBJDIR)SumArray.o $(SRCDIR)SumArray.c -I$(INCDIR)
     
