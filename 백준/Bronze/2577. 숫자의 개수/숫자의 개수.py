A = int(input())
B = int(input())
C = int(input())

total = str(A*B*C)
num_list = [0]*10

for i in total:
    num_list[int(i)] += 1

for num in num_list:
    print(num)
