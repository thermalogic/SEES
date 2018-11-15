
all: helloexe
    
helloexe: helloobj
	 gcc -o ./code/bin/hello.exe ./code/bin/hello.o
	 del .\code\bin\hello.o
    
helloobj: ./code/gcc/hello.c
	 gcc -c -o ./code/bin/hello.o ./code/gcc/hello.c
     
clean:
	 del .\code\bin\hello.exe
