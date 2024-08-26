def solution(triangle):
    answer = 0
    
    # 아래부터 높은 수를 선택하면 최대
    for i in range(len(triangle)-2, -1, -1):
        row = triangle[i]
        for j in range(len(row)):
            triangle[i][j] = triangle[i][j] + max(triangle[i+1][j], triangle[i+1][j+1])
    return triangle[0][0]