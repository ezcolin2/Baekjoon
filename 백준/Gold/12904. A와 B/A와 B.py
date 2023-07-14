import sys
input=sys.stdin.readline
s=input().rstrip()
t=input().rstrip()
while(len(t)>len(s)): # t의 길이가 s와 같아질 때까지
    if t[-1]=='A': # 마지막 A면 빼버림
        t=t[:-1]
    else: # 마지막 B면 빼고 뒤집음
        t=t[:-1]
        t=t[::-1]
print(1 if s==t else 0)