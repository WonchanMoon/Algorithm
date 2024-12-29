from bisect import bisect_left

N = int(input())
A = sorted(list(map(int, input().split())))
M = int(input())
B = list(map(int, input().split()))
for num in B:
    index = bisect_left(A, num)
    if index < len(A) and A[index] == num:
        print(1)
    else:
        print(0)