
all: statApp

statApp: statobj  
	gcc -o ./bin/statApp ./obj/statApp.o ./obj/statistics.o 

statobj:  
	gcc -c -o ./obj/statApp.o ./src/statApp.c -I./include/ 
	gcc -c -o ./obj/statistics.o  ./src/statistics.c -I./include/ 
