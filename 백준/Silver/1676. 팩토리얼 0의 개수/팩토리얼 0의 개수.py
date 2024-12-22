N = int(input())
fac = 1
for i in range(1, N+1):
    fac *= i
fac = str(fac)

num = 0
for j in fac[::-1]:
    if j != '0':
        break
    else:
        num += 1
        
print(num)