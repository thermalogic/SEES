
CC=gcc
CFLAGS=-O3 -Wall -fPIC 

SRCDIR= ./src/
OBJDIR= ./obj/
BINDIR= ./bin/
INCDIR=./include/

# Linux
#LIB=libstat.so

LIB=libstat.dll

all:  $(LIB)

$(LIB): obj
	 $(CC) -shared -o $(BINDIR)$@ $(OBJDIR)statistics.o
    
obj: $(SRCDIR)statistics.c
	 $(CC) -c $(CFLAGS)  -o $(OBJDIR)statistics.o $(SRCDIR)statistics.c -I$(INCDIR)
     
