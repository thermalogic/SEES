
SRC= ./gfortran/
BIN= ./bin/
OBJ= ./obj/

all: circle_test

circle_test: circleobj
	 gfortran -o $(BIN)circle_test.exe  $(OBJ)circle_test.o $(OBJ)class_Circle.mod
    
circleobj:
	 gfortran -o $(OBJ)class_Circle.mod -c  $(SRC)class_Circle.f08    
	 gfortran -o $(OBJ)circle_test.o  -c  $(SRC)circle_test.f08     
