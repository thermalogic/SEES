
all: helloexe clean
	./bin/hello
    
helloexe: helloobj
	 gcc -o ./bin/hello ./obj/hello.o
    
helloobj: ./src/hello.c
	 gcc -c -o ./obj/hello.o ./src/hello.c

clean:
	 del .\obj\hello.o    
