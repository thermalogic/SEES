
INC= -IC:./include \
    -IC:/Python38/include \
    -IC:/Python38/Lib/site-packages/numpy/core/include

        
LIBDIR= C:/Python38/

SRC= ./src/spring_matplotlib.cpp \
    ./src/PolynomialFit.c 
            
BIN= ./bin/demo

all: spring_matplotlib

spring_matplotlib: 
	 g++ -std=c++11 -o $(BIN) $(SRC) $(INC) -L$(LIBDIR) -lPython38 
