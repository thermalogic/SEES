INC= -I./include \
	-IC:/Python38/include \
	-IC:/Python38/Lib/site-packages/numpy/core/include
     
LIB= -LC:/Python38/ \
	-L./bin/

SRC= ./src/spring_matplotlib.cpp    
            
BIN= ./bin/demofit

all: spring_matplotlib
	./bin/demofit.exe

spring_matplotlib:
	g++ -w -o  $(BIN) $(SRC) $(LIB) -lPython38  -lcurvefit $(INC) 
