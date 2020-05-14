
CC=gcc

SRCDIR= ./src/
OBJDIR= ./obj/
BINDIR= ./bin/
INCDIR= ./include/

# SRCS=$(SRCDIR)statistics.c \ 
#     $(SRCDIR)statApp.c 

SRCS=$(wildcard $(SRCDIR)stat*.c)

# non-path filename
filename=$(notdir $(SRCS))

# the obj target of a source code using the pattern rule
OBJS=$(patsubst %.c,$(OBJDIR)%.o,$(filename))

all:statApp
    
statApp: $(OBJS)  
	$(CC) -o $(BINDIR)$@ $(OBJS) 

# the pattern rule: one step rule for multiple source files
$(OBJS):$(SRCS)
	$(CC) -o $(OBJDIR)$(notdir $@) -c $(patsubst  %.o,$(SRCDIR)%.c,$(notdir $@))  -I$(INCDIR) 
