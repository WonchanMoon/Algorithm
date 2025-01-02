from collections import deque

N = int(input())
queue = deque([i+1 for i in range(N)])

while len(queue)>1:
    queue.popleft()
    go_back = queue.popleft()
    queue.append(go_back)
    
print(queue.popleft())