s1 = input()
s2 = input()
s3 = input()
if s1.isdigit():
    num = int(s1)+3
if s2.isdigit():
    num = int(s2)+2
if s3.isdigit():
    num = int(s3)+1
    
result = ""
if num%3 == 0:
    result += "Fizz"
if num%5 == 0:
    result += "Buzz"

if result != "":
    print(result)
else:
    print(num)