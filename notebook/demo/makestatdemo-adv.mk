
CC=gcc

SRCDIR= ./src/
OBJDIR= ./obj/
BINDIR= ./bin/
INCDIR= ./include/

#SRCS=$(SRCDIR)statistics.c \ 
#     $(SRCDIR)statdemo.c 

SRCS=$(wildcard $(SRCDIR)stat*.c)

# non-path filename
filename=$(notdir $(SRCS))

# the obj target of a source code using the pattern rule
OBJS=$(patsubst %.c,$(OBJDIR)%.o,$(filename))

all:statdemo
    
statdemo: $(OBJS)  
	$(CC) -o $(BINDIR)$@ $^ 
	del .\obj\*.o

$(OBJS):$(SRCS)
	$(CC) -o $@ -c $(SRCDIR)$(patsubst  %.o,%.c,$(notdir $@))  -I$(INCDIR) 
