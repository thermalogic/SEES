
CC=gcc
CFLAGS=-DBUILD_DLL

SRCDIR= ./src/
OBJDIR= ./obj/
BINDIR= ./bin/
INCDIR=./include/

all: libregion4

libregion4: obj
	 $(CC) -shared -o $(BINDIR)libregion4.dll -static-libgcc $(OBJDIR)region4.o -Wl,--add-stdcall-alias,-output-def=libregion4.def
obj: 
	 $(CC) -c $(CFLAGS) -o $(OBJDIR)region4.o $(SRCDIR)region4.c -I$(INCDIR)
