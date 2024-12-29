N = int(input())

group = []
for i in range(N):
    w, h = map(int, input().split())
    group.append((w,h))

for i in range(N):
    now = group[i]
    rank = 1
    for target in group:
        if now[0] < target[0] and now[1] < target[1]:
            rank += 1
    print(rank, end = ' ')