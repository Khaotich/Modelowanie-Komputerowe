import pygame
import sys
import numpy as np
from copy import deepcopy
from pygame.locals import *

N = 100
P = 0.50

def init():
    pygame.init()
    pygame.display.set_caption('Game of Life')

def rand_board():
    return np.random.choice(a=[0, 1], size=(N, N), p=[1 - P, P]).reshape(N, N)

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
    #fps_clock = pygame.time.Clock()
    #fps_clock.tick(60)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

def next_gen(board):
    result = deepcopy(board)

    for i in range(N):
        for j in range(N):
            nieghboards = 0
            #lewy górny róg
            if i == 0 and j == 0:
                if board[N-1][N-1] == 1: nieghboards += 1
                if board[N-1][0] == 1: nieghboards += 1
                if board[N-1][1] == 1: nieghboards += 1
                if board[0][1] == 1: nieghboards += 1
                if board[1][1] == 1: nieghboards += 1
                if board[1][0] == 1: nieghboards += 1
                if board[1][N-1] == 1: nieghboards += 1
                if board[0][N-1] == 1: nieghboards += 1
            #prawy górny róg
            elif i == 0 and j == N-1:
                if board[N-1][N-2] == 1: nieghboards += 1
                if board[N-1][N-1] == 1: nieghboards += 1
                if board[0][N-1] == 1: nieghboards += 1
                if board[0][0] == 1: nieghboards += 1
                if board[1][0] == 1: nieghboards += 1
                if board[0][1] == 1: nieghboards += 1
                if board[1][N-2] == 1: nieghboards += 1
                if board[0][N-2] == 1: nieghboards += 1
            #lewy dolny bok
            elif i == N-1 and j == 0:
                if board[N-2][N-1] == 1: nieghboards += 1
                if board[N-2][0] == 1: nieghboards += 1
                if board[N-2][1] == 1: nieghboards += 1
                if board[N-1][1] == 1: nieghboards += 1
                if board[0][1] == 1: nieghboards += 1
                if board[0][0] == 1: nieghboards += 1
                if board[0][N-1] == 1: nieghboards += 1
                if board[N-1][N-1] == 1: nieghboards += 1
            #prawy dolny bok
            elif i == N-1 and j == N-1:
                if board[N-2][N-2] == 1: nieghboards += 1
                if board[N-2][N-1] == 1: nieghboards += 1
                if board[N-2][0] == 1: nieghboards += 1
                if board[N-1][0] == 1: nieghboards += 1
                if board[0][0] == 1: nieghboards += 1
                if board[0][N-1] == 1: nieghboards += 1
                if board[0][N-2] == 1: nieghboards += 1
                if board[N-1][N-2] == 1: nieghboards += 1
            #lewy bok
            elif (i > 0 and i < N - 1) and j == 0:
                if board[i-1][N-1] == 1: nieghboards += 1
                if board[i-1][j] == 1: nieghboards += 1
                if board[i-1][j+1] == 1: nieghboards += 1
                if board[i][j+1] == 1: nieghboards += 1
                if board[i+1][j+1] == 1: nieghboards += 1
                if board[i+1][j] == 1: nieghboards += 1
                if board[i+1][N-1] == 1: nieghboards += 1
                if board[i][N-1] == 1: nieghboards += 1
            #górny bok
            elif i == 0 and (j > 0 and j < N-1):
                if board[N-2][j-1] == 1: nieghboards += 1
                if board[N-2][j] == 1: nieghboards += 1
                if board[N-2][j+1] == 1: nieghboards += 1
                if board[i][j+1] == 1: nieghboards += 1
                if board[i+1][j+1] == 1: nieghboards += 1
                if board[i+1][j] == 1: nieghboards += 1
                if board[i+1][j-1] == 1: nieghboards += 1
                if board[i-1][j-1] == 1: nieghboards += 1
            #prawy bok
            elif (i > 0 and i < N-1) and j == N-1:
                if board[i-1][j-1] == 1: nieghboards += 1
                if board[i-1][j] == 1: nieghboards += 1
                if board[i-1][0] == 1: nieghboards += 1
                if board[i][0] == 1: nieghboards += 1
                if board[i+1][0] == 1: nieghboards += 1
                if board[i+1][j] == 1: nieghboards += 1
                if board[i+1][j-1] == 1: nieghboards += 1
                if board[i][j-1] == 1: nieghboards += 1
            #dolny bok
            elif i == N-1 and (j > 0 and j < N-1):
                if board[i-1][j-1] == 1: nieghboards += 1
                if board[i-1][j] == 1: nieghboards += 1
                if board[i-1][j+1] == 1: nieghboards += 1
                if board[i][j+1] == 1: nieghboards += 1
                if board[0][j+1] == 1: nieghboards += 1
                if board[0][j] == 1: nieghboards += 1
                if board[0][j-1] == 1: nieghboards += 1
                if board[i][j-1] == 1: nieghboards += 1
            #reszta
            else:
                if board[i-1][j-1] == 1: nieghboards += 1
                if board[i-1][j] == 1: nieghboards += 1
                if board[i-1][j+1] == 1: nieghboards += 1
                if board[i][j+1] == 1: nieghboards += 1
                if board[i+1][j+1] == 1: nieghboards += 1
                if board[i+1][j] == 1: nieghboards += 1
                if board[i+1][j-1] == 1: nieghboards += 1
                if board[i][j-1] == 1: nieghboards += 1


            if board[i][j] == 1 and (nieghboards < 2 or nieghboards > 3):
                result[i][j] = 0

            if board[i][j] == 0 and nieghboards == 3:
                result[i][j] = 1

    return result

def count_alive(board):
    result = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1: result += 1
    return result

def main():
    init()

    file = open(f'p={P}', 'w')
    generation = rand_board()
    gens = 0

    while True:
        draw(generation)
        update_pygame()

        if gens < 1000:
            file.write(f'{gens} {count_alive(generation)/ 10000}\n')
        elif gens == 1000:
            file.close()
            print('Finish')

        gens += 1
        generation = next_gen(generation)


if __name__ == '__main__':
    main()