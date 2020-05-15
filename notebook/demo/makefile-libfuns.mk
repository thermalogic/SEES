
CC=gcc
CFLAGS=-O3 -Wall -fPIC

SRCDIR= ./src/
OBJDIR= ./obj/
BINDIR= ./bin/
INCDIR= ./include/

# Linux
# LIB=libfuns.so 
LIB=libfuns.dll

SRCS=$(SRCDIR)statistics.c \
    $(SRCDIR)funs.c 

# non-path filename
filename=$(notdir $(SRCS))

# the obj target of a source code using the pattern rule
OBJS=$(patsubst %.c,$(OBJDIR)%.o,$(filename))

all:$(LIB)
    
$(LIB): $(OBJS)  
	$(CC) -shared -o $(BINDIR)$@ $(OBJS) 

$(OBJS):$(SRCS)
	$(CC) $(CFLAGS) -o $@ -c $<  -I$(INCDIR) 
