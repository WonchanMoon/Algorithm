from collections import deque

def solution(maps):
    
    n = len(maps[0])
    m = len(maps)
    
    queue = deque()
    queue.append((0,0))
    
    while queue:
        (x, y) = queue.popleft()
        
        if x + 1 < n:
            if maps[y][x+1] != 0 and maps[y][x+1] == 1 and (x+1,y) != (0,0):
                maps[y][x+1] = 1 + maps[y][x]
                queue.append((x+1, y))
                
        if x - 1 >= 0:
            if maps[y][x-1] != 0 and maps[y][x-1] == 1 and (x-1,y) != (0,0):
                maps[y][x-1] = 1 + maps[y][x]
                queue.append((x-1, y))
                
        if y + 1 < m:
            if maps[y+1][x] != 0 and maps[y+1][x] == 1 and (x,y+1) != (0,0):
                maps[y+1][x] = 1 + maps[y][x]
                queue.append((x, y+1))
                
        if y - 1 >= 0:
            if maps[y-1][x] != 0 and maps[y-1][x] == 1 and (x,y-1) != (0,0):
                maps[y-1][x] = 1 + maps[y][x]
                queue.append((x, y-1))
    
    if maps[m-1][n-1] == 1:
        return -1
    else:
        return maps[m-1][n-1]
