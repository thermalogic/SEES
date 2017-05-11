
all: hello.exe

hello.exe: hello.o
	 gcc -o ./code/gcc/hello.exe hello.o
	 del hello.o
    
hello.o: ./code/gcc/hello.c
	 gcc -c ./code/gcc/hello.c
     
clean:
	 del .\code\gcc\hello.exe