# 백준 9081
# 문자열
import sys
input=sys.stdin.readline
t=int(input())
def next_string(x): # 사전 식으로 x 다음 문자 반환
    arr=[]
    for i in range(len(x)-1, -1 ,-1):
        for j in range(i-1, -1, -1):
            if x[j]<x[i]:
                arr.append((j, i))
    if arr: # arr가 비어있지 않다면
        arr.sort(key=lambda x : -x[0])
        j, i = arr[0]
        x[j], x[i] = x[i], x[j]
        return x[:j+1]+sorted(x[j+1:])
    return x
for _ in range(t):
    s=input().rstrip()
    print(''.join(next_string(list(s))))