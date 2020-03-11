
INC=-I./include \
    -IC:/Python38/include \
    -IC:/Python38/Lib/site-packages/numpy/core/include
        
LIBDIR= C:/Python38/

SRC= ./src/demo_matplotlib.cpp 
            
BIN= ./bin/demo

all: spring_matplotlib

spring_matplotlib: 
	 g++ -w -o $(BIN) $(SRC) $(INC) -L$(LIBDIR) -lPython38
