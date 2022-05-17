
CC=gcc
CFLAGS=-O3 -Wall -fPIC

SRC= ./src/
OBJ= ./obj/
BIN= ./bin/
INC= ./include/

LIB=libmaths.dll

SRCS=$(SRC)statistics.c \
    $(SRC)number.c 

# non-path filename
filename=$(notdir $(SRCS))

# the obj target of a source code using the pattern rule
OBJS=$(patsubst %.c,$(OBJ)%.o,$(filename))

all:$(LIB)
    
$(LIB): $(OBJS)  
	$(CC) -shared -o $(BIN)$@ $^ 

# the pattern rule: one step rule for multiple source files
$(OBJS):$(SRCS)
	$(CC) $(CFLAGS) -o $@ -c $(SRC)$(patsubst  %.o,%.c,$(notdir $@))  -I$(INC)
