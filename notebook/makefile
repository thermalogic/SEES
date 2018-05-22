
all: helloexe

helloexe: helloobj
	 gfortran -o ./code/gfortran/hello hello.o
	 rm -f hello.o
    
helloobj: ./code/gfortran/hello.f90
	 gfortran -c ./code/gfortran/hello.f90
     
clean:
	rm -f ./code/gfortran/hello