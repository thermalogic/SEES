
CC=gfortran
CFLAGS=-O3 -Wall -fPIC -o 

all: libfibonacci.dll

libfibonacci.dll: fibonacciobj
	 $(CC) -shared -o ./code/gfortran/libfibonacci.dll fibonacci.o
	 del fibonacci.o
    
fibonacciobj: ./code/gfortran/fibonacci.f90
	 $(CC) -c $(CFLAGS) fibonacci.o ./code/gfortran/fibonacci.f90
     
clean:
	 del .\code\gfortran\libfibonacci.dll