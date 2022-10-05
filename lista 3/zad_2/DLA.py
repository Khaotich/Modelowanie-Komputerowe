import random
import pygame
import sys
import numpy as np
from copy import deepcopy
from pygame.locals import *
import math
from matplotlib import pyplot as plt

N = 100


def init():
    pygame.init()
    pygame.display.set_caption('DLA Model')


def gen_board():
    result = np.zeros([N, N])
    c = N // 2
    result[c][c] = 1

    for i in range(N):
        for j in range(N):
            if i == c and j == c:
                continue
            r = random.random()
            if r <= 0.2:
                result[i][j] = -1

    return result


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
    # fps_clock = pygame.time.Clock()
    # fps_clock.tick(60)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


def next_gen(board):
    result = deepcopy(board)

    for i in range(N):
        for j in range(N):
            if board[i][j] == -1:
                moves = [[1, 0], [-1, 0], [0, -1], [0, 1],
                         [1, 1], [1, -1], [-1, 1], [-1, -1]]
                x, y = random.choice(moves)
                while True:
                    x, y = random.choice(moves)
                    if 0 < i + x < N and 0 < j + y < N:
                        break
                if result[i + x][j + y] == 0:
                    result[i + x][j + y] = -1
                    result[i][j] = 0

    for i in range(N):
        for j in range(N):
            try:
                if result[i][j] == -1:
                    if result[i + 1][j] == 1 or result[i - 1][j] == 1 or result[i][j + 1] == 1 or result[i][j - 1] == 1:
                        result[i][j] = 1
            except:
                continue

    return result


def max_r(board, r):
    result = r
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                tmp_r = math.sqrt((i - N // 2) ** 2 + (j - N // 2) ** 2)
                if tmp_r > result:
                    result = tmp_r
    return result


def main():
    init()
    generation = gen_board()
    r = 0
    t = 0
    x = []
    y = []

    while t <= 1000:
        draw(generation)
        update_pygame()
        generation = next_gen(generation)
        r = max_r(generation, r)
        x.append(t)
        y.append(r)
        t += 1

    plt.plot(x, y)
    plt.xlabel('Czas')
    plt.ylabel('Promień')
    plt.title('Wykres zależności promienia od czasu')
    plt.show()


if __name__ == '__main__':
    main()
