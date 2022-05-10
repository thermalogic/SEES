
all: statdemo

statdemo: statobj  
	gcc -o ./bin/statdemo ./obj/statdemo.o ./obj/statistics.o 

statobj:  
	gcc -c -o ./obj/statdemo.o ./src/statdemo.c -I./include/ 
	gcc -c -o ./obj/statistics.o  ./src/statistics.c -I./include/ 
