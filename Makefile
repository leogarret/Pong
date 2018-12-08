##
## EPITECH PROJECT, 2018
## makefile
## File description:
## to make
##

NAME	=	101pong

all:
	cp pong_game.py $(NAME)

clean:
	rm -rf $(NAME)

fclean: clean

re:	clean all
