
CC=gcc
CFLAGS=-O3 -fPIC -Wall 

SRCDIR=./src/
BINDIR=./bin/
INCDIR=./include/

SRCS=$(SRCDIR)statistics.c
OBJS=$(OBJDIR)statistics.o

# Windows
LIB=libstat.dll

all:  $(LIB)

$(LIB):$(SRCS)
	 $(CC) -shared -o $(BINDIR)$@  $(CFLAGS) $^ -I$(INCDIR) 
    

