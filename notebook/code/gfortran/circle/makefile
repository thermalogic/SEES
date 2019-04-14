
DIR= ./code/gfortran/circle/

all: circle_test

circle_test: obj
	 gfortran -o $(DIR)circle_test.exe  $(DIR)circle_test.o $(DIR)class_Circle.mod
	 del .\code\gfortran\circle\*.o
	 del .\code\gfortran\circle\*.mod    
    
obj:
	 gfortran -o $(DIR)class_Circle.mod -c  $(DIR)class_Circle.f08    
	 gfortran -o $(DIR)circle_test.o  -c  $(DIR)circle_test.f08     
