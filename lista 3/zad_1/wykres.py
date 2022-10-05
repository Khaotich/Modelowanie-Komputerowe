import random
import numpy as np
from copy import deepcopy
import math
from matplotlib import pyplot as plt

N = 100


def gen_board():
    result = np.zeros([N, N])
    i = int(N / 2)
    result[i][i] = 1
    return result


def next_gen(board):
    result = deepcopy(board)

    indexs_of_lifes_cels = []
    for i in range(N):
        for j in range(N):
            if result[i][j] == 1:
                indexs_of_lifes_cels.append([i, j])

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


def get_center(board):
    x = 0
    y = 0
    z = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                x += i
                y += j
                z += 1

    return [int(x / z), int(y / z)]


def max_r(board, r):
    result = r
    xy = get_center(board)
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                tmp_r = math.sqrt((i - xy[0]) ** 2 + (j - xy[1]) ** 2)
                if tmp_r > result:
                    result = tmp_r
    return result


def get_cels(board):
    result = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                result += 1
    return result


def main():
    generation = gen_board()
    r = 0
    t = 0
    x = []
    y = []

    while t <= 50000:
        generation = next_gen(generation)
        r = max_r(generation, r)
        x.append(get_cels(generation))
        y.append(r)
        t += 1

    plt.plot(x, y)
    plt.xlabel('Żywe Komórki')
    plt.ylabel('Promień')
    plt.title('Wykres zależności promienia od żywych komórek')
    plt.show()


if __name__ == '__main__':
    main()
