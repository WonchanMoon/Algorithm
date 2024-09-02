N = int(input())

stairs = [int(input()) for _ in range(N)]

dp = [[0, 0] for _ in range(N)]
dp[-1] = [0, stairs[-1]]

# 연속된 3개 계단은 불가
# 각 칸에 경우를 나누어 기록 (2칸을 내려갈 수밖에 없는 경우, 1칸 2칸 둘다 내려갈 수 있는 경우)

for i in range(N-1, -1, -1):
    two_step, one_two_step = dp[i]

    if two_step != 0 and i-2 >= 0:
        dp[i-2][1] = max(dp[i-2][1], two_step + stairs[i-2])
    if one_two_step != 0:
        if i - 1 >= 0:
            dp[i-1][0] = max(dp[i-1][0], one_two_step + stairs[i-1])
        if i - 2>= 0:
            dp[i-2][1] = max(dp[i-2][1], one_two_step + stairs[i-2])

if len(stairs) == 1:
    print(stairs[0])
else :
    print(max(max(dp[0]), max(dp[1])))