import numpy as np
from copy import copy
from matplotlib import pyplot as plt

N = 100


def rand_board(P):
    return np.random.choice(a=[0, 1], size=(N, N), p=[1 - P, P]).reshape(N, N)


def next_gen(board):
    result = copy(board)

    for i in range(N):
        for j in range(N):
            nieghboards = 0
            #lewy górny róg
            if board[i][j] == 1:
                nieghboards += 1
            if i == 0 and j == 0:
                if board[N-1][N-1] == 1:
                    nieghboards += 1
                if board[N-1][0] == 1:
                    nieghboards += 1
                if board[N-1][1] == 1:
                    nieghboards += 1
                if board[0][1] == 1:
                    nieghboards += 1
                if board[1][1] == 1:
                    nieghboards += 1
                if board[1][0] == 1:
                    nieghboards += 1
                if board[1][N-1] == 1:
                    nieghboards += 1
                if board[0][N-1] == 1:
                    nieghboards += 1
            #prawy górny róg
            elif i == 0 and j == N-1:
                if board[N-1][N-2] == 1:
                    nieghboards += 1
                if board[N-1][N-1] == 1:
                    nieghboards += 1
                if board[0][N-1] == 1:
                    nieghboards += 1
                if board[0][0] == 1:
                    nieghboards += 1
                if board[1][0] == 1:
                    nieghboards += 1
                if board[0][1] == 1:
                    nieghboards += 1
                if board[1][N-2] == 1:
                    nieghboards += 1
                if board[0][N-2] == 1:
                    nieghboards += 1
            #lewy dolny bok
            elif i == N-1 and j == 0:
                if board[N-2][N-1] == 1:
                    nieghboards += 1
                if board[N-2][0] == 1:
                    nieghboards += 1
                if board[N-2][1] == 1:
                    nieghboards += 1
                if board[N-1][1] == 1:
                    nieghboards += 1
                if board[0][1] == 1:
                    nieghboards += 1
                if board[0][0] == 1:
                    nieghboards += 1
                if board[0][N-1] == 1:
                    nieghboards += 1
                if board[N-1][N-1] == 1:
                    nieghboards += 1
            #prawy dolny bok
            elif i == N-1 and j == N-1:
                if board[N-2][N-2] == 1:
                    nieghboards += 1
                if board[N-2][N-1] == 1:
                    nieghboards += 1
                if board[N-2][0] == 1:
                    nieghboards += 1
                if board[N-1][0] == 1:
                    nieghboards += 1
                if board[0][0] == 1:
                    nieghboards += 1
                if board[0][N-1] == 1:
                    nieghboards += 1
                if board[0][N-2] == 1:
                    nieghboards += 1
                if board[N-1][N-2] == 1:
                    nieghboards += 1
            #lewy bok
            elif (i > 0 and i < N - 1) and j == 0:
                if board[i-1][N-1] == 1:
                    nieghboards += 1
                if board[i-1][j] == 1:
                    nieghboards += 1
                if board[i-1][j+1] == 1:
                    nieghboards += 1
                if board[i][j+1] == 1:
                    nieghboards += 1
                if board[i+1][j+1] == 1:
                    nieghboards += 1
                if board[i+1][j] == 1:
                    nieghboards += 1
                if board[i+1][N-1] == 1:
                    nieghboards += 1
                if board[i][N-1] == 1:
                    nieghboards += 1
            #górny bok
            elif i == 0 and (j > 0 and j < N-1):
                if board[N-2][j-1] == 1:
                    nieghboards += 1
                if board[N-2][j] == 1:
                    nieghboards += 1
                if board[N-2][j+1] == 1:
                    nieghboards += 1
                if board[i][j+1] == 1:
                    nieghboards += 1
                if board[i+1][j+1] == 1:
                    nieghboards += 1
                if board[i+1][j] == 1:
                    nieghboards += 1
                if board[i+1][j-1] == 1:
                    nieghboards += 1
                if board[i-1][j-1] == 1:
                    nieghboards += 1
            #prawy bok
            elif (i > 0 and i < N-1) and j == N-1:
                if board[i-1][j-1] == 1:
                    nieghboards += 1
                if board[i-1][j] == 1:
                    nieghboards += 1
                if board[i-1][0] == 1:
                    nieghboards += 1
                if board[i][0] == 1:
                    nieghboards += 1
                if board[i+1][0] == 1:
                    nieghboards += 1
                if board[i+1][j] == 1:
                    nieghboards += 1
                if board[i+1][j-1] == 1:
                    nieghboards += 1
                if board[i][j-1] == 1:
                    nieghboards += 1
            #dolny bok
            elif i == N-1 and (j > 0 and j < N-1):
                if board[i-1][j-1] == 1:
                    nieghboards += 1
                if board[i-1][j] == 1:
                    nieghboards += 1
                if board[i-1][j+1] == 1:
                    nieghboards += 1
                if board[i][j+1] == 1:
                    nieghboards += 1
                if board[0][j+1] == 1:
                    nieghboards += 1
                if board[0][j] == 1:
                    nieghboards += 1
                if board[0][j-1] == 1:
                    nieghboards += 1
                if board[i][j-1] == 1:
                    nieghboards += 1
            #reszta
            else:
                if board[i-1][j-1] == 1:
                    nieghboards += 1
                if board[i-1][j] == 1:
                    nieghboards += 1
                if board[i-1][j+1] == 1:
                    nieghboards += 1
                if board[i][j+1] == 1:
                    nieghboards += 1
                if board[i+1][j+1] == 1:
                    nieghboards += 1
                if board[i+1][j] == 1:
                    nieghboards += 1
                if board[i+1][j-1] == 1:
                    nieghboards += 1
                if board[i][j-1] == 1:
                    nieghboards += 1

            if nieghboards == 4 or nieghboards in range(6, 10):
                result[i][j] = 1
            else:
                result[i][j] = 0

    x1 = 0
    x2 = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                x1 += 1
            if result[i][j] == 1:
                x2 += 1  
    
    return [result, x2/(N*N)]


def main():
    
    x = range(1001)
    y1 = []
    y2 = []
    y3 = []
    
    generation1 = rand_board(0.49)
    generation2 = rand_board(0.5)
    generation3 = rand_board(0.51)
    
    for _ in x:
        data1 = next_gen(generation1)
        generation1 = data1[0]
        y1.append(data1[1])
        data2 = next_gen(generation2)
        generation2 = data2[0]
        y2.append(data2[1])
        data3 = next_gen(generation3)
        generation3 = data3[0]
        y3.append(data3[1])

    plt.subplot(3, 1, 1)
    plt.plot(x, y1, label='0.49', color='red')
    plt.xlabel('Generacja')
    plt.ylabel('Stosunek fazy 1 do fazy 2')
    plt.title('p = 0.49')

    plt.subplot(3, 1, 2)
    plt.plot(x, y2, label='0.5', color='green')
    plt.xlabel('Generacja')
    plt.ylabel('Stosunek fazy 1 do fazy 2')
    plt.title('p = 0.5')
    
    plt.subplot(3, 1, 3)
    plt.plot(x, y3, label='0.51', color='blue')
    plt.xlabel('Generacja')
    plt.ylabel('Stosunek fazy 1 do fazy 2')
    plt.title('p = 0.51')

    plt.show()

if __name__ == '__main__':
    main()
