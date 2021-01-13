BIN=./bin/
SRC=./src/
OBJ=./obj/
INC=./include/
MAIN_FILE=rtbisApp.c
SONAME=libroots.so.1
REAL_NAME=libroots.so.1.0.0
LINKER_NAME=libroots.so
OUTPUT_FILE=mainrtso.out
LINKERFLAGS=-L./bin -lroots -Wl,-rpath=./bin/

all:symlink buildexec exec

symlink:
	ln -sf $(REAL_NAME) $(BIN)$(SONAME)
	ln -sf $(SONAME) $(BIN)$(LINKER_NAME)

buildexec:
	gcc -o $(BIN)${OUTPUT_FILE}  $(SRC)$(MAIN_FILE) -I$(INC) $(LINKERFLAGS)
    
exec:
	$(BIN)${OUTPUT_FILE}
