N = int(input())
P = list(map(int, input().split()))
P.sort()

waiting = 0
total = 0
for p in P:
    waiting += p
    total += waiting
print(total)