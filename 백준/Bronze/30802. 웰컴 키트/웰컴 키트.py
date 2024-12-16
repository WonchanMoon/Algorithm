import math

N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

num_T = 0
for size in sizes:
    num_T += math.ceil(size/T)
print(num_T)

print(N//P, end=' ')
print(N%P)
