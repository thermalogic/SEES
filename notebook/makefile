
all: mainmathfuns.exe

clean:
	del .\code\gcc\mainmathfuns.exe

mainmathfuns.exe: mainmathfuns.o ./code/gcc/mathfuns.h 
	gcc -o ./code/gcc/mainmathfuns mainmathfuns.o -I./code/gcc -L./code/gcc/ -lmathfuns
	del *.o

mainmathfuns.o: ./code/gcc/mainmathfuns.c 
	gcc -c ./code/gcc/mainmathfuns.c 