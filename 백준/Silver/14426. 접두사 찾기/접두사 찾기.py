import sys
input=sys.stdin.readline
n, m = map(int, input().split())
s=[input().rstrip() for _ in range(n)]
arr=[input().rstrip() for _ in range(m)]
cnt=0
prefix_set=set()
# 모든 접두사들을 집합 안에 넣기
for string in s:
    for idx in range(1, len(string)+1):
        prefix_set.add(string[:idx])
#접두사인지 확인
for string in arr:
    if string in prefix_set:
        cnt+=1
print(cnt)