n = int(input())
# dp[i][0] : i번째 행까지 고려하고 i번째 행에서 사자를 배치하지 않았을 때
# dp[i][1] : i번째 행까지 고려하고 i번째 행에서 왼쪽에 사자를 배치했을 때
# dp[i][2] : i번째 행까지 고려하고 i번째 행에서 오른쪽에 사자를 배치했을 때
dp = [[0, 0, 0] for _ in range(n)]

# dp 배열 초기화
dp[0][0] = 1 # 배치하지 않는 경우의 수는 하나
dp[0][1] = 1
dp[0][2] = 1
for i in range(1, n):
    # 배치하지 않는 경우의 수는 이전 행에서 (배치하지 않았을 경우 + 배치한 경우)
    dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % 9901
    dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % 9901
    dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % 9901

print(sum(dp[-1])%9901)