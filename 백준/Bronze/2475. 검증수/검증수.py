numbers = input().split()

last_num = 0
for num in numbers:
    last_num += int(num)**2

print(last_num%10)