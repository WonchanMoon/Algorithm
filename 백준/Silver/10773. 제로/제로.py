K = int(input())

L = []
for _ in range(K):
    now = int(input())
    if now == 0:
        L.pop()
    else:
        L.append(now)
        
print(sum(L))