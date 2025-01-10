from math import floor
def round_(num):
    return floor(num + 0.5)

import sys
from collections import deque
n = int(sys.stdin.readline())
if n == 0:
    print(0)
else:
    L = []
    for _ in range(n):
        L.append(int(sys.stdin.readline()))
    L.sort()
    del_n = round_(n * 15 / 100)
    L = deque(L)
    for _ in range(del_n):
        L.popleft()
        L.pop()
    print(round_(sum(L)/len(L)))