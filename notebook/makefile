
all: mainfibexe

clean:
	rm -f ./code/gcc/mainfib

mainfibexe: mainfibobj ./code/gcc/fibonacci.h 
	gcc -o ./code/gcc/mainfib mainfib.o -I./code/gcc/ -L./code/gcc/ -lfibonacci -Wl,-rpath=./code/gcc/ 
	rm -f *.o

mainfibobj: ./code/gcc/mainfib.c 
	gcc -c ./code/gcc/mainfib.c