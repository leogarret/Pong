#!/usr/bin/env python3.6
##
## EPITECH PROJECT, 2018
## Léo
## File description:
## main.py
##

import contextlib
with contextlib.redirect_stdout(None):
    import pygame

pygame.init()

def main():
    game()
        


def game():
    # General
    display_width = 1000
    display_height = 700
    black = [0, 0, 0]
    white = [255, 255, 255]
    # ball
    ball_pos_x = display_width / 2
    ball_pos_y = display_height / 2
    ball_vel_x = 0
    ball_vel_y = 0
    ball_radius = 13
    # Players
    player_width = 20
    player_height = 100
    p1_pos_x = 15
    p1_pos_y = (display_height / 2) - (player_height / 2)
    p2_pos_x = display_width - 35
    p2_pos_y = (display_height / 2) - (player_height / 2)
    player_velocity = 0
    # Window
    window = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption("Pong")
    run = True
    while run:
        pygame.time.delay(2)
        key_p = pygame.key.get_pressed()
        if key_p[pygame.K_p]:
            player_velocity = 1
            ball_vel_x = 1
            ball_vel_y = 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        # rectangles moves
        if key_p[pygame.K_UP]:
            if p2_pos_y != 0: 
                p2_pos_y -= player_velocity
        if key_p[pygame.K_DOWN]:
            if (p2_pos_y + player_height) < display_height:
                p2_pos_y += player_velocity
        if key_p[pygame.K_z]:
            if p1_pos_y != 0:
                p1_pos_y -= player_velocity
        if key_p[pygame.K_s]:
            if (p1_pos_y + player_height) < display_height:
                p1_pos_y += player_velocity
        # collisions ball-rectangles
        if ball_pos_y > p2_pos_y and ball_pos_y < (p2_pos_y + player_height) and (ball_pos_x + ball_radius) == p2_pos_x or \
           ball_pos_y > p1_pos_y and ball_pos_y < (p1_pos_y + player_height) and (ball_pos_x - ball_radius) == p1_pos_x:
            ball_vel_x *= (-1)
        # collisions ball-wall
        if (ball_pos_y - ball_radius) == 0 or (ball_pos_y + ball_radius) == display_height:
            ball_vel_y *= (-1)
        if ball_pos_x == 0 + ball_radius or ball_pos_x == display_width - ball_radius:
            ball_pos_x = display_width / 2
            ball_pos_y = display_height / 2
            player_velocity = 0
            p1_pos_x = 15
            p1_pos_y = (display_height / 2) - (player_height / 2)
            p2_pos_x = (display_width - 25) - (player_width / 2)
            p2_pos_y = (display_height / 2) - (player_height / 2)
            ball_vel_x = 0
            ball_vel_y = 0
            ball_first = True
        # ball moves
        ball_pos_x += ball_vel_x
        ball_pos_y += ball_vel_y
        # print game
        window.fill(black)
        pygame.draw.circle(window, white, [int(ball_pos_x), int(ball_pos_y)], ball_radius, 0)
        pygame.draw.rect(window, white, (p1_pos_x, p1_pos_y, player_width, player_height), 0)
        pygame.draw.rect(window, white, (p2_pos_x, p2_pos_y, player_width, player_height), 0)
        pygame.draw.line(window, white, (display_width / 2, display_height), (display_width / 2, 0), 1)
        pygame.display.update()

pygame.quit()

main()