
CC=gcc

SRCDIR= ./src/
OBJDIR= ./obj/
BINDIR= ./bin/
INCDIR= ./include/

#SRCS=$(SRCDIR)statistics.c \ 
#     $(SRCDIR)statApp.c 

SRCS=$(wildcard $(SRCDIR)stat*.c)

# non-path filename
filename=$(notdir $(SRCS))

# the obj target of a source code using the pattern rule
OBJS=$(patsubst %.c,$(OBJDIR)%.o,$(filename))

all:statApp
    
statApp: $(OBJS)  
	$(CC) -o $(BINDIR)$@ $(OBJS) 

$(OBJS):$(SRCS)
	$(CC) -o $@ -c $(SRCDIR)$(patsubst  %.o,%.c,$(notdir $@))  -I$(INCDIR) 
