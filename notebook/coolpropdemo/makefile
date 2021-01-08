BIN=./bin/
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
	g++ -o $(BIN)${OUTPUT_FILE} -DCOOLPROP_LIB  $(MAIN_FILE) -I./include $(LINKERFLAGS)
    
exec:
	$(BIN)${OUTPUT_FILE}
