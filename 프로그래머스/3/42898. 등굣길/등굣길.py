from collections import deque

def solution(m, n, puddles):
    answer = 0
    
    board = []
    for _ in range(n+1):
        board.append([0]*(m+1))   
    board[0][1] = 1
    
    # return board
    for j in range(1, n+1):
        for i in range(1, m+1):
            # print(i,j)
            if [i,j] in puddles:
                continue
            board[j][i] = board[j-1][i] + board[j][i-1]
    # return board
    return board[n][m] % 1000000007