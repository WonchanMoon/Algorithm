N = int(input())
length = len(str(N))

answer = 0
for i in range(1, length * 9):
    temp = N - i
    if temp <= 0:
        break
    temp += sum([int(t) for t in str(temp)])
    if temp == N:
        answer = N - i

print(answer)