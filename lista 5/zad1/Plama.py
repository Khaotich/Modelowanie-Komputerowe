import pygame
import sys
import numpy as np
from copy import copy
from pygame.locals import *

N = 100
P = 0.5

def init():
    pygame.init()
    pygame.display.set_caption('Plama')


def rand_board():
    return np.random.choice(a=[0, 1], size=(N, N), p=[1 - P, P]).reshape(N, N)


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


def next_gen(board):
    result = copy(board)

    for i in range(N):
        for j in range(N):
            nieghboards = 0
            #lewy górny róg
            if board[i][j] == 1: nieghboards += 1
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


            if nieghboards == 4  or nieghboards in range(6, 10):
                result[i][j] = 1
            else:
                result[i][j] = 0

    return result


def main():
    init()
    generation = rand_board()

    while True:
        draw(generation)
        update_pygame()
        generation = next_gen(generation)


if __name__ == '__main__':
    main()
