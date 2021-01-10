BIN=./demo/bin/
SRC=./demo/src/
OBJ=./demo/obj/

all:buildexec exec

buildexec:
	gcc -o $(OBJ)gsl-example.o -c $(SRC)gsl-example.c
	gcc -o $(BIN)gsl-example  $(OBJ)gsl-example.o  -lgsl -lgslcblas -lm
    
exec:
	$(BIN)gsl-example
