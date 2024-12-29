def check(board, n, m):
    total_W = 0
    total_B = 0
    for i in range(n, n+8):
        for j in range(m, m+8):
            if (i+j)%2 == 0:
                if board[i][j] != "W":
                    total_W += 1
                elif board[i][j] != "B":
                    total_B += 1
            else:
                if board[i][j] != "B":
                    total_W += 1
                elif board[i][j] != "W":
                    total_B += 1
                    
    return min(total_W, total_B)
    
N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(input()))

num = 64
for n in range(N-7):
    for m in range(M-7):
        now = check(board, n, m)
        if num > now:
            num = now

print(num)