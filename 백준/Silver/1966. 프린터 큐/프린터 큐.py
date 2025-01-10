from collections import deque

n = int(input())
for _ in range(n):
    N, M = map(int, input().split())
    imp = list(map(int, input().split()))
    queue = deque([i for i in range(N)])
    order = 1
    while True:
        now = queue.popleft()
        if imp[now] != max(imp):
            queue.append(now)
        else:
            if now == M:
                print(order)
                break
            else:
                imp[now] = 0
                order += 1