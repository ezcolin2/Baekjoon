import sys
input=sys.stdin.readline

#인덱스 맞추기 위해 앞에 의미없는 문자 추가. 
s1 = [0]+list(input().rstrip())
s2 = [0]+list(input().rstrip())

#dp[x][y] 
#첫 번째 문자열 x번째까지와 두 번째 문자열 y번째까지 비교했을 때 LCS 길이

dp=[[0]*len(s2) for _ in range(len(s1))]
for i in range(1, len(s1)):
    for j in range(1, len(s2)):
        if s1[i]==s2[j]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i][j-1], dp[i-1][j])
print(dp[len(s1)-1][len(s2)-1])