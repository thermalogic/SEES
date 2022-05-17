
SRC= ./src/
OBJ= ./obj/
BIN= ./bin/
INC=./include/

all: statdemoso

statdemoso: statobj  
	gcc -o $(BIN)$@ $(OBJ)statdemo.o -L$(BIN) -lstat

statobj: $(SRC)statdemo.c 
	gcc -c -o $(OBJ)statdemo.o $(SRC)statdemo.c -I$(INC)
    
run:
	./bin/statdemoso  
    
