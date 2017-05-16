
all: DemoBinarySearch.exe

DemoBinarySearch.exe: DemoBinarySearch.o
	 gcc -o ./src/DemoBinarySearch.exe DemoBinarySearch.o
	 del DemoBinarySearch.o
    
DemoBinarySearch.o: ./src/DemoBinarySearch.c ./src/BinarySearch.c
	 gcc -c ./src/DemoBinarySearch.c ./src/BinarySearch.c
     
clean:
	 del .\src\DemoBinarySearch.exe