def solution(phone_number):
    back_number = phone_number[-4:]
    answer = '*'*(len(phone_number)-4)
    return answer + back_number