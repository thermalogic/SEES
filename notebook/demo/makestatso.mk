
CC=gcc
CFLAGS=-O3 -Wall -fPIC 

SRCDIR=./src/
OBJDIR=./obj/
BINDIR=./bin/
INCDIR=./include/

SRCS=$(SRCDIR)statistics.c
OBJS=$(OBJDIR)statistics.o

# Windows
LIB=libstat.dll

all:  $(LIB)

$(LIB):$(OBJS)
	 $(CC) -shared -o $(BINDIR)$@ $^
    
$(OBJS): $(SRCS)
	 $(CC) -c $(CFLAGS) -o $@ $^ -I$(INCDIR)    
