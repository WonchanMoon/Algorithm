def solution(N, number):
    
    # 가능한 계산 결과를 저장할 리스트
    dp = [set() for _ in range(9)]
    
    # 기본적으로 N을 i번 사용한 결과를 dp[i]에 저장
    for i in range(1, 9):
        dp[i].add(int(str(N) * i))  # 예를 들어, 5, 55, 555, ...

    # i는 N을 사용한 횟수
    for i in range(1, 9):
        for j in range(1, i):
            for x in dp[j]:
                for y in dp[i - j]:
                    dp[i].add(x + y)
                    dp[i].add(x - y)
                    dp[i].add(x * y)
                    if y != 0:
                        dp[i].add(x // y)
        
        # 목표 숫자가 dp[i]에 포함되어 있다면 그 때의 i값을 반환
        if number in dp[i]:
            return i
    
    # N을 8번 사용해도 못 만들면 -1 반환
    return -1



