def solution(arr):
    answer = []
    before = 10
    for i in arr:
        if i == before:
            continue
        answer.append(i)
        before = i
        
    return answer