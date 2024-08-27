def solution(numbers):
    answer = [-1] * len(numbers)
    
    for i in range(len(numbers)-2, -1, -1):
        if numbers[i] < numbers[i+1]:
            answer[i] = numbers[i+1]
        else:
            j = 1
            while True:
                if answer[i+j] == -1:
                    break
                if numbers[i] < answer[i+j]:
                    answer[i] = answer[i+j]
                    break
                j += 1
    return answer