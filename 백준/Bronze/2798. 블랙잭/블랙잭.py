from itertools import combinations

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

total = 0
for combi in combinations(numbers, 3):
    if total < sum(combi) < M:
        total = sum(combi)
    if sum(combi) == M:
        total = sum(combi)
        break
        
print(total)