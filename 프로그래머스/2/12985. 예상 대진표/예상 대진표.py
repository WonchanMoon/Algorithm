from math import ceil

def solution(n,a,b):
    answer = 1
    
    a,b = sorted([a,b])
    
    while (a+1 != b) or (a%2==0):
        a = ceil(a/2)
        b = ceil(b/2)
        answer += 1
    
    return answer