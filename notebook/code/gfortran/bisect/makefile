
DIR= ./code/gfortran/bisect/
program = nonlinear 
F08 = gfortran

$(program):
	$(F08) -o $(DIR)bisect.o -c $(DIR)bisect.f08  
	$(F08) -o $(DIR)myfun.o -c $(DIR)myfun.f08 
	$(F08) -o $(DIR)nonlinear.o -c $(DIR)nonlinear.f08 
	$(F08) -o $(DIR)nonlinear.exe $(DIR)nonlinear.o  $(DIR)bisect.o  $(DIR)myfun.o  
	del .\code\gfortran\bisect\*.o
