# 3차원 dp를 사용한다.
# dp[i][j][k] : 길이가 i이고 끝 번호가 j이면서 현재까지 나온 숫자들을 비트로 표현했을 때 k일 때 계단 수의 개수
n = int(input())
dp = [[[0 for _ in range(1024)] for _ in range(10)] for _ in range(n+1)]
# 길이가 1일 때 초기화 (0으로 시작하는 것은 계단수가 아니기 때문에 제외)
for i in range(1, 10):
    dp[1][i][2**i] = 1

for i in range(1, n): # 길이
    for j in range(10): # 끝 숫자
        for k in range(1024): # 지금까지 등장한 숫자
            # 만약 해당 조건의 계단수가 없으면 스킵
            if dp[i][j][k] == 0:
                continue
            if j>0:
                dp[i+1][j-1][k | 2**(j-1)] += dp[i][j][k] 
            if j<9:
                dp[i+1][j+1][k | 2**(j+1)] += dp[i][j][k]
result = 0
for i in range(10):
    result += dp[n][i][1023]
print(result%1000000000)