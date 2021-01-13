BIN=./bin/
INC=./include/
MAIN_FILE=mainso.c
SONAME=libCoolProp.so.6
REAL_NAME=libCoolProp.so.6.4.1
LINKER_NAME=libCoolProp.so
OUTPUT_FILE=mainso.out
LINKERFLAGS=-L./bin -lCoolProp -Wl,-rpath=./bin/

all:symlink buildexec exec

symlink:
	ln -sf $(REAL_NAME) $(BIN)$(SONAME)
	ln -sf $(SONAME) $(BIN)$(LINKER_NAME)

buildexec:
	g++ -DCOOLPROP_LIB -o $(BIN)${OUTPUT_FILE}  $(MAIN_FILE) -I$(INC) $(LINKERFLAGS)
    
exec:
	$(BIN)${OUTPUT_FILE}
