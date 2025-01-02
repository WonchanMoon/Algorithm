from collections import deque

N, K = map(int, input().split())
queue = deque([i+1 for i in range(N)])

print("<", end='')
i = 1
while queue:
    now = queue.popleft()
    if i != K:
        queue.append(now)
        i += 1
    else:
        i = 1
        if not queue: 
            print(now, end = '')
        else : 
            print(now, end = ", ")
print(">")