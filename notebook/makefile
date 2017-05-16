
all: DemobSearch.exe

DemobSearch.exe: bSearchobjs
	 gcc -o ./code/ds/DemobSearch.exe DemobSearch.o bSearch.o
	 del DemobSearch.o
    
bSearchobjs: 
	 gcc -c -I./code/ds ./code/ds/DemobSearch.c ./code/ds/bSearch.c
     
clean:
	 del .\code\ds\DemobSearch.exe