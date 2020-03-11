
all: helloexe clean
	./bin/hello.exe
    
helloexe: helloobj
	 gcc -o ./bin/hello.exe ./obj/hello.o
    
helloobj: ./src/hello.c
	 gcc -c -o ./obj/hello.o ./src/hello.c

clean:
	 del .\obj\hello.o    
