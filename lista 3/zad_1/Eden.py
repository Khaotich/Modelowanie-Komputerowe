import random
import pygame
import sys
import numpy as np
from copy import deepcopy
from pygame.locals import *

N = 100

def init():
    pygame.init()
    pygame.display.set_caption('Eden Model')

def gen_board():
    result  = np.zeros([N, N])
    i = int(N / 2)
    result[i][i] = 1
    return result

def draw(board):
    WINDOW = pygame.display.set_mode((N*8, N*8), 0, 32)
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
    fps_clock = pygame.time.Clock()
    fps_clock.tick(60)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

def next_gen(board):
    result = deepcopy(board)

    indexs_of_lifes_cels = []
    for i in range(N):
        for j in range(N):
           if result[i][j] == 1: indexs_of_lifes_cels.append([i, j])

    index = random.choice(indexs_of_lifes_cels)
    new_life_cel = random.choice([1, 2, 3, 4])

    if new_life_cel == 1 and result[index[0] + 1][index[1]] == 0:
        result[index[0] + 1][index[1]] = 1
    elif new_life_cel == 2 and result[index[0]][index[1] + 1] == 0:
        result[index[0]][index[1] + 1] = 1
    elif new_life_cel == 3 and result[index[0] - 1][index[1]] == 0:
        result[index[0] - 1][index[1]] = 1
    elif new_life_cel == 4 and result[index[0]][index[1] - 1] == 0:
        result[index[0]][index[1] - 1] = 1

    return result

def main():
    init()
    generation = gen_board()

    while True:
        draw(generation)
        update_pygame()
        generation = next_gen(generation)

if __name__ == '__main__':
    main()