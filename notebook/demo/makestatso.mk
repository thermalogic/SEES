
CC=gcc
CFLAGS=-O3 -Wall -fPIC 

SRCDIR=./src/
OBJDIR=./obj/
BINDIR=./bin/
INCDIR=./include/

# Linux
#LIB=libstat.so
# Windows
LIB=libstat.dll

all:  $(LIB)

$(LIB): statobj
	 $(CC) -shared -o $(BINDIR)$@ $(OBJDIR)statistics.o
    
statobj: $(SRCDIR)statistics.c
	 $(CC) -c $(CFLAGS)  -o $(OBJDIR)statistics.o $(SRCDIR)statistics.c -I$(INCDIR)    
