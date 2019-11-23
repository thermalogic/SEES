
INC= -IC:/Python37/include \
    -IC:/Python37/Lib/site-packages/numpy/core/include
        
LIBDIR= C:/Python37/

SRC= ./demo/src/spring_matplotlib.cpp \
    ./demo/src/PolynomialFit.c 
            
BIN= ./demo/bin/demo

all: spring_matplotlib

spring_matplotlib: 
	 g++ -std=c++11 -o $(BIN) $(SRC) $(INC) -L$(LIBDIR) -lPython37 
