import pygame
import sys
import numpy as np
from copy import copy
from pygame.locals import *
from random import randint

N = 100


def init():
    pygame.init()
    pygame.display.set_caption('Mrówka Langtona')


def rand_board():
    return np.zeros((N, N), dtype=int)

def draw(board):
    WINDOW = pygame.display.set_mode((N * 8, N * 8), 0, 32)
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)

    h = 0
    for i in range(N):
        w = 0
        for j in range(N):
            if board[i][j] == 1:
                pygame.draw.rect(WINDOW, RED, (w, h, 6, 6))
            else:
                pygame.draw.rect(WINDOW, BLACK, (w, h, 6, 6))
            w += 8
        h += 8


def update_pygame():
    #fps_clock = pygame.time.Clock()
    #fps_clock.tick(60)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


def next_gen(board, x ,y):
    result = copy(board)

    if board[x][y] == 0:
        result[x][y] = 1
    else:
        result[x][y] = 0

    return result


def destiny(destination, x, y, board):
    if board[x][y] == 0:
        if destination == 1:
            destination = 2
        elif destination == 2:
            destination = 3
        elif destination == 3:
            destination = 4
        elif destination == 4:
            destination = 1
    elif board[x][y] == 1:
        if destination == 1:
            destination = 4
        elif destination == 2:
            destination = 1
        elif destination == 3:
            destination = 2
        elif destination == 4:
            destination = 3

    return destination

def move(destiny, x, y):
    if destiny == 1:
        y -= 1
    elif destiny == 2:
        x += 1
    elif destiny == 3:
        y += 1
    elif destiny == 4:
        x -= 1
    return x, y

def main():
    init()
    generation = rand_board()
    x_c = N // 2
    y_c = N // 2
    t = 0

    #1-góra, 2-prawo, 3-dół, 4-lewo
    destination = randint(1, 4)

    while True:
        draw(generation)
        update_pygame()
        
        if t < 11000:
            x_c, y_c = move(destination, x_c, y_c)
            destination = destiny(destination, x_c, y_c, generation)
            generation = next_gen(generation, x_c, y_c)
            print(t)
            t += 1
 
        
if __name__ == '__main__':
    main()
