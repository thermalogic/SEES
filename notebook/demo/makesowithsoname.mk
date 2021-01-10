BIN=./bin/
SRC=./src/
OBJ=./obj/
INC=./include/
SONAME=libroots.so.1
REAL_NAME=libroots.so.1.0.0

all:
	gcc -c -O3 -Wall -fPIC -o $(OBJ)roots.o  $(SRC)roots.c -I$(INC)
	g++ -shared $(OBJ)roots.o -Wl,-soname,$(SONAME) -o $(BIN)$(REAL_NAME)
