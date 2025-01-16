import sys

N, M = map(int, input().split())

not_hear = set()
not_see = set()
for _ in range(N):
    name = sys.stdin.readline().strip()
    not_hear.add(name)
for _ in range(M):
    name = sys.stdin.readline().strip()
    not_see.add(name)

not_hear_see = not_hear & not_see
print(len(not_hear_see))
not_hear_see = sorted(list(not_hear_see))
for name in not_hear_see:
    print(name)