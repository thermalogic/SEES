
all: SumApp

SumApp: sumobj  
	gcc -o ./bin/SumApp.exe ./obj/SumApp.o ./obj/SumArray.o 

sumobj:  
	gcc -c -o ./obj/SumApp.o ./src/SumApp.c -I./include/ 
	gcc -c -o ./obj/SumArray.o  ./src/SumArray.c -I./include/ 
