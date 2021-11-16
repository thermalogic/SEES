BIN=./bin/
INC=./include/
MAIN_FILE=main.c
SONAME=libCoolProp.so.6
REAL_NAME=libCoolProp.so.6.4.1
LINKER_NAME=libCoolProp.so
OUTPUT_FILE=mainso.out
LINKERFLAGS=-L./bin -lCoolProp 

all:buildexec runner

buildexec:
	g++ -DCOOLPROP_LIB -o $(BIN)${OUTPUT_FILE}  $(MAIN_FILE) -I$(INC) $(LINKERFLAGS)
    
runner:
	$(BIN)${OUTPUT_FILE}
    
install:
	cp $(BIN)$(REAL_NAME) /usr/lib/
	ln -sf $(REAL_NAME)  /usr/lib/$(SONAME)
	ln -sf $(SONAME)  /usr/lib/$(LINKER_NAME)
    
