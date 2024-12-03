def solution(left, right):
    answer = 0
    for num in range(left, right+1):
        if factor_even(num):
            answer += num
        else:
            answer -= num
    return answer

def factor_even(num):
    if num ** 0.5 == round(num**0.5):
        return False
    return True
        
        
    