
all: hello.exe

hello.exe: hello.o
	 gcc -o hello.exe hello.o
	 del hello.o
    
hello.o: ./code/gcc/hello.c
	 gcc -c ./code/gcc/hello.c
     
clean:
	 del hello.exe