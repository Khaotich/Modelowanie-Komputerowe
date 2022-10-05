import random
import pygame
import sys
import numpy as np
from pygame.locals import *

N = 100

def init():
    pygame.init()
    pygame.display.set_caption('Model Płatka Śniegu')


def gen_board():
    # jeśli ustawimy two na True to wygeneruje się obraz dla twóch sąsiadów
    result = np.zeros([N, N])
    two = True

    if two:
        n = int(15 * random.random())
        s = 5
        for i in range(n):
            dx = int(s * (random.random() - 0.5))
            dy = int(s * (random.random() - 0.5))
            result[N // 2 + dx][N // 2 + dy] = 1
    else:
        result[N // 2][N // 2] = 1

    return result


def draw(board):
    WINDOW = pygame.display.set_mode((N * 8, N * 8), 0, 32)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    h = 0
    for i in range(N):
        w = 0
        for j in range(N):
            if board[i][j] == 1:
                pygame.draw.rect(WINDOW, WHITE, (w, h, 6, 6))
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
    result = np.zeros([N, N])
    ip = 0
    im = 0
    jp = 0
    jm = 0

    for i in range(N):
        for j in range(N):
            if i < N - 1:
                ip = i + 1
            else:
                ip = 0
            if i > 0:
                im = i - 1
            else:
                im = N - 1
            if j < N - 1:
                jp = j + 1
            else:
                jp = 0
            if j > 0:
                jm = j - 1
            else:
                jm = N - 1

            s1 = 0
            s2 = 0
            s3 = 0
            s4 = 0
            s5 = 0
            s6 = 0

            p = j % 2

            if p == 0:
                s1 = board[ip][j]
                s2 = board[ip][jp]
                s3 = board[i][jp]
                s4 = board[im][j]
                s5 = board[i][jm]
                s6 = board[ip][jm]
            elif p == 1:
                s1 = board[ip][j]
                s2 = board[i][jp]
                s3 = board[im][jp]
                s4 = board[im][j]
                s5 = board[im][jm]
                s6 = board[i][jm]

            suma = s1 + s2 + s3 + s4 + s5 + s6

            #if board[i][j] or (not board[i][j] and suma == 1):
            if board[i][j] or (not board[i][j] and suma == 2):
            #if board[i][j] or (not board[i][j] and suma > 0):
                result[i][j] = 1

    return result


def main():
    init()
    generation = gen_board()
    t = 0

    while True:
        draw(generation)
        update_pygame()
        # t = 45 dla n > 0
        # t = 45 dla n = 1
        # t = 80 dla n = 2
        if t < 80:
            generation = next_gen(generation)
        t += 1


if __name__ == '__main__':
    main()
