
all: mainSum

mainSum: sumobj  
	gcc -o ./bin/mainSum.exe ./obj/mainSum.o ./obj/SumArray.o 

sumobj:  
	gcc -c -o ./obj/mainSum.o ./src/mainSum.c -I./include/ 
	gcc -c -o ./obj/SumArray.o  ./src/SumArray.c -I./include/ 
