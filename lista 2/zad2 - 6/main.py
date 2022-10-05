from random import choice
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

N = 10000

def walk_1d(n):
    x = 0
    y = 0
    x_ = [0]
    y_ = [0]
    for _ in range(n):
        r = choice([-1, 1])
        x += 1
        y += r
        x_.append(x)
        y_.append(y)

    return [x_, y_]

def walk_2d(n):
    x = 0
    y = 0
    x_ = [0]
    y_ = [0]
    direction = [1, 2, 3, 4]

    for _ in range(n):
        f = choice(direction)
        if f == 1: x += 1
        elif f == 2: y += 1
        elif f == 3: x -= 1
        else: y -= 1

        x_.append(x)
        y_.append(y)

    return [x_, y_]

def walk_3d(n):
    R = (np.random.rand(n) * 6).astype("int")
    x = np.zeros(n)
    y = np.zeros(n)
    z = np.zeros(n)
    x[R == 0] = -1
    x[R == 1] = 1
    y[R == 2] = -1
    y[R == 3] = 1
    z[R == 4] = -1
    z[R == 5] = 1

    x = np.cumsum(x)
    y = np.cumsum(y)
    z = np.cumsum(z)

    return [x, y, z]

#zadanie 2
def draw(nd):
    if nd == 1:
        for _ in range(5):
            walk = walk_1d(N)
            plt.plot(walk[0], walk[1])
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('1D Random Walk')
        plt.show()
    elif nd == 2:
        for _ in range(5):
            walk = walk_2d(N)
            plt.plot(walk[0], walk[1])
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('2D Random Walk')
        plt.show()
    #zadanie 5
    elif nd == 3:
        walk = walk_3d(N)
        plt.figure()
        ax = plt.subplot(1,1,1, projection='3d')
        ax.plot(walk[0], walk[1], walk[2], alpha=0.9)
        ax.scatter(walk[0][-1], walk[1][-1], walk[2][-1])
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('3D Random Walk')
        plt.show()

#zadanie 3
def his_1d(n):
    points = []
    for _ in range(n):
        points.append(walk_1d(1000)[1][-1])
    plt.hist(points, density=True, bins=30)
    plt.title("Uśredniony rozkład odległości")
    plt.show()

    q = []
    l = []
    for i in points:
        if i not in q: q.append(i)
    for i in n:
        l.append([i, points.count(i)])
    p = sorted(l, key= lambda l: l[1], reverse=True)
    for i in p: print(i)

#zadanie 4
def p():
    end_1d = 0
    end_2d = 0
    end_3d = 0
    for _ in range(N):
        walk_1 = walk_1d(N)
        walk_2 = walk_2d(N)
        walk_3 = walk_3d(N)
        for i in range(N):
            if walk_1[1][i] == 0: end_1d += 1
            if walk_2[0][i] == 0 and walk_2[1][i] == 0: end_2d += 1
            if walk_3[0][i] == 0 and walk_3[1][i] == 0 and walk_3[2][i] == 0: end_3d += 1

    print(f'p dla 1D = {end_1d / (N*N)} \n'
          f'p dla 2D = {end_2d / (N*N)} \n'
          f'p dla 3D = {end_3d / (N*N)}')

#zadanie 5
def walk_2d_4_directions(n):
    x = 0
    y = 0
    direction = [1, 2, 3, 4]
    for _ in range(n):
        f = choice(direction)
        if f == 1: x += 1
        elif f == 2: y += 1
        elif f == 3: x -= 1
        else: y -= 1

    return [x, y]

def walk_2d_8_directions(n):
    x = 0
    y = 0
    direction = [1, 2, 3, 4, 5, 6, 7, 8]
    for _ in range(n):
        f = choice(direction)
        if f == 1:
            y += 1
        elif f == 2:
             x += 1
             y += 1
        elif f == 3:
            x += 1
        elif f == 4:
            x += 1
            y -= 1
        elif f == 5:
            y -= 1
        elif f == 6:
            x -= 1
            y -= 1
        elif f == 7:
            x -= 1
        else:
            x -= 1
            y += 1

    return [x, y]

def D():
    sum_4 = 0
    sum_8 = 0
    for _ in range(N):
        d_4 = walk_2d_4_directions(N)
        d_8 = walk_2d_8_directions(N)
        for i in d_4: sum_4 += i ** 2
        for i in d_8: sum_8 += i ** 2

    print(f'D dla 4 kierunków: {sqrt(sum_4) / (N * 4)}')
    print(f'D dla 8 kierunków: {sqrt(sum_8) / (N * 4)}')

def main():
    D()


if __name__ == '__main__':
    main()