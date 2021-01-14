
LIBFLAGS=-L./bin -lvcc
ifneq ($(OS),Windows_NT)
	UNAME_S := $(shell uname -s)
    ifeq ($(UNAME_S),Linux)
        LIBFLAGS += -Wl,-rpath=./bin
    endif
endif

CFLAGES=-std=c++17 -O3 
	 
OUTFILE=./bin/vccdemo

all: $(OUTFILE)
	$(OUTFILE)

$(OUTFILE): ./demovcc.cpp  
	g++ $(CFLAGES) -o $@ $^   -I./include $(LIBFLAGS)
