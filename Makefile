##
## EPITECH PROJECT, 2018
## makefile
## File description:
## to make
##

NAME	=	101pong

all:
	cp 101pong.py $(NAME)

clean:
	rm -rf $(NAME)

fclean: clean

re:	clean all