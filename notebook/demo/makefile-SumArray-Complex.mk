
CC=gcc

SRCDIR= ./src/
OBJDIR= ./obj/
BINDIR= ./bin/
INCDIR= ./include/

SRCS=$(SRCDIR)SumArray.c \
     $(SRCDIR)mainSum.c 

filename=$(notdir $(SRCS))

OBJS=$(patsubst %.c,$(OBJDIR)%.o,$(filename))

all:mainSum
    
mainSum: $(OBJS)  
	$(CC) -o $(BINDIR)$@ $(OBJS) 

$(OBJS):$(SRCS)
	$(CC) -o $(OBJDIR)$(notdir $@) -c $(patsubst  %.o,$(SRCDIR)%.c,$(notdir $@))  -I$(INCDIR) 
