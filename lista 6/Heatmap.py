import numpy as np
from copy import copy
from random import randint
from matplotlib import pyplot as plt

N = 100


def rand_board():
    return np.zeros((N, N), dtype=int)


def next_gen(board, x, y):
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
    generation = rand_board()
    x_c = N // 2
    y_c = N // 2
    t = 0

    #1-góra, 2-prawo, 3-dół, 4-lewo
    destination = randint(1, 4)
    tab = np.zeros((N, N), dtype=int)

    while t < 11000:
        tab[x_c][y_c] += 1

        x_c, y_c = move(destination, x_c, y_c)
        destination = destiny(destination, x_c, y_c, generation)
        generation = next_gen(generation, x_c, y_c)
        print(t)
        t += 1

    plt.imshow(tab, cmap='hot', interpolation='nearest')
    plt.show()


if __name__ == '__main__':
    main()