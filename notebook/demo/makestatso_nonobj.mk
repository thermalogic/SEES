
CC=gcc
CFLAGS=-shared -O3 -Wall -fPIC 

SRCDIR=./src/
BINDIR=./bin/
INCDIR=./include/

SRCS=$(SRCDIR)statistics.c

# Windows
LIBNAME=libstat.dll

all:  $(LIBNAME)

$(LIBNAME):$(SRCS)
	 $(CC)  -o $(BINDIR)$@ $(CFLAGS) $^ -I$(INCDIR)   
