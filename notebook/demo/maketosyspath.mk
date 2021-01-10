BIN=./bin/
SRC=./src/
OBJ=./obj/
INC=./include/

all: makeso syspath

syspath:   
	sudo cp $(INC)roots.h /usr/include/roots.h
	sudo cp $(BIN)libroots.so /usr/lib/libroots.so      
makeso:
	gcc -c -O3 -Wall -fPIC -o $(OBJ)roots.o  $(SRC)roots.c -I$(INC)
	gcc -shared -o $(BIN)libroots.so  $(OBJ)roots.o

clean:
	sudo rm -f /usr/include/roots.h
	sudo rm -f /usr/lib/libroots.so    
