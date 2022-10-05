import numpy as np
from copy import deepcopy

N = 1000
P = 0.5

def rand_board():
    return np.random.choice(a=[0, 1], size=(N, N), p=[1 - P, P]).reshape(N, N)

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

    file = open(f'L={N}', 'w')
    
    for i in range(10):
        generation = rand_board()
        gens = 0

        while gens <= 1000:
            if gens == 1000: file.write(f'{count_alive(generation)/ N**2}\n')
            gens += 1
            generation = next_gen(generation)
        print(i+1)

    print('Finish')
    file.close()


if __name__ == '__main__':
    main()