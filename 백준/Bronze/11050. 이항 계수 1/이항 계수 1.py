N, K = map(int, input().split())

upper = 1
lower = 1
for i in range(K):
    upper *= N-i
    lower *= i+1
    
print(upper//lower)