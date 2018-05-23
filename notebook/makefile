
all: libmultifuns.dll

libmultifuns.dll: multifunsobj
	 gcc  -shared -o ./code/gcc/libmultifuns.dll funs.o fibonacci.o
	 del funs.o fibonacci.o
    
multifunsobj: ./code/gcc/funs.c ./code/gcc/fibonacci.c
	 gcc -c -O3 -Wall -fPIC ./code/gcc/funs.c ./code/gcc/fibonacci.c
     
clean:
	 del .\code\gcc\libmultifuns.dll