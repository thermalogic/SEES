# makefile for lib and client
all:
	make -f makestatso.mk
	make -f makestatsodemo.mk
	make -f makestatsodemo.mk run
