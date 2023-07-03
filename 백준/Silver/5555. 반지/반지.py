import sys
input=sys.stdin.readline
find=input().rstrip()
n=int(input())
cnt=0 # 문자열 포함 반지의 개수
for _ in range(n):
    temp=input().rstrip()
    temp*=2
    for i in range(len(temp)-len(find)): # 문자열 비교
        if temp[i:i+len(find)]==find:
            cnt+=1
            break
print(cnt)