
CC=gcc
CFLAGS=-DBUILD_DLL

SRCDIR= ./src/
OBJDIR= ./obj/
BINDIR= ./bin/
INCDIR=./include/

all: libregion4

libregion4: obj
	 $(CC) -shared -o $(BINDIR)libR134aSat.dll -static-libgcc $(OBJDIR)R134aSat.o -Wl,--add-stdcall-alias,-output-def=libR134aSat.def
obj: 
	 $(CC) -c $(CFLAGS) -o $(OBJDIR)R134aSat.o $(SRCDIR)R134aSat.c -I$(INCDIR)
