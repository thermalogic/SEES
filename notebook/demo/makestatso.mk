
CC=gcc
CFLAGS=-O3 -Wall -fPIC 

SRC=./src/
OBJ=./obj/
BIN=./bin/
INC=./include/

# Windows
LIB=libstat.dll

all:  $(LIB)

$(LIB): statobj
	 $(CC) -shared -o $(BIN)$@ $(OBJ)statistics.o
    
statobj: $(SRC)statistics.c
	 $(CC) -c $(CFLAGS)  -o $(OBJ)statistics.o $(SRC)statistics.c -I$(INC)    
