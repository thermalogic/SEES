
SRCDIR=./src/
BINDIR=./bin/
INCDIR=./include/

all: statdemoso

statdemoso: $(SRCDIR)statdemo.c
	gcc -o $(BINDIR)$@ $^ -L$(BINDIR) -lstat -I$(INCDIR)
    
run:
	./bin/statdemoso    
